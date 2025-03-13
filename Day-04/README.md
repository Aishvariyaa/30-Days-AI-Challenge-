## 💳 Day 4: Credit Score Prediction using XGBoost  

### 📌 Overview  
Today's challenge was focused on **predicting credit scores** using **XGBoost**! 🏦  
Credit scoring is essential in the financial industry, and **machine learning models** can optimize risk assessment for better lending decisions.  

### 🔍 Key Steps  
✅ **Understanding XGBoost:** A powerful **gradient boosting** algorithm for classification.  
✅ **Dataset Preprocessing:**  
   - Handling **missing values** with median imputation.  
   - Encoding **categorical features** for model compatibility.  
✅ **Model Training:**  
   - **Trained XGBoost Classifier** on labeled data.  
   - Tuned **hyperparameters** to improve accuracy.  
✅ **Evaluation Metrics:**  
   - **Accuracy, Precision, Recall, F1-score**  
   - **Confusion Matrix** to assess model performance.  

### 📂 Project Structure  
```
Day-4-Credit-Score-Prediction/
│── README.md  # Documentation  
│── credit_score.py  # Model Training & Evaluation  
│── test.csv  # Kaggle Credit Score Dataset  
│── credit_score_predictions.csv  # Model Predictions  
```

### 🔗 Dataset Link  
📌 **Kaggle Dataset:** [Credit Score Prediction Dataset](https://www.kaggle.com/datasets/abhishekhere/credit-score)   

### 📊 Dataset  
For this project, we use a **credit score dataset** containing:  

📌 **Features**: Loan History, Payment Behavior, Credit Mix, Outstanding Debt, etc.  
🎯 **Target Variable**: **Credit Score Category (Low, Medium, High)**  

### 🔧 Technologies Used  
🔹 Python  
🔹 Pandas & NumPy (Data Processing)  
🔹 XGBoost (Gradient Boosting Model)  
🔹 Scikit-learn (Model Evaluation)  

### 📜 How to Run the Project?  
#### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Aishvariyaa/30-Day-AI-Challenge.git
cd 30-Day-AI-Challenge/Day-04
```

#### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

#### 3️⃣ Download Dataset  
📌 Download the dataset from [Kaggle](https://www.kaggle.com/datasets/abhishekhere/credit-score)  and place it in the project folder.  

#### 4️⃣ Run the Script  
```bash
python credit_score.py
```

### 📈 Model Performance  
📌 **Validation Accuracy: 70.9%**  

📌 **Classification Report**  
```
Precision | Recall | F1-score  
--------------------------------  
0 (Low)   | 0.72   | 0.75  | 0.73  
1 (Medium)| 0.70   | 0.68  | 0.69  
2 (High)  | 0.69   | 0.66  | 0.67  
```
📌 **Key Observations**  
- The **XGBoost model performed well**, achieving **70.9% accuracy**.  
- **Recall is slightly lower** for high credit score cases, indicating possible improvements.  
- Feature selection & boosting techniques could further optimize results.  

### 📌 Next Steps  
🔹 Implement **Feature Selection** to improve model efficiency.  
🔹 Try **other ensemble models** for better performance.  
🔹 Tune **hyperparameters** using advanced optimization techniques.  

### ⭐ Contribute & Connect!  
📢 Follow my **30-day AI journey** & share your thoughts! 🚀  
