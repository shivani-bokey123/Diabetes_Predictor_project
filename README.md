Diabetes Disease Predictor (Two‑Level Model + Chatbot)
Problem Statement
Diabetes is a chronic disease affecting millions worldwide.
Most ML predictors rely on clinical blood test values (Glucose, Insulin, BMI).
Normal users without lab tests cannot use such predictors effectively.
To solve this, I developed a two‑level predictor (Advanced + Basic) with chatbot integration.

Advanced Diabetes Predictor
Uses clinical features for accurate detection.
Features: Age, Pregnancies, Blood Pressure, Glucose, Insulin, Skin Thickness, Diabetes Pedigree Function, BMI.
Limitation: Reliable only with proper lab test values.

Basic Diabetes Predictor
Uses symptom‑based inputs for accessibility without lab tests.
Features: Age, Gender, Polyuria, Polydipsia, Weight Loss, Weakness, Polyphagia, Genital Thrush, Visual Blurring, Itching, Irritability, Delayed Healing, Partial Paresis, Muscle Stiffness, Alopecia.
Solves accessibility gap for middle‑class users.

Integrated Chatbot
Built with Streamlit, providing:

Diet recommendations

Sleep schedule guidance

Lifestyle tips

General health FAQs

Data Processing Workflow
Data Cleaning: Handled missing values and normalized features.

Data Splitting: Divided dataset into training and testing sets.

Model Training: Trained multiple ML models.

Model Comparison: Evaluated accuracy and selected the best performing model.

Models Compared
During experimentation, I implemented and compared multiple machine learning algorithms including Logistic Regression, Support Vector Machine (SVM), Random Forest, Decision Tree, XGBoost, and Gradient Boosting. Each model was trained and tested on the dataset, and their accuracy was evaluated. Based on this comparison, the models with higher accuracy were selected for deployment in the final application.

Tech Stack
Languages/Frameworks: Python, Streamlit
Libraries: Scikit‑Learn, XGBoost, LightGBM, CatBoost, Pandas, NumPy, Matplotlib, Seaborn
Model Storage: Pickle‑Mixin
Deployment: Streamlit with custom UI

Impact
Accessible diabetes prediction for users without lab tests.
Accurate detection for medical professionals with clinical data.
Interactive chatbot improves user experience.
