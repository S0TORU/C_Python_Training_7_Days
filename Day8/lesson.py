#!/usr/bin/env python3
"""
Bonus Day 8: AI/ML Engineering Fundamentals
Lesson: Simple Linear Regression Example

This script demonstrates building a basic ML model to predict house prices
using the Boston Housing dataset (or a synthetic one for simplicity).

Prerequisites:
- pip install numpy pandas matplotlib scikit-learn

Run: python lesson.py
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# For this example, we'll create a synthetic dataset
# In real ML, you'd load from CSV: data = pd.read_csv('data.csv')
np.random.seed(42)  # For reproducibility
n_samples = 100
# Features: size (sq ft), rooms
X = np.random.rand(n_samples, 2) * [3000, 5] + [500, 1]  # Realistic ranges
# Target: price (in thousands)
y = X[:, 0] * 0.1 + X[:, 1] * 50 + np.random.randn(n_samples) * 10  # Linear relationship + noise

# Create DataFrame for easier handling
data = pd.DataFrame(X, columns=['size_sqft', 'rooms'])
data['price_k'] = y

print("Sample Data:")
print(data.head())
print("\nData Info:")
print(data.describe())

# Step 1: Preprocess (minimal here; in real ML, handle missing values, scaling, etc.)
# Assume data is clean

# Step 2: Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nTrain set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")

# Step 3: Train the model
model = LinearRegression()
model.fit(X_train, y_train)
print(f"\nModel Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")

# Step 4: Make predictions
y_pred = model.predict(X_test)

# Step 5: Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\nMean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")  # Closer to 1 is better

# Step 6: Visualize
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted House Prices')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # Perfect prediction line
plt.show()  # In a script, this may not display; run in Jupyter or save fig

# Bonus: Predict for a new house
new_house = np.array([[2000, 3]])  # 2000 sq ft, 3 rooms
predicted_price = model.predict(new_house)
print(f"\nPredicted price for 2000 sq ft, 3 rooms: ${predicted_price[0]*1000:.2f}")

# Exercises:
# 1. Change test_size to 0.3 and see how metrics change.
# 2. Add more features or noise to y.
# 3. Try a different model from sklearn, like RandomForestRegressor.
