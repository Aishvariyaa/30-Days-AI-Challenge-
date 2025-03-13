## 🚀 Day 1: Predicting Employee Attrition using Logistic Regression  

### 📌 Overview  
Today, I explored **Logistic Regression** to predict **employee attrition** using **machine learning**! 📊  
The goal is to analyze factors influencing employee turnover and optimize the model with **feature selection and hyperparameter tuning**.  

### 🔍 Key Steps  
✅ **Data Preprocessing:** One-Hot Encoding, Feature Scaling  
✅ **Model Training:** Logistic Regression  
✅ **Evaluation:** Achieved **78% accuracy**  
✅ **Insights:**  
- **Precision & Recall** show a balanced classification performance.  
- **Confusion Matrix** reveals misclassifications that can be improved.  

### 📂 Project Structure  
```
Day-1-Employee-Attrition/
│── README.md  # Documentation  
│── employee_attrition.py  # Standalone script  
│── emp_attrition.csv  # (from kaggle)  
```

### 📊 Dataset  
For this project, we use a dataset containing:  

📌 **Features**: Employee Age, Department, Salary, Work-Life Balance, Job Satisfaction, etc.  
🎯 **Target Variable**: Attrition (Yes/No)  

### 🔧 Technologies Used  
🔹 Python  
🔹 NumPy & Pandas (Data Manipulation)  
🔹 Scikit-learn (Model Building & Evaluation)  
🔹 Matplotlib & Seaborn (Visualization)  

### 📜 How to Run the Project?  
#### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Aishvariyaa/30-Day-AI-Challenge.git
cd 30-Day-AI-Challenge/Day-01
```

#### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

#### 3️⃣ Run the Script  
```bash
python employee_attrition.py
```

### 📈 Model Performance  
📌 **Classification Report**  
- **Accuracy:** **78%**  
- **Precision:** **0.77 - 0.78**  
- **Recall:** **0.71 - 0.83**  
- **F1-Score:** **0.74 - 0.80**  

📌 **Key Observations**  
- Work-Life Balance & Job Satisfaction are **strong predictors** of attrition.  
- Feature selection & scaling **significantly improved** model performance.  
- Hyperparameter tuning helped improve accuracy.  

### 📌 Next Steps  
🔹 Experiment with additional features like commute time & team culture.  
🔹 Apply **Random Forest or XGBoost** for better performance.  
🔹 Implement **SHAP values** for feature importance analysis.  

### ⭐ Contribute & Connect!  
📢 Follow my **30-day AI journey** & share your thoughts! 🚀  
