
# 🎬 Netflix Title Type Prediction

## 📘 Project Overview
This project focuses on predicting whether a Netflix title is a **Movie** or a **TV Show** based on its metadata such as country, rating, duration, and other descriptive features.  
It demonstrates end-to-end **data cleaning, feature engineering, and machine learning model training** using Python.

---

## 📂 Dataset Description
The dataset used is **`netflix_titles.csv`**, which contains details of Netflix titles such as:
| Column Name | Description |
|--------------|-------------|
| `show_id` | Unique ID for each show |
| `type` | Target variable — *Movie (0)* or *TV Show (1)* |
| `title` | Name of the title |
| `director` | Name of the director |
| `cast` | Main actors involved |
| `country` | Country where the show was produced |
| `date_added` | Date when added to Netflix |
| `release_year` | Year of release |
| `rating` | Age rating (e.g., TV-MA, PG-13) |
| `duration` | Duration (minutes or seasons) |
| `listed_in` | Genre categories |
| `description` | Short summary of the show/movie |

---

## 🧹 Data Preprocessing Steps
1. **Handle Missing Values**
   - Filled missing values in `director` and `cast` with `'Unknown'`.
   - Inferred missing countries using keywords in the `listed_in` column.
   - Dropped rows with missing `rating` or `date_added`.

2. **Feature Cleaning**
   - Extracted **year** from `date_added`.
   - Cleaned and standardized `duration` (minutes vs seasons).
   - Replaced incorrect `rating` entries (e.g., `'74 min'` → `NaN`).

3. **Encoding**
   - Label encoded categorical columns (`type`, `listed_in`, `description`).
   - Optionally applied **One-Hot Encoding** to categorical genres.

---

## 📊 Exploratory Data Analysis
- Checked **data distribution** and **null values**.
- Used **boxplots** and **histograms** to visualize numerical feature distributions.
- Verified **normality** of numeric features using skewness plots.

---

## 🤖 Machine Learning Models
Trained multiple models to predict the `type` of Netflix title:

| Model | Accuracy |
|--------|-----------|
| Logistic Regression | 1.000 |
| Decision Tree | 1.000 |
| Random Forest | 1.000 |
| Gradient Boosting | 1.000 |

> ⚠️ *All models achieved perfect accuracy — possible due to simple dataset or target leakage.*

---

## 🧪 MLflow Integration
Used **MLflow** to track:
- Model parameters  
- Accuracy metrics  
- Saved and versioned trained models  

> **Warnings (safe to ignore)**  
> - `artifact_path` deprecated → use `name` instead.  
> - Missing model signature → add `input_example` for schema inference.

---

## 🧩 Next Steps
- Add more feature engineering to reduce target leakage.  
- Experiment with text processing on `description`.  
- Deploy the model using MLflow or Streamlit for interactive predictions.

---

## 🛠️ Technologies Used
- Python 🐍  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- MLflow  

---

## 📈 Expected Output
- Cleaned dataset ready for ML  
- Model accuracy and confusion matrices  
- MLflow tracking dashboard with all logged experiments  

---

## 🏁 Conclusion
This notebook successfully demonstrates a full **ML pipeline** for classifying Netflix titles using structured data.  
It can serve as a strong foundation for deeper **content recommendation** or **genre prediction** systems.

---
