# FitPulse Health Anomaly Detection – Milestone 2
## Feature Extraction, Trend Modeling, and Behavioral Pattern Analysis

### 1. Objective

The primary objective of this milestone is to extract meaningful statistical and time-series features from the preprocessed fitness dataset generated in Milestone 1. This milestone also focuses on modeling temporal trends and identifying behavioral patterns using unsupervised learning techniques. These steps establish the analytical groundwork required for detecting anomalies in subsequent project phases.

### 2. Dataset Description

This milestone uses the cleaned and consolidated dataset produced in Milestone 1, which contains timestamped fitness measurements collected from wearable devices.

Metrics Analyzed:

Heart Rate

Daily Step Count

Sleep Duration

Stress Level

### Data Characteristics:

Timestamped observations across multiple users

Limited per-user temporal depth

Combination of physiological signals and activity-related data

### 3. Steps Performed
#### Step 1: Automated Time-Series Feature Extraction

Applied TSFresh to automatically extract time-series features from heart rate, daily steps, sleep duration, and stress level data.

Extracted features include statistical, temporal, and frequency-based characteristics such as Fourier coefficients and wavelet transforms.

Handled missing and non-finite values using TSFresh imputation utilities.

####  Step 2: Statistical Feature Computation

Computed descriptive statistical features for each user to summarize behavioral patterns:

Mean

Standard Deviation

Skewness

Kurtosis

These features provide an interpretable summary of physiological and activity-related behavior.

####  Step 3: Feature Selection

Applied variance thresholding to remove low-variance and non-informative features from the extracted feature set.

Reduced feature dimensionality while preserving relevant behavioral information for downstream analysis.

####  Step 4: Temporal Trend Modeling

Applied Facebook Prophet to model temporal and seasonal trends in heart rate, steps, and sleep duration data.

Captured daily and weekly seasonality present in the dataset.

Generated forecasts representing expected behavioral patterns over time.

#### Step 5: Deviation and Residual Analysis

Computed residuals as the difference between observed values and Prophet-generated forecasts.

Used residuals to identify deviations from expected behavior, serving as indicators of unusual or abnormal patterns.

Visualized trends with confidence intervals and corresponding residual plots.

#### Step 6: Dimensionality Reduction

Applied Principal Component Analysis to project the high-dimensional feature space into two principal components.

Enabled effective visualization and interpretation of behavioral patterns.

#### Step 7: Behavioral Pattern Clustering

Applied unsupervised clustering techniques to group users based on behavioral similarity:

KMeans clustering to identify common behavioral groups

DBSCAN clustering to detect dense clusters and isolate atypical or anomalous behavior

Interpreted DBSCAN noise points as indicators of atypical behavior.

#### 4. Tools Used

Python: Core programming language

Pandas: Data manipulation and aggregation

NumPy: Numerical computations

TSFresh: Automated time-series feature extraction

Facebook Prophet: Temporal trend modeling and forecasting

Scikit-learn: Feature selection, dimensionality reduction, and clustering

Matplotlib and Seaborn: Visualization of trends and clusters

#### 5. Key Insights

Automated time-series feature extraction captures complex behavioral characteristics beyond raw fitness signals.

Statistical features provide clear and interpretable summaries of user behavior.

Prophet effectively models temporal and seasonal trends, enabling deviation-based analysis.

Residual analysis highlights periods of unexpected or abnormal behavior.

Unsupervised clustering reveals distinct behavioral groups and isolates atypical patterns.

PCA improves interpretability by enabling low-dimensional visualization of high-dimensional feature sets.