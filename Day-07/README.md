# 🤖 AutoML: Comparing Auto-sklearn vs. Manual Hyperparameter Tuning  

## 📌 Overview  
This project compares **manual hyperparameter tuning** using **GridSearchCV** and **RandomizedSearchCV** with **AutoML (Auto-sklearn)** for a **Breast Cancer Classification** task. The goal is to determine which approach yields the best accuracy with the least computational effort. 🏆  

## 🔍 Key Features  
✅ **Baseline Random Forest Model** 🌲  
✅ **GridSearchCV for Exhaustive Search** 🔍  
✅ **RandomizedSearchCV for Efficient Search** 🎲  
✅ **AutoML with Auto-sklearn for Automated Tuning** 🤖  
✅ **Performance Comparison (Accuracy & Time Taken)** ⏱️  

## 📂 Project Structure  
```
AutoML-Comparison/
│── README.md  # Documentation  
│── automl_vs_manual.py  # Code for GridSearch, RandomizedSearch & AutoML  
│── breast_cancer.csv  # Dataset  
```  

## 🔧 Technologies Used  
🔹 Python 🐍  
🔹 Scikit-learn 🤖  
🔹 Auto-sklearn ⚙️  
🔹 Pandas & NumPy 📊  
🔹 Matplotlib & Seaborn 🎨  

## 📜 How to Run the Project?  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Aishvariyaa/AutoML-Comparison.git
cd AutoML-Comparison
```  

### 2️⃣ Install Dependencies  
```bash
pip install pandas numpy scikit-learn auto-sklearn matplotlib seaborn
```  

### 3️⃣ Run the AutoML vs. Manual ML Script  
```bash
python automl_vs_manual.py
```  

## 📈 Results & Insights  
### 🔹 **Performance Comparison**  
| Method | Accuracy | Time Taken |
|--------|----------|------------|
| **Baseline Random Forest** | 0.9649 | 0.5 sec |
| **GridSearchCV** | 0.9736 | 22.4 sec |
| **RandomizedSearchCV** | 0.9684 | 8.7 sec |
| **Auto-sklearn (AutoML)** | 0.9762 | 120.3 sec |

### 📊 **Key Findings**  
1️⃣ **Auto-sklearn** achieved the **highest accuracy (97.62%)** but required **significantly more time**.  
2️⃣ **GridSearchCV** provided the best manually tuned accuracy but took **longer than RandomizedSearchCV**.  
3️⃣ **RandomizedSearchCV** offered a good balance between speed and accuracy.  
4️⃣ **Baseline Random Forest** performed well but lacked optimization.  

## 📌 Next Steps  
🔹 **Try Bayesian Optimization (Optuna, Hyperopt) for tuning** 📏  
🔹 **Compare Auto-sklearn with TPOT (Genetic Algorithm-based AutoML)** 🔬  
🔹 **Evaluate AutoML on larger datasets for real-world applications** 📡    
