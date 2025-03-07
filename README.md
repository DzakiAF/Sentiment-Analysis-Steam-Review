# Sentiment Analysis Steam Review

## 📌 Project Overview
Sentiment Analysis Steam Review is a project aimed at classifying game reviews on the Steam platform into **positive** or **negative** sentiments using **Natural Language Processing (NLP)** and **Machine Learning** techniques.

## 📂 Dataset
- **Source**: [Kaggle - Top 10 Steam Games Dataset](https://www.kaggle.com/datasets/muhammadiqbalmukati/top10-steam-games-dataset?select=Train.csv)  
- **Description**: The dataset contains reviews of Steam games along with sentiment labels.
- **Main Features**:
  - `review_text`: User review text.
  - `sentiment`: Sentiment label (0 = negative, 1 = positive).

## 🔧 Tech Stack
- **Python**
- **Pandas & NumPy** (Data Processing)
- **NLTK & SpaCy** (Text Preprocessing)
- **Scikit-learn** (Machine Learning)
- **TensorFlow/Keras** (Deep Learning, if used)
- **Matplotlib & Seaborn** (Visualization)

## 📌 Workflow
1. **Data Preprocessing**
   - Tokenization
   - Stopword Removal
   - Lemmatization
   - Vectorization (TF-IDF/Word2Vec)
2. **Model Training & Evaluation**
   - Algorithms used: `Logistic Regression`, `Random Forest`, `XGBoost`, `Neural Networks`
   - Evaluation Metrics: Accuracy, Precision, Recall, F1-Score
3. **Deployment (Optional)**
   - API using Flask/FastAPI (if deployment is required)

## 📊 Results
Best model evaluation results:
- **Accuracy**: 85%
- **F1-Score**: 0.85
- **Best Model**: Artificial Neural Networks (ANN)

## 🤝 Contribution
If you would like to contribute, please **fork** this repository and submit a **pull request** with your proposed changes!

---
✨ **Created by DzakiAF**

