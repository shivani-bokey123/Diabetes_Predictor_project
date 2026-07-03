Diabetes Disease Predictor (Two‑Level Model + Chatbot)
🔹 Problem Statement
➡️ Diabetes is a chronic disease affecting millions worldwide.

➡️ Most ML predictors rely on clinical blood test values (Glucose, Insulin, BMI).

➡️ Limitation: Normal users without lab tests cannot use such predictors effectively.

➡️ Solution: Developed a two‑level predictor (Advanced + Basic) with chatbot integration.

🔹 Advanced Diabetes Predictor
➡️ Uses clinical features for accurate detection.

➡️ Features: Age, Pregnancies, Blood Pressure, Glucose, Insulin, Skin Thickness, Diabetes Pedigree Function, BMI.

➡️ Limitation: Reliable only with proper lab test values.

🔹 Basic Diabetes Predictor
➡️ Uses symptom‑based inputs for accessibility without lab tests.

➡️ Features: Age, Gender, Polyuria, Polydipsia, Weight Loss, Weakness, Polyphagia, Genital Thrush, Visual Blurring, Itching, Irritability, Delayed Healing, Partial Paresis, Muscle Stiffness, Alopecia.

➡️ Solves accessibility gap for middle‑class users.

🔹 Integrated Chatbot
➡️ Built with Streamlit for interactivity.

➡️ Provides:

→ Diet recommendations

→ Sleep schedule guidance

→ Lifestyle tips

→ General health FAQs

🔹 Data Processing Workflow
➡️ Data Cleaning → handled missing values, normalized features.

➡️ Data Splitting → train/test split for evaluation.

➡️ Model Training → trained multiple ML models.

➡️ Model Comparison → checked accuracy and selected best performing model.

🔹 Models Compared
➡️ Logistic Regression

➡️ Support Vector Machine (SVM)

➡️ Random Forest

➡️ Decision Tree

➡️ XGBoost

➡️ Gradient Boosting

🔹 Tech Stack
➡️ Languages/Frameworks: Python, Streamlit

➡️ Libraries: Scikit‑Learn, XGBoost, LightGBM, CatBoost, Pandas, NumPy, Matplotlib, Seaborn

➡️ Model Storage: Pickle‑Mixin

➡️ Deployment: Streamlit with custom UI

🔹 Impact
➡️ Accessible diabetes prediction for users without lab tests.

➡️ Accurate detection for medical professionals with clinical data.

➡️ Interactive chatbot improves user experience.
