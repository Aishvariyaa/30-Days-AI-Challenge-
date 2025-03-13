## 🎬 Day 2: Movie Recommendation System using Collaborative Filtering  

### 📌 Overview  
Diving deeper into **Collaborative Filtering**, a powerful technique used in recommendation systems! 🎥🎞️  
The goal is to **recommend movies** based on user interactions and preferences.  

### 🔍 Key Steps  
✅ **Understanding Collaborative Filtering:** Leveraging user interactions for recommendations.  
✅ **Types of Collaborative Filtering:**  
   - **User-Based Filtering**: Finds similar users and recommends movies they liked.  
   - **Item-Based Filtering**: Recommends similar movies based on item similarity.  
✅ **Dataset Exploration:** Analyzing movie ratings data for meaningful insights.  
✅ **Implementing Similarity Metrics:**  
   - **Pearson Correlation**  
   - **Cosine Similarity**  
✅ **Challenges & Next Steps:**  
   - Handling **sparse data** to improve recommendations.  
   - Enhancing **personalization** by incorporating hybrid approaches.  

### 📂 Project Structure  
```
Day-2-Movie-Recommendation/
│── README.md  # Documentation  
│── movie_recommendation.py  # Standalone script  
│── movies.csv # (from kaggle)
│── ratings.csv # (from kaggle)  
```

### 📊 Dataset  
For this project, we use a **Movie Ratings Dataset**, containing:  

📌 **Features**: User ID, Movie ID, Rating, Timestamp  
🎯 **Target Variable**: Predicted Movie Ratings  

### 🔧 Technologies Used  
🔹 Python  
🔹 NumPy & Pandas (Data Manipulation)  
🔹 Scikit-learn (Model Building & Evaluation)  
🔹 Surprise Library (Collaborative Filtering)  
🔹 Matplotlib & Seaborn (Visualization)  

### 📜 How to Run the Project?  
#### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Aishvariyaa/30-Day-AI-Challenge.git
cd 30-Day-AI-Challenge/Day-02
```

#### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

#### 3️⃣ Run the Script  
```bash
python movie_recommendation.py
```

### 📈 Model Performance  
📌 **Sample Recommendations**  
```json
{
  "recommendations": [
    { "movieId": 527, "title": "Schindler's List (1993)" },
    { "movieId": 3469, "title": "Inherit the Wind (1960)" },
    { "movieId": 77177, "title": "Wild China (2008)" },
    { "movieId": 103319, "title": "Jim Gaffigan: Mr. Universe (2012)" },
    { "movieId": 105250, "title": "Century of the Self, The (2002)" }
  ]
}
```
📌 **Key Observations**  
- Item-based filtering **outperformed** user-based filtering for sparse datasets.  
- Feature engineering & similarity metrics **significantly impact** recommendations.  

### 📌 Next Steps  
🔹 Implement **Hybrid Recommendation** (Collaborative + Content-Based).  
🔹 Experiment with **Deep Learning models (AutoEncoders, Neural CF)**.  
🔹 Optimize hyperparameters using **GridSearchCV**.  

### ⭐ Contribute & Connect!  
📢 Follow my **30-day AI journey** & share your thoughts! 🚀  
