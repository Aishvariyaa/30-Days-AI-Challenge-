import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

# Load datasets 
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Check data
print("Data loaded successfully!")
print(day_df.head())

# Selecting features and target variable
features = ['temp', 'hum', 'windspeed', 'weathersit']
target = 'cnt'  # Total bike rentals

X = day_df[features]  # Feature variables
y = day_df[target]    # Target variable

# Splitting the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizing the features (important for SVR)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Support Vector Regressor (SVR)
svr = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1)
svr.fit(X_train_scaled, y_train)

# Predict on test data
y_pred = svr.predict(X_test_scaled)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f" Model Trained Successfully!")
print(f" Mean Squared Error (MSE): {mse:.2f}")
print(f" R-squared Score (R²): {r2:.2f}")

# Plot predictions vs actual values
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
plt.xlabel("Actual Bike Rentals")
plt.ylabel("Predicted Bike Rentals")
plt.title("Actual vs Predicted Bike Rentals (SVR Model)")
plt.show()
