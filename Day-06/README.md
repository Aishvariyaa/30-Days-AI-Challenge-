# 🚴‍♂️ Predicting Bike Rentals using Support Vector Regression (SVR)  

## 📌 Overview  
This project applies **Support Vector Regression (SVR)** to predict daily bike rentals based on weather and environmental conditions. SVR is a powerful regression model that maps input features into a high-dimensional space to minimize prediction error.  

## 🔍 Key Features  
✅ **Support Vector Regression (RBF Kernel)** 📈  
✅ **Feature Scaling using StandardScaler** ⚙️  
✅ **Model Performance Evaluation (MSE, R² Score)** 📊  
✅ **Actual vs Predicted Bike Rentals Visualization** 🎨  

## 📂 Project Structure  
```
Bike-Rental-Prediction/
│── README.md  # Documentation  
│── bike_rental_svr.py  # SVR implementation  
│── bike_rental.csv  # Dataset  
```  

## 🔧 Technologies Used  
🔹 Python 🐍  
🔹 Scikit-learn 🤖  
🔹 Pandas & NumPy 📊  
🔹 Matplotlib & Seaborn 🎨  

## 📜 How to Run the Project?  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Aishvariyaa/Bike-Rental-Prediction.git
cd Bike-Rental-Prediction
```  

### 2️⃣ Install Dependencies  
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```  

### 3️⃣ Run the SVR Model  
```bash
python bike_rental_svr.py
```  

## 📈 Results & Insights  
### 🔹 **Model Performance Metrics**  
```
Mean Squared Error (MSE): 1,941,285.47  
R-squared Score (R²): 0.52  
```

| Metric | Value |
|--------|------:|
| **MSE** | 1,941,285.47 |
| **R² Score** | 0.52 |

### 📊 **Actual vs Predicted Bike Rentals**  
The scatter plot below shows the relationship between **actual and predicted bike rentals**:  

![SVR Bike Rental Predictions](file-M7vaW2tZzVoRzLKwxKwNMx.png)  

## 📌 Next Steps  
🔹 Tune **C, epsilon, and gamma** to improve performance ⚡  
🔹 Compare SVR with **Random Forest & XGBoost** 🌲  
🔹 Include **time-based features (seasonality effects)** for better predictions 🕒  
