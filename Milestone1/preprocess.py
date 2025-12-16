import pandas as pd
import os

# =========================================================
# STEP 1: Ingest & Merge Raw Data
# ---------------------------------------------------------
def load_and_merge_raw_data(data_folder="/content/"):
    print("--- Step 1: Ingesting Raw Data ---")
    try:
        # Load raw files
        sleep = pd.read_csv(os.path.join(data_folder, "minuteSleep_merged.csv"), low_memory=False)
        steps = pd.read_csv(os.path.join(data_folder, "minuteStepsNarrow_merged.csv"), low_memory=False)
        hr = pd.read_csv(os.path.join(data_folder, "heartrate_seconds_merged.csv"), low_memory=False)

        # Standardize Names
        sleep = sleep.rename(columns={"date": "Time", "value": "Sleep"})
        steps = steps.rename(columns={"ActivityMinute": "Time"})
        hr = hr.rename(columns={"Value": "HeartRate"})

        # Fix IDs
        for df in [sleep, steps, hr]:
            df["Id"] = df["Id"].astype(str)

        # Parse Dates (Explicit format speeds this up significantly)
        fmt = "%m/%d/%Y %I:%M:%S %p"
        sleep["Time"] = pd.to_datetime(sleep["Time"], format=fmt, errors="coerce")
        steps["Time"] = pd.to_datetime(steps["Time"], format=fmt, errors="coerce")
        hr["Time"] = pd.to_datetime(hr["Time"], format=fmt, errors="coerce").dt.floor("min")

        # Aggregate to 1-minute level to prevent duplicates
        sleep_agg = sleep.groupby(["Id", "Time"], as_index=False)["Sleep"].max()
        steps_agg = steps.groupby(["Id", "Time"], as_index=False)["Steps"].sum()
        hr_agg = hr.groupby(["Id", "Time"], as_index=False)["HeartRate"].mean()

        # Merge
        merged = steps_agg.merge(sleep_agg, on=["Id", "Time"], how="inner") \
                          .merge(hr_agg, on=["Id", "Time"], how="inner")
        
        print(f"✓ Raw data merged. Shape: {merged.shape}")
        return merged

    except FileNotFoundError:
        print("❌ Error: Raw files not found. Please upload minuteSleep, minuteSteps, and heartrate_seconds.")
        return pd.DataFrame()

# =========================================================
# STEP 2: Processing Pipeline (Your Code)
# ---------------------------------------------------------
def normalize_timestamps(df):
    df["Time"] = pd.to_datetime(df["Time"], errors="coerce", utc=True)
    df = df.dropna(subset=["Time"])
    return df

def clean_dtypes(df):
    df["Steps"] = pd.to_numeric(df["Steps"], errors="coerce").fillna(0)
    df["Sleep"] = pd.to_numeric(df["Sleep"], errors="coerce").fillna(0)
    df["HeartRate"] = pd.to_numeric(df["HeartRate"], errors="coerce")
    return df

def align_to_minute(df):
    df = (
        df.set_index("Time")
          .groupby("Id")
          .resample("1min")
          .agg({"Steps": "sum", "Sleep": "max", "HeartRate": "mean"})
          .reset_index()
    )
    # Fill gaps created by resampling
    df["Steps"] = df["Steps"].fillna(0)
    df["Sleep"] = df["Sleep"].fillna(0)
    df["HeartRate"] = df["HeartRate"].fillna(df["HeartRate"].median())
    return df

def final_cleanup(df):
    return df.dropna().sort_values(["Id", "Time"])

# =========================================================
# MAIN EXECUTION
# =========================================================
if __name__ == "__main__":
    # 1. Start from Raw Data
    df = load_and_merge_raw_data()
    
    if not df.empty:
        # 2. Apply your cleaning pipeline
        df = normalize_timestamps(df)
        df = clean_dtypes(df)
        df = align_to_minute(df)  # This includes handling missing values via resampling
        df = final_cleanup(df)

        # 3. Save Final Output
        output_path = "/content/fitbit_clean_final.csv"
        df.to_csv(output_path, index=False)
        print(f" Success! Final dataset saved to {output_path}")
        print("Final Shape:", df.shape)