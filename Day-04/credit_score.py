import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load train and test data
train_file = "train.csv"  # Replace with actual path
test_file = "test.csv"

df_train = pd.read_csv(train_file, low_memory=False)
df_test = pd.read_csv(test_file, low_memory=False)


# Drop unnecessary columns
drop_cols = ["ID", "Customer_ID", "Name", "SSN", "Month", "Type_of_Loan"]
df_train.drop(columns=drop_cols, inplace=True, errors="ignore")
df_test.drop(columns=drop_cols, inplace=True, errors="ignore")

# Handle missing values
df_train.fillna(df_train.median(numeric_only=True), inplace=True)
df_test.fillna(df_test.median(numeric_only=True), inplace=True)

# Encode categorical features
categorical_cols = df_train.select_dtypes(include=["object"]).columns
le = LabelEncoder()

for col in categorical_cols:
    df_train[col] = df_train[col].astype(str)  # Ensure all values are strings
    df_train[col] = le.fit_transform(df_train[col])

    if col in df_test.columns:
        df_test[col] = df_test[col].astype(str)
        df_test[col] = df_test[col].apply(lambda x: x if x in le.classes_ else "UNKNOWN")
        le.classes_ = np.append(le.classes_, "UNKNOWN")
        df_test[col] = le.transform(df_test[col])

# Split features and labels
X = df_train.drop(columns=["Credit_Score"])
y = df_train["Credit_Score"]

# Convert target variable to numerical values
y = LabelEncoder().fit_transform(y)

# Train-test split for validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = xgb.XGBClassifier(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# Evaluate on validation data
y_pred = model.predict(X_val)
print(f"Validation Accuracy: {accuracy_score(y_val, y_pred):.4f}")

# Make predictions on test data
X_test = df_test.drop(columns=["Credit_Score"], errors="ignore")  # Ignore missing column
test_predictions = model.predict(X_test)

# Save predictions
df_test["Predicted_Credit_Score"] = test_predictions
df_test.to_csv("credit_score_predictions.csv", index=False)

print("✅ Predictions saved to 'credit_score_predictions.csv'")
