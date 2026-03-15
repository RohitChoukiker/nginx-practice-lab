# Titanic Survival Prediction — ML Model Comparison

## Project Overview

This project builds a Machine Learning pipeline to predict whether a passenger survived the Titanic disaster.

Dataset used:
Titanic Machine Learning from Disaster (Kaggle)

Pipeline:

Dataset
↓
Data Cleaning
↓
Feature Selection
↓
Train/Test Split
↓
Model Training
↓
Evaluation
↓
Model Comparison

---

## Project Structure

ML-Model-Comparison-System

titanic_ml_project.py  
train.csv  
README.md  

---

## Machine Learning Algorithms Used

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

Libraries:

- scikit-learn
- XGBoost
- Pandas
- NumPy

---

## Data Preprocessing

Steps performed:

1. Feature Selection
2. Missing Value Handling
3. Train/Test Split
4. Feature Scaling

Example:

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="mean")
X = imputer.fit_transform(X)

---

## Model Evaluation Metrics

Models evaluated using:

- Accuracy
- F1 Score
- Cross Validation
- Confusion Matrix

Example:

Model: Random Forest
Accuracy: 0.84
F1 Score: 0.82

---

## Model Leaderboard Example

XGBoost → 0.86  
Random Forest → 0.84  
Logistic Regression → 0.80  
Decision Tree → 0.78  

---

## Run the Project

Install dependencies:

pip install pandas numpy scikit-learn xgboost

Run project:

python titanic_ml_project.py

---

## Learning Outcomes

This project demonstrates:

- End-to-end ML pipeline
- Model comparison
- Data preprocessing
- Evaluation metrics

---

## Author

Rohit Choukiker  
AI / ML Engineer
