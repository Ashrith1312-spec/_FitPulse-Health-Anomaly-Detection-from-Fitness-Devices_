FitPulse Health Anomaly Detection – Milestone 2
Feature Extraction, Trend Modeling, and Behavioral Clustering
1. Objective

The primary objective of this milestone is to derive meaningful insights from the preprocessed fitness dataset created in Milestone 1. This is achieved by extracting statistical and time-series features, modeling temporal trends, and identifying behavioral patterns using unsupervised learning techniques. The outcomes of this milestone establish the analytical foundation required for anomaly detection in subsequent phases of the project.

2. Dataset Description

This milestone operates on the cleaned and consolidated dataset generated in Milestone 1. The dataset contains timestamped fitness measurements aggregated at a consistent temporal resolution.

Key Metrics Analyzed:

Heart rate

Daily step count

Sleep duration

Stress level

Data Characteristics:

Each record represents a user observation with an associated timestamp

Limited per-user temporal depth, requiring global trend modeling

Includes both physiological signals and activity-related attributes

3. Steps Performed
Step 1: Feature Extraction Using TSFresh

Applied TSFresh to automatically extract time-series features from heart rate, steps, sleep duration, and stress level data.

Extracted features include temporal, statistical, and frequency-based characteristics such as Fourier coefficients and wavelet transforms.

Missing and non-finite feature values were handled using TSFresh’s imputation utilities.

Step 2: Statistical Feature Computation

Computed statistical features for each user to summarize behavioral patterns:

Mean

Standard Deviation

Skewness

Kurtosis

These features provide a compact representation of physiological and activity-related behavior.

Step 3: Feature Selection

Applied variance thresholding to remove low-variance and non-informative features.

Reduced the dimensionality of the extracted feature set while preserving relevant behavioral signals.

Step 4: Trend Modeling with Facebook Prophet

Applied Facebook Prophet to model temporal and seasonal trends in the fitness data.

Modeled daily and weekly seasonality for heart rate, steps, and sleep duration.

Forecasted expected values for each metric over time.

Step 5: Residual and Deviation Analysis

Computed residuals as the difference between observed values and Prophet forecasts.

Residuals represent deviations from expected behavior and serve as indicators of unusual or abnormal patterns.

Generated visualizations of trends with confidence intervals and residual plots to support interpretability.

Step 6: Dimensionality Reduction

Applied Principal Component Analysis to reduce the high-dimensional feature space into two components.

Enabled efficient visualization and clustering of user behavior patterns.

Step 7: Behavioral Pattern Clustering

Applied unsupervised clustering techniques to identify behavioral groups:

KMeans clustering to group users with similar fitness behavior

DBSCAN clustering to identify dense clusters and detect atypical or anomalous users

DBSCAN noise points were interpreted as atypical behavioral patterns.

4. Tools Used

Python: Core programming language

Pandas: Data manipulation and aggregation

NumPy: Numerical computations

TSFresh: Automated time-series feature extraction

Facebook Prophet: Trend modeling and forecasting

Scikit-learn: Feature selection, PCA, and clustering

Matplotlib and Seaborn: Visualization of trends and clusters

5. Key Insights

Automated time-series feature extraction captures complex behavioral patterns that are not easily represented by raw signals.

Statistical features provide an interpretable summary of user fitness behavior.

Prophet effectively models seasonal and temporal trends, enabling deviation-based analysis.

Residual analysis highlights periods of abnormal or unexpected behavior.

Unsupervised clustering reveals distinct behavioral groups and isolates atypical patterns.

PCA significantly improves interpretability by enabling low-dimensional visualization of high-dimensional data.