## 📊 Market Segmentation using Hierarchical Clustering  

### 📌 Overview  
This project demonstrates **market segmentation** by applying **Hierarchical Clustering** to sales data. The dataset includes **quantity sold, revenue, and categorical attributes (region, product, reps)**, which are **encoded and clustered** based on sales patterns. 📈🛍️  

### 🔍 Key Features  
✅ **Hierarchical Clustering with Ward's Method** 🏷️  
✅ **Automated Customer Segmentation** 🏢  
✅ **Data Preprocessing (Standardization & Encoding)** ⚙️  
✅ **Cluster Visualization with Seaborn & Matplotlib** 📊  

### 📂 Project Structure  
```
Market-Segmentation/
│── README.md  # Documentation  
│── clustering.py  # Clustering implementation  
│── store.csv  # Sample dataset  
```  

### 🔧 Technologies Used  
🔹 Python 🐍  
🔹 Pandas 📊  
🔹 Seaborn & Matplotlib 🎨  
🔹 Scipy (Hierarchical Clustering)  

### 📜 How to Run the Project?  
#### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Aishvariyaa/Market-Segmentation.git
cd Market-Segmentation
```  

#### 2️⃣ Install Dependencies  
```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn
```  

#### 3️⃣ Run the Clustering Script  
```bash
python clustering.py
```  

### 📈 Results & Insights  
#### 🔹 **Cluster Summary**  
```
Cluster 1 → Low Volume, Low Revenue  
Cluster 2 → Medium Volume, Medium Revenue  
Cluster 3 → High Volume, High Revenue  
```

| Cluster | Avg. Quantity Sold | Avg. Revenue |
|---------|-------------------|--------------|
| **1**   | 2.17              | 58.04        |
| **2**   | 12.73             | 318.29       |
| **3**   | 21.54             | 618.73       |

#### 📊 **Cluster Visualization**  
The scatter plot below shows **customer segments** based on **sales quantity vs. revenue**:  

![Cluster Visualization](file-8xEJbqvGCSYyTEdrLrvAGs.png)  

### 📌 Next Steps  
🔹 Apply **K-Means & DBSCAN** for comparison 🔄  
🔹 Use **Elbow Method** to determine optimal clusters 📏  
🔹 Incorporate **customer demographics** for deeper insights 🏠  
