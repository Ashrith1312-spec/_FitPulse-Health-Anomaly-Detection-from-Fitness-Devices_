# FitPulse Health Anomaly Detection - Milestone 1
## Data Ingestion and Preprocessing Pipeline

### 1. Objective
The primary objective of this milestone is to design and implement a robust data engineering pipeline. This pipeline is responsible for ingesting, cleaning, and normalizing raw fitness tracker data. By consolidating disparate data sources (Heart Rate, Steps, and Sleep logs) into a high-quality, "Gold Standard" dataset, we establish the foundation required for advanced anomaly detection and analysis in subsequent project phases.

### 2. Dataset Description
**Source:** The data is derived from the **Fitbit Fitness Tracker Data** (publicly available via Kaggle or similar repositories), consisting of minute-level output for physical activity, heart rate, and sleep monitoring.

**Files Processed:**
* **`minuteSleep_merged.csv`**: Logs sleep states at minute-level granularity.
* **`minuteStepsNarrow_merged.csv`**: Logs step counts at minute-level granularity.
* **`heartrate_seconds_merged.csv`**: Logs heart rate values at varying second-level intervals.

**Data Characteristics:**
* **Granularity Mismatch:** Heart rate data (seconds) vs. Steps/Sleep data (minutes).
* **Timezone Inconsistency:** Timestamps required normalization to a standard timezone.
* **Data Quality:** Raw data contained missing values and unaligned timestamps.

### 3. Steps Performed

#### **Step 1: Data Ingestion & Schema Validation**
* Ingested three raw CSV files using Pandas.
* Validated the schema by checking for required columns.
* Standardized column names (renaming `date`/`ActivityMinute` to `Time`, and `value` to `Sleep`/`Steps`) to ensure consistency across datasets.
* Enforced string data types for the `Id` column to prevent merging errors.

#### **Step 2: Timestamp Normalization**
* Converted all timestamp columns to Python `datetime` objects.
* **Floored** heart rate timestamps to the nearest minute to match the granularity of the steps and sleep datasets.
* Normalized all timestamps to **UTC** (Coordinated Universal Time) to ensure a unified timeline.

#### **Step 3: Aggregation & Merging**
* **Aggregation:** Grouped data by `Id` and `Time` to handle duplicates before merging:
    * *Heart Rate:* Calculated the **mean** per minute.
    * *Steps:* Calculated the **sum** per minute.
    * *Sleep:* Took the **max** value to capture the dominant sleep state.
* **Merging:** Performed an `inner join` on all three datasets to create a single consolidated dataframe containing only aligned time periods.

#### **Step 4: Cleaning & Resampling**
* **Imputation (Handling Nulls):**
    * Missing `Steps` and `Sleep` values were filled with `0` (implying inactivity or awake state).
    * Missing `HeartRate` values were filled with the **median** value to avoid skewing the data with outliers.
* **Alignment:** Resampled the entire dataset to a strict **1-minute frequency** for every user. This ensured a continuous timeline and exposed hidden gaps in data recording.

### 4. Tools Used
* **Python:** The core programming language for the pipeline.
* **Pandas:** Used for data ingestion (`read_csv`), dataframe manipulation, merging (`merge`), and time-series resampling (`resample`).
* **NumPy:** Used for numerical operations and handling `NaN` values effectively.

### 5. Key Insights
1.  **Granularity Alignment:** The raw heart rate data was recorded every few seconds, resulting in a much larger file than the steps or sleep data. Aggregating this to the minute level was critical for merging without creating massive data redundancy.
2.  **Timeline Gaps:** The resampling process revealed significant gaps where users likely removed their devices. Filling these gaps with appropriate default values (0 for steps, median for HR) ensures that future machine learning models receive a continuous stream of data without crashing on missing rows.
3.  **UTC Standardization:** Converting local times to UTC prevents analysis errors related to daylight savings or timezone differences between users.
