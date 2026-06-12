**Diabetes Disease Predictor**
*Problem Statement:*
Diabetes is a chronic disease affecting millions worldwide. Early detection and awareness are crucial for prevention and management. Most existing ML‑based predictors are accurate only when clinical blood test values are available (e.g., glucose, insulin, BMI). This creates a limitation: normal users without medical test results cannot use such predictors effectively.

To address this real‑world problem, I developed a two‑level Diabetes Disease Predictor:

**Advanced Diabetes Predictor**
This model uses clinical features and provides accurate predictions when proper medical test values are available.

Features used:

Age

Pregnancies

Blood Pressure

Glucose Level

Insulin Level

Skin Thickness

Diabetes Pedigree Function

BMI

Outcome (Positive = 1, Negative = 0)

**Limitation:** Prediction is reliable only when all values are correct and obtained through blood tests. Hence, it is suitable for medical professionals or users with lab reports.

**Basic Diabetes Predictor**
To make diabetes risk detection accessible for everyone, especially middle‑class users, I built a symptom‑based predictor that does not require medical knowledge or lab tests.

**Features used:**

Age

Gender

Polyuria

Polydipsia

Sudden Weight Loss

Weakness

Polyphagia

Genital Thrush

Visual Blurring

Itching

Irritability

Delayed Healing

Partial Paresis

Muscle Stiffness

Alopecia

Class (Outcome: Positive = 1, Negative = 0)

This model solves the accessibility gap by allowing normal users to check their diabetes risk based on common symptoms.

**Integrated Chatbot:**
I also integrated a Streamlit‑based chatbot that helps users with health‑related queries such as:

Diet recommendations

Sleep schedule guidance

Lifestyle tips

General health FAQs

The chatbot makes the application interactive and user‑friendly.

**Tech Stack:**
Web App: Streamlit

ML Models: Scikit‑Learn, XGBoost, LightGBM, CatBoost

Data Handling: Pandas, NumPy

Visualization: Matplotlib, Seaborn

Model Storage: Pickle‑Mixin

**Deployment:**
The application is deployed on Streamlit with a custom UI built using Streamlit components, making it simple and accessible for end‑users.

