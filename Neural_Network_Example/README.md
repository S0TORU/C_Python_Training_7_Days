# Neural Network Example: Predicting F1 Racer Speeds

This directory provides a hands-on example of training a neural network on a synthetic dataset of F1 racer speeds. It's an extension of Bonus Day 8, demonstrating how to apply AI/ML concepts to a fun, real-world-inspired problem.

## Dataset: f1_speeds.csv
- **Features**:
  - `engine_power`: Engine horsepower (800-1100)
  - `tire_type`: 0=soft, 1=medium, 2=hard
  - `weather`: 0=dry, 1=wet
- **Target**: `max_speed` (km/h)
- **Samples**: 1000 synthetic entries
- **Generation**: Created using `generate_csv.py` (in repo root) with realistic correlations (e.g., more power = faster speeds, wet weather slows down).

## Script: train_nn.py
Trains a simple feedforward neural network using TensorFlow/Keras.

### Steps:
1. Load and preprocess data (scaling features).
2. Build a 3-layer NN (64, 32, 1 neurons).
3. Train on 80% of data, validate on 20%.
4. Evaluate with MSE, MAE, R².
5. Visualize predictions.
6. Save model and make example prediction.

### Requirements:
- Python 3
- TensorFlow: `pip install tensorflow`
- NumPy, Pandas, Matplotlib, Scikit-learn

### Run:
```bash
cd Neural_Network_Example
python train_nn.py
```

## Why This Example?
- **Fun Theme**: F1 racing makes ML engaging.
- **Regression Task**: Predict continuous values (speeds).
- **End-to-End**: From data to predictions.
- **Extensible**: Add features, try different architectures, or use real F1 data.

## Exercises:
1. Experiment with network layers/sizes.
2. Add dropout for regularization.
3. Compare with Scikit-learn's LinearRegression.
4. Visualize training history (loss curves).

This example bridges your programming skills with AI—keep experimenting! 🚗💨🤖
