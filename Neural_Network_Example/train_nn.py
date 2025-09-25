#!/usr/bin/env python3
"""
Train a Neural Network on F1 Racer Speeds Dataset

This script loads the synthetic f1_speeds.csv dataset and trains a simple
feedforward neural network to predict max_speed based on features.

Requirements: pip install tensorflow numpy pandas matplotlib scikit-learn

Run: python train_nn.py
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('f1_speeds.csv')
print("Dataset shape:", data.shape)
print(data.head())

# Features and target
X = data[['engine_power', 'tire_type', 'weather']].values
y = data['max_speed'].values

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features (important for NN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1)  # Output layer for regression
])

# Compile
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train
history = model.fit(X_train_scaled, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=1)

# Evaluate
loss, mae = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Test Loss: {loss:.4f}, Test MAE: {mae:.4f}")

# Predictions
y_pred = model.predict(X_test_scaled).flatten()

# Metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse:.4f}, R²: {r2:.4f}")

# Plot predictions vs actual
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Max Speed')
plt.ylabel('Predicted Max Speed')
plt.title('Neural Network Predictions on F1 Speeds')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.show()

# Save model (optional)
model.save('f1_nn_model.h5')
print("Model saved as f1_nn_model.h5")

# Example prediction
new_racer = np.array([[1000, 0, 0]])  # 1000 HP, soft tires, dry weather
new_racer_scaled = scaler.transform(new_racer)
predicted_speed = model.predict(new_racer_scaled)[0][0]
print(f"Predicted max speed for new racer: {predicted_speed:.2f} km/h")
