# FitPulse Health Anomaly Detection – Milestone 2
## Feature Extraction, Trend Modeling, and Behavioral Pattern Analysis

### 1. Objective

The primary objective of Milestone 2 is to extract meaningful statistical and time-series features from the preprocessed fitness dataset generated in Milestone 1. In addition, this milestone focuses on modeling temporal trends and exploring behavioral patterns using unsupervised learning techniques. These steps help build the analytical groundwork required for anomaly detection and behavioral analysis in later stages of the project.

### 2. Dataset Description

This milestone uses a cleaned and consolidated dataset derived from wearable fitness tracking data. The dataset was produced as the final output of Milestone 1 after performing data ingestion, timestamp normalization, aggregation, and missing-value handling.

### Dataset File

Filename: Clean.csv

Format: CSV (Comma-Separated Values)

### Dataset Structure

Total Records: 374

Total Features: 17

Primary Identifier: person_id

Temporal Attribute: timestamp

Each row represents a timestamped observation for an individual user, capturing physiological, activity-based, and lifestyle-related metrics.

### Variables Included

Time-Series Variables (Dynamic Features):

heart_rate – Heart rate measurements

daily_steps – Number of steps recorded

sleep_duration – Total sleep duration

stress_level – Stress indicator

These variables are treated as time-series signals and are used for automated feature extraction, trend modeling, and behavioral analysis.

### Demographic and Lifestyle Variables (Static / Categorical Features):

gender

age

occupation

job_category

bmi_category

weight_category

sleep_disorder

These attributes provide contextual information about users and are incorporated as metadata during feature construction and clustering.

### Data Characteristics

Timestamped observations across multiple users

Limited per-user temporal depth

Combination of physiological signals and activity-related data

Suitable for time-series feature extraction and unsupervised learning

### 3. Steps Performed
#### Step 1: Automated Time-Series Feature Extraction

TSFresh was applied to automatically extract high-level time-series features from heart rate, daily steps, sleep duration, and stress level data.
The extracted features include statistical, temporal, and frequency-based characteristics such as Fourier coefficients and wavelet-based features.
Missing and non-finite values were handled using TSFresh imputation utilities to maintain numerical stability.

####  Step 2: Statistical Feature Computation

In addition to automated features, descriptive statistical features were computed for each user to summarize behavioral patterns:

Mean

Standard Deviation

Skewness

Kurtosis

These statistics provide interpretable summaries of individual physiological and activity-related behavior.
####  Step 3: Feature Selection

Variance thresholding was applied to remove low-variance and non-informative features from the extracted feature set.
This approach was chosen to reduce noise introduced by high-dimensional automated features while retaining behaviorally relevant information for further analysis.

####  Step 4: Temporal Trend Modeling

Facebook Prophet was used to model global temporal and seasonal trends in heart rate, daily steps, sleep duration, and stress level data.
Daily and weekly seasonality patterns observed in the dataset were captured, and forecasts were generated to represent expected population-level behavioral trends over time.

#### Step 5: Deviation and Residual Analysis

Residuals were computed as the difference between observed values and Prophet-generated forecasts.
These residuals were examined to identify deviations from expected behavior, which may indicate unusual or irregular patterns.
Trend plots with confidence intervals and corresponding residual plots were used to support visual interpretation.

#### Step 6: Dimensionality Reduction

Principal Component Analysis (PCA) was applied to project the high-dimensional feature space into two principal components.
This step helped simplify visualization and interpretation while preserving most of the variance present in the original feature set.

#### Step 7: Behavioral Pattern Clustering

Unsupervised clustering techniques were applied to group users based on behavioral similarity:

KMeans clustering was used to identify common behavioral groups

DBSCAN clustering was applied to additionally detect dense clusters and isolate atypical or outlier behavior

Noise points identified by DBSCAN were interpreted as indicators of potentially atypical behavioral patterns.

### 4. Tools Used

Python – Core programming language

Pandas – Data manipulation and aggregation

NumPy – Numerical computations

TSFresh – Automated time-series feature extraction

Facebook Prophet – Temporal trend modeling and forecasting

Scikit-learn – Feature selection, dimensionality reduction, and clustering

Matplotlib & Seaborn – Visualization of trends and behavioral clusters

### 5. Key Insights

Automated time-series feature extraction helped capture behavioral characteristics beyond raw fitness signals.

Statistical features provided clear and interpretable summaries of user behavior.

Prophet was effective in modeling temporal and seasonal trends observed in the dataset.

Residual analysis highlighted periods of unexpected or irregular behavior.

Unsupervised clustering revealed distinct behavioral groups and helped isolate atypical patterns.

PCA improved interpretability by enabling low-dimensional visualization of high-dimensional feature sets.