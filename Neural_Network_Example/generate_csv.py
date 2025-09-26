#!/usr/bin/env python3
"""
Generate synthetic F1 racer speeds dataset.

Features: engine_power (HP), tire_type (0=soft, 1=medium, 2=hard), weather (0=dry, 1=wet)
Target: max_speed (km/h)

This script creates f1_speeds.csv with 1000 samples.
"""

import numpy as np
import pandas as pd

np.random.seed(42)  # For reproducibility

n_samples = 1000

# Features
engine_power = np.random.randint(800, 1100, n_samples)  # HP
tire_type = np.random.randint(0, 3, n_samples)  # 0,1,2
weather = np.random.randint(0, 2, n_samples)  # 0=dry, 1=wet

# Target: max_speed influenced by features
# Base speed + adjustments
base_speed = 300
speed_adj = (engine_power - 800) * 0.1  # More power = faster
tire_adj = np.where(tire_type == 0, 10, np.where(tire_type == 1, 5, 0))  # Soft tires faster
weather_adj = weather * -20  # Wet = slower

max_speed = base_speed + speed_adj + tire_adj + weather_adj + np.random.randn(n_samples) * 5  # Add noise

# Create DataFrame
data = pd.DataFrame({
    'engine_power': engine_power,
    'tire_type': tire_type,
    'weather': weather,
    'max_speed': max_speed
})

# Save to CSV
data.to_csv('Neural_Network_Example/f1_speeds.csv', index=False)

print("Generated f1_speeds.csv with", n_samples, "samples.")
print(data.head())
