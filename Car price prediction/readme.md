# Car Price Prediction

This project aims to predict car prices based on various features using a Linear Regression model.

## Overview

Predicting car prices accurately is essential for both buyers and sellers in the automotive market. This project leverages machine learning techniques to build a predictive model that estimates car prices based on features such as make, model, year, mileage, engine size, fuel type, and transmission.

## Features

- **Load and Preprocess Data**: The dataset `car_prices.csv` is loaded and preprocessed to handle missing values and encode categorical variables.
- **Train Linear Regression Model**: A Linear Regression model is trained using the preprocessed data to predict car prices.
- **Evaluate Model Performance**: The trained model's performance is evaluated using metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
- **Visualize Results**: Data and model results are visualized using Matplotlib and Seaborn to gain insights into the relationships between features and car prices.

## Data

The dataset `car_prices.csv` contains the following columns:

- `make`: The make of the car (e.g., Toyota, Ford).
- `model`: The model of the car (e.g., Camry, Mustang).
- `year`: The manufacturing year of the car.
- `mileage`: The mileage of the car.
- `engine_size`: The size of the car's engine.
- `fuel_type`: The type of fuel the car uses (e.g., petrol, diesel).
- `transmission`: The transmission type of the car (e.g., manual, automatic).
- `price`: The price of the car (target variable).

## Model

The Linear Regression model is chosen for its simplicity and interpretability. The model building process includes:

1. **Data Preprocessing**:
   - Handling missing values.
   - One-hot encoding categorical variables.
   - Splitting the data into training and testing sets.

2. **Training**:
   - Training the Linear Regression model using the training data.

3. **Evaluation**:
   - Evaluating the model's performance using metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

## Results

The model's performance on the test data:

- **Mean Absolute Error (MAE)**: 1.5408119549693085
- **Root Mean Squared Error (RMSE)**: 2.583688081114541

## Usage

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
