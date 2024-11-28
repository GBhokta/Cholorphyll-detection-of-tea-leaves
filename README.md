

This project presents a novel, cost-effective approach to predict the chlorophyll content of tea leaves using smartphone images. Traditional methods such as SPAD meters and spectrophotometers are costly and inaccessible to many small-scale farmers. This repository showcases the development and evaluation of machine learning models for chlorophyll estimation.

## Features
- **Low-cost Implementation**: Utilizes smartphone images combined with light features for chlorophyll measurement.
- **Machine Learning Models**:
  - Multiple Linear Regression (MLR)
  - Support Vector Regression (SVR)
  - Artificial Neural Networks (ANN)
- **Data Collection**: Contact imaging of tea leaves, using features like RGB intensity, variance, kurtosis, and skewness for predictive modeling.

## Datasets
The dataset contains 1364 rows and 10 columns, including features such as:
- `mean_r`, `mean_g`, `mean_b`
- `stddev_r`, `stddev_g`, `stddev_b`
- `variance`, `kurtosis`, `skewness`
- `Chlorophyll value` (target variable)

The dataset was prepared using images of mature tea leaves from Kokrajhar Tea Estate, with SPAD-calculated chlorophyll values as the reference.

## Methods
1. **Multiple Linear Regression**:
   - Models the linear relationship between features and the target variable.
   - Evaluation Metrics: MAE, MSE, RMSE, R².

2. **Support Vector Regression**:
   - Employs the RBF kernel for non-linear regression.
   - Evaluation Metrics: MAE, MSE, RMSE, R².

3. **Artificial Neural Networks**:
   - Designed with 4 dense layers (128, 64, 32, 1) using ELU activation functions.
   - Optimized for higher predictive accuracy.

## Results
| Model   | MAE   | MSE    | RMSE   | R²     |
|---------|-------|--------|--------|--------|
| MLR     | 3.591 | 23.533 | 4.851  | 0.711  |
| SVR     | 5.274 | 55.904 | 7.476  | 0.314  |
| ANN     | 4.443 | 23.533 | 4.851  | 0.711  |



## Applications
- Provides farmers and researchers with an affordable tool for monitoring plant health.
- Enhances precision agriculture by replacing expensive lab-based chlorophyll tests.

## Advantages
- Cost-effective and scalable solution for small-scale farmers.
- High reliability using AI-driven models for prediction.

## Limitations
- Requires high-quality images for optimal results.
- Accuracy may vary based on lighting conditions and feature extraction.

## Acknowledgments
Special thanks to Girijananda Chowdhury Institute of Management and Technology for their guidance and support.

---
