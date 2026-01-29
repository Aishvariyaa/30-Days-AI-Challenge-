import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset 
file_path = "emp_attrition.csv"  

try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Make sure it's in the correct path.")
    exit()

# Print the first few rows for inspectio
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Print column names to debug missing 'Attrition' error
print("\nColumn names in the dataset:")
print(df.columns)

df.columns = df.columns.str.strip()

# Check if 'Attrition' column exists
if 'Attrition' not in df.columns:
    print("\nError: 'Attrition' column not found in the dataset. Please check the column names.")
    exit()

# Convert 'Attrition' column to binary values 
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# Drop unnecessary columns like EmployeeID if present
if 'EmployeeID' in df.columns:
    df.drop(columns=['EmployeeID'], inplace=True)

# Convert categorical variables to numerical (One-Hot Encoding)
df = pd.get_dummies(df, drop_first=True)

# Define features (X) and target (y)
y = df['Attrition']
X = df.drop(columns=['Attrition'])

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)

# Model Evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix Visualization
plt.figure(figsize=(5, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

