Diabetes Disease Predictor (Two‑Level Model + Chatbot)

Problem Statement
Diabetes is a chronic disease affecting millions worldwide. Most ML predictors rely on clinical blood test values (glucose, insulin, BMI), limiting accessibility for normal users.
This project introduces a two‑level predictor:

Advanced Predictor → Clinical features for accurate detection.

Basic Predictor → Symptom‑based detection for accessibility without lab tests.

Models Compared
Implemented and evaluated multiple ML algorithms:

Logistic Regression

Support Vector Machine (SVM)

Random Forest

Decision Tree

XGBoost

Gradient Boosting

Accuracy of each model was compared, and the best performing model was selected for deployment.

Data Processing
Data Cleaning → handled missing values, normalized features.

Data Splitting → train/test split for evaluation.

Model Training → trained multiple models and selected the one with highest accuracy.

Model Storage → saved using Pickle‑Mixin for deployment.

Features Used
Advanced Model: Age, Pregnancies, Blood Pressure, Glucose, Insulin, Skin Thickness, Diabetes Pedigree Function, BMI.

Basic Model: Age, Gender, Polyuria, Polydipsia, Weight Loss, Weakness, Polyphagia, Genital Thrush, Visual Blurring, Itching, Irritability, Delayed Healing, Partial Paresis, Muscle Stiffness, Alopecia.

Integrated Chatbot
Streamlit‑based chatbot provides:

Diet recommendations

Sleep schedule guidance

Lifestyle tips

General health FAQs

Tech Stack
Languages/Frameworks: Python, Streamlit

Libraries: Scikit‑Learn, XGBoost, LightGBM, CatBoost, Pandas, NumPy, Matplotlib, Seaborn

Deployment: Streamlit with custom UI

Impact
Makes diabetes prediction accessible for users without lab tests.

Provides interactive chatbot for lifestyle guidance.

Demonstrates comparison of multiple ML models with accuracy evaluation.
