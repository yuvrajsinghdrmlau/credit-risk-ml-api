import streamlit as st
import requests

st.title("Credit Risk Prediction")

st.write("Enter customer details to predict credit risk.")

limit_balance = st.number_input("Credit Limit", value=20000)
age = st.number_input("Age", value=24)

sex = st.selectbox("Sex", ["male", "female"])
education = st.selectbox(
    "Education",
    ["graduate_school", "university", "high_school", "others"]
)

marriage = st.selectbox(
    "Marriage Status",
    ["single", "married", "other"]
)

pay_0 = st.number_input("Repayment Status September", value=-1)
pay_2 = st.number_input("Repayment Status August", value=-1)
pay_3 = st.number_input("Repayment Status July", value=-1)
pay_4 = st.number_input("Repayment Status June", value=-1)
pay_5 = st.number_input("Repayment Status May", value=-2)
pay_6 = st.number_input("Repayment Status April", value=-2)

if st.button("Predict Risk"):

    url = "https://credit-risk-ml-api-8s0o.onrender.com/predict"

    data = {
        "limit_balance": limit_balance,
        "sex": sex,
        "education": education,
        "marriage": marriage,
        "age": age,
        "pay_0": pay_0,
        "pay_2": pay_2,
        "pay_3": pay_3,
        "pay_4": pay_4,
        "pay_5": pay_5,
        "pay_6": pay_6
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['credit_risk']}")
    else:
        st.error("API request failed")