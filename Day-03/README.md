## 🩺 Day 3: Diabetes Prediction using Random Forest  

### 📌 Overview  
Today's challenge was all about **predicting diabetes** using machine learning! 🏥  
I implemented a **Random Forest Classifier** to predict **diabetes** using the **Kaggle Diabetes Dataset**.  

### 🔍 Key Steps  
✅ **Understanding Random Forest:** An ensemble learning method that combines multiple decision trees for better accuracy.  
✅ **Dataset Exploration:** Analyzing the **PIMA Indian Diabetes Dataset** for meaningful insights.  
✅ **Feature Engineering:** Handling missing values, feature scaling, and encoding categorical variables.  
✅ **Model Training:**  
   - Trained a **Random Forest Classifier** on labeled patient data.  
   - Tuned hyperparameters for better model performance.  
✅ **Evaluation Metrics:**  
   - **Accuracy, Precision, Recall, F1-score**  
   - **Confusion Matrix** to analyze model performance.  

### 📂 Project Structure  
```
Day-3-Diabetes-Prediction/
│── README.md  # Documentation  
│── diabetes_prediction.py  # Model Training & Evaluation  
│── diabetes.csv  # Kaggle Diabetes Dataset  
```  

### 📊 Dataset  
For this project, we used the **PIMA Indian Diabetes Dataset**, containing:  

📌 **Features**: Age, BMI, Blood Pressure, Glucose, Insulin, Skin Thickness, etc.  
🎯 **Target Variable**: **Diabetes Diagnosis (0 = Non-Diabetic, 1 = Diabetic)**  

### 🔧 Technologies Used  
🔹 Python  
🔹 Pandas & NumPy (Data Processing)  
🔹 Scikit-learn (Random Forest, Model Evaluation)  
🔹 Matplotlib & Seaborn (Visualization)  

### 📜 How to Run the Project?  
#### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Aishvariyaa/30-Day-AI-Challenge.git
cd 30-Day-AI-Challenge/Day-3
```  

#### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```  

#### 3️⃣ Run the Script  
```bash
python diabetes_prediction.py
```  

### 📈 Model Performance  
📌 **Classification Report & Accuracy**  
```
Model Accuracy: 72%  

Precision | Recall | F1-score  
--------------------------------  
0 (Non-Diabetic) | 0.79   | 0.78  | 0.78  
1 (Diabetic)     | 0.61   | 0.62  | 0.61  
```  
📌 **Key Observations**  
- The **Random Forest model achieved 72% accuracy**.  
- **Class 1 (Diabetic) recall is slightly lower**, meaning the model struggles with detecting some diabetic cases.  
- Improving feature selection and tuning hyperparameters could enhance performance.  

### 📌 Next Steps  
🔹 Implement **Feature Selection** to improve model efficiency.  
🔹 Try **Gradient Boosting (XGBoost, LightGBM)** for better performance.  
🔹 Further optimize hyperparameters for better results.  

### ⭐ Contribute & Connect!  
📢 Follow my **30-day AI journey** & share your thoughts! 🚀  
