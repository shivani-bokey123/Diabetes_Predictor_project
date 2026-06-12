# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 09:56:00 2026
@author: Shantanu
"""

import numpy as np
import pickle
import streamlit as st
import os

# Load models and scaler
# safer relative paths
base_path = os.path.dirname(__file__)

simple_model = pickle.load(open(os.path.join(base_path, "catboost_model.pkl"), "rb"))
advanced_model = pickle.load(open(os.path.join(base_path, "trained_model.pkl"), "rb"))
scaler = pickle.load(open(os.path.join(base_path, "scaler.pkl"), "rb"))

# Prediction functions
def simple_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
    prediction = simple_model.predict(input_data_as_numpy_array)
    return '🟢 Negative (Healthy)' if prediction[0] == 0 else '🔴 Positive (At Risk)'

def advanced_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
    std_data = scaler.transform(input_data_as_numpy_array)
    prediction = advanced_model.predict(std_data)
    return '🟢 Unlikely diabetes' if prediction[0] == 0 else '🔴 Likely diabetes'

# ✅ FAQ knowledge base
faq = {
    "diet": "Eat whole grains, vegetables, lean proteins, avoid refined sugar.",
    "exercise": "Do 30 minutes brisk walking or yoga daily.",
    "lifestyle": "Sleep 7-8 hours, manage stress, avoid smoking.",
    "foods to avoid": "Sugary drinks, white bread, fried foods, processed snacks.",
    "fruits": "Prefer apples, berries, oranges. Avoid very sweet fruits like mangoes and grapes.",
    "vegetables": "Eat spinach, broccoli, okra, beans. Limit starchy vegetables like potatoes.",
    "protein": "Include lentils, beans, paneer, eggs, fish. Avoid red meat and processed meats.",
    "breakfast": "Choose oats, multigrain bread, boiled eggs, or vegetable upma.",
    "snacks": "Healthy options are roasted chana, nuts, sprouts, or fruit salad.",
    "hydration": "Drink 8-10 glasses of water daily. Avoid sugary drinks and sodas.",
    "stress": "Practice yoga, meditation, or deep breathing to reduce stress.",
    "sleep": "Maintain 7-8 hours of consistent sleep daily.",
    "weight control": "Maintain a healthy BMI with balanced diet and regular exercise.",
    "oil": "Use olive oil, mustard oil, or groundnut oil. Avoid hydrogenated oils.",
    "routine": "Follow fixed meal timings, avoid late-night eating, and keep portions small."
}


# Main UI
def main():
    st.set_page_config(page_title="Disease Prediction", page_icon="🩺", layout="wide")

    # Sidebar navigation
    page = st.sidebar.selectbox("Choose Page", ["Simple Prediction", "Advanced Prediction", "FAQ Chatbot"])

    # ---------------- SIMPLE MODEL PAGE ----------------
    if page == "Simple Prediction":
        st.markdown("<h1 style='text-align: center; color: #2C3E50;'>Simple Disease Prediction</h1>", unsafe_allow_html=True)
        st.write("### Enter basic health details:")

        age = st.number_input("Age (years)", 1, 120, 30)
        gender = st.selectbox("Gender", ["Male", "Female"])
        polyuria = st.selectbox("Polyuria", ["No", "Yes"])
        polydipsia = st.selectbox("Polydipsia", ["No", "Yes"])
        sudden_weight_loss = st.selectbox("Sudden Weight Loss", ["No", "Yes"])
        weakness = st.selectbox("Weakness", ["No", "Yes"])
        polyphagia = st.selectbox("Polyphagia", ["No", "Yes"])
        genital_thrush = st.selectbox("Genital Thrush", ["No", "Yes"])
        irritability = st.selectbox("Irritability", ["No", "Yes"])
        visual_blurring = st.selectbox("Visual Blurring", ["No", "Yes"])
        itching = st.selectbox("Itching", ["No", "Yes"])
        delayed_healing = st.selectbox("Delayed Healing", ["No", "Yes"])
        partial_paresis = st.selectbox("Partial Paresis", ["No", "Yes"])
        muscle_stiffness = st.selectbox("Muscle Stiffness", ["No", "Yes"])
        alopecia = st.selectbox("Alopecia", ["No", "Yes"])

        if st.button("Predict", use_container_width=True):
            features = [[
                age,
                1 if gender == "Female" else 0,
                int(polyuria == "Yes"), int(polydipsia == "Yes"), int(sudden_weight_loss == "Yes"),
                int(weakness == "Yes"), int(polyphagia == "Yes"), int(genital_thrush == "Yes"),
                int(irritability == "Yes"), int(visual_blurring == "Yes"), int(itching == "Yes"),
                int(delayed_healing == "Yes"), int(partial_paresis == "Yes"),
                int(muscle_stiffness == "Yes"), int(alopecia == "Yes")
            ]]
            result = simple_prediction(features)
            st.success(result)

    # ---------------- ADVANCED MODEL PAGE ----------------
    elif page == "Advanced Prediction":
        st.markdown("<h1 style='text-align: center; color: #2C3E50;'>Advanced Diabetes Prediction</h1>", unsafe_allow_html=True)
        st.write("### Enter detailed medical parameters:")

        col1, col2 = st.columns(2)
        with col1:
            Pregnancies = st.number_input('Pregnancies', 0, 20, 1)
            BloodPressure = st.number_input('Blood Pressure (mm Hg)', 0, 200, 70)
            Insulin = st.number_input('Insulin', 0, 900, 80)
            DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', 0.0, 2.5, 0.3)
        with col2:
            Glucose = st.number_input('Glucose Level (mg/dL)', 0, 300, 120)
            SkinThickness = st.number_input('Skin Thickness (mm)', 0, 100, 20)
            BMI = st.number_input('BMI', 0.0, 70.0, 25.5)
            Age = st.number_input('Age (years)', 1, 120, 40)

        if st.button('Predict', use_container_width=True):
            diagnosis = advanced_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
            st.success(diagnosis)

    # ---------------- FAQ CHATBOT PAGE ----------------
   # ---------------- FAQ CHATBOT PAGE ----------------
    elif page == "FAQ Chatbot":
     st.markdown("<h1 style='text-align: center; color: #2C3E50;'>Diabetes Care FAQ Chatbot</h1>", unsafe_allow_html=True)

    # ✅ Initialize session messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ✅ Display previous messages
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # ✅ Single chat_input block
    if prompt := st.chat_input("Ask me about diet, health or lifestyle..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # ✅ Response logic
        if "diet" in prompt.lower():
            response = faq["diet"]
        elif "exercise" in prompt.lower():
            response = faq["exercise"]
        elif "lifestyle" in prompt.lower():
            response = faq["lifestyle"]
        elif "avoid" in prompt.lower():
            response = faq["foods to avoid"]
        elif "fruits" in prompt.lower():
            response = faq["fruits"]
        elif "vegetables" in prompt.lower():
            response = faq["vegetables"]
        elif "protein" in prompt.lower():
            response = faq["protein"]
        elif "breakfast" in prompt.lower():
            response = faq["breakfast"]
        elif "snacks" in prompt.lower():
            response = faq["snacks"]
        elif "hydration" in prompt.lower() or "water" in prompt.lower():
            response = faq["hydration"]
        elif "stress" in prompt.lower():
            response = faq["stress"]
        elif "sleep" in prompt.lower():
            response = faq["sleep"]
        elif "weight" in prompt.lower():
            response = faq["weight control"]
        elif "oil" in prompt.lower():
            response = faq["oil"]
        elif "routine" in prompt.lower():
            response = faq["routine"]
        else:
            response = "Maintain a balanced diet, regular exercise, and consult your doctor."

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)




if __name__ == '__main__':
    main()
