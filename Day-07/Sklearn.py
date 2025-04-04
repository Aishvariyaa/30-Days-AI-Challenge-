import numpy as np
import time
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_breast_cancer

# Load dataset
data = load_breast_cancer()
X, y = data.data, data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Baseline model
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
baseline_acc = accuracy_score(y_test, rf.predict(X_test))
print(f"Baseline Random Forest Accuracy: {baseline_acc:.4f}")

### 1️⃣ GridSearchCV ###
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10]
}

start_time = time.time()
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)
grid_time = time.time() - start_time

best_grid_acc = accuracy_score(y_test, grid_search.best_estimator_.predict(X_test))
print(f"GridSearchCV Best Accuracy: {best_grid_acc:.4f} | Time Taken: {grid_time:.2f} sec")
print(f"Best GridSearchCV Params: {grid_search.best_params_}")

### 2️⃣ RandomizedSearchCV ###
param_dist = {
    'n_estimators': np.arange(50, 200, 10),
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10]
}

start_time = time.time()
random_search = RandomizedSearchCV(RandomForestClassifier(random_state=42), param_dist, cv=5, n_iter=10, scoring='accuracy', n_jobs=-1, random_state=42)
random_search.fit(X_train, y_train)
random_time = time.time() - start_time

best_random_acc = accuracy_score(y_test, random_search.best_estimator_.predict(X_test))
print(f"RandomizedSearchCV Best Accuracy: {best_random_acc:.4f} | Time Taken: {random_time:.2f} sec")
print(f"Best RandomizedSearchCV Params: {random_search.best_params_}")

# Compare results
print("\nComparison:")
print(f"Baseline Model -> Accuracy: {baseline_acc:.4f}")
print(f"GridSearchCV -> Accuracy: {best_grid_acc:.4f}, Time: {grid_time:.2f} sec")
print(f"RandomizedSearchCV -> Accuracy: {best_random_acc:.4f}, Time: {random_time:.2f} sec")
