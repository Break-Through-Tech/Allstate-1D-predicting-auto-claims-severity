# Auto Claims Severity - Gate 2: EDA & Feature Engineering

## Overview

This repository contains the artifacts for Gate 2 of the Auto Claims Severity prediction project. This phase focuses on Exploratory Data Analysis (EDA), establishing a performance baseline, and conducting initial feature engineering to prepare the claims data for predictive modeling.

## Key Methodologies

### 1. Target Variable Transformation

* **Challenge:** The raw `loss` target variable exhibits severe right-skewness, which is typical for insurance claims but detrimental to standard regression algorithms.
* **Solution:** We applied a `log1p(Loss)` transformation to the target variable. This compresses the long right tail, creating a roughly normal distribution that stabilizes model training and prevents extreme outliers from dominating the gradient.
* **Evaluation:** Model predictions made in the log space will be converted back to dollar amounts using the inverse `expm1()` function before evaluating the Mean Absolute Error (MAE).

### 2. Feature Engineering: Categorical Consolidation

* **Challenge:** The dataset contains highly cardinal categorical features (e.g., `cat112`), with many categories representing less than 1% of the total claims. Leaving these raw leads to a high risk of model overfitting.
* **Solution:** Implemented a grouping threshold. Any categorical value appearing in less than 1% of the total dataset was rolled up into a consolidated `"Other"` category.

### 3. Baseline Establishment

* **Metric:** Mean Absolute Error (MAE).
* **Baseline Strategy:** We calculated a naive baseline MAE by predicting the **median** claim loss for all observations. This serves as the primary benchmark that our future machine learning models must outperform.

## Artifacts Included in this Submission

* **EDA Notebooks:** Google Colab notebooks containing the data exploration, distribution plotting, and feature analysis (outputs cleared for version control).
* **Visualizations:** Visual proof of the methodologies, including:
  * Distribution comparisons of Raw Loss vs. `log1p(Loss)`.
  * Box plots and frequency charts demonstrating the successful grouping of rare categorical variables (e.g., `cat112`).
* **Baseline Calculations:** Script establishing the median-based baseline MAE.

## Team Collaboration

Code is developed in Google Colab and version-controlled via this GitHub repository. All feature branches must be reviewed prior to merging into the main branch.