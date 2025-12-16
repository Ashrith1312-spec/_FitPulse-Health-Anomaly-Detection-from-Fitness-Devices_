# FitPulse Health Anomaly Detection - Milestone 1

##  Objective
The goal of Milestone 1 is to build a robust data preprocessing pipeline for fitness tracker data. This involves ingesting raw CSV logs (Heart Rate, Steps, Sleep), normalizing timestamps to a consistent UTC format, handling missing values, and aligning all metrics to a unified 1-minute interval frequency.

##  Dataset Source
* **Source:** FitBit Fitness Tracker Data (Public Dataset)
* **Files Used:**
    * `heartrate_seconds_merged.csv` (Raw heart rate values)
    * `minuteStepsNarrow_merged.csv` (Step counts per minute)
    * `minuteSleep_merged.csv` (Sleep stage logs)

##  Steps Performed
1.  **Data Ingestion:** Loaded raw CSV files using Pandas and validated the schema.
2.  **Time Normalization:** Converted all `timestamp` columns to datetime objects and standardized them to **UTC**.
3.  **Resampling & Alignment:** * Aggregated Heart Rate (seconds) to **1-minute averages**.
    * Aggregated Steps (minutes) to **1-minute sums**.
    * Aligned Sleep logs to the same 1-minute timeline.
4.  **Handling Missing Values:**
    * **Heart Rate:** Applied **Linear Interpolation** to fill gaps smoothly.
    * **Steps/Sleep:** Filled `NaN` values with `0`.
5.  **Output Generation:** Exported the final cleaned dataset to `fitpulse_milestone1_cleaned.csv`.

##  Tools Used
* **Python** (Pandas, NumPy)
* **Streamlit** (User Interface)
* **Matplotlib/Seaborn** (Visualization)

##  Key Insights
* **Data Alignment:** Successfully aligned high-frequency heart rate data (seconds) with lower-frequency steps data.
* **Interpolation:** The visualization confirms that linear interpolation effectively bridges gaps in heart rate data.
