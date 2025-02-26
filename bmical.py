# CREATE  A BMI CALCULATOR
import streamlit as st
import time

st.set_page_config(page_title="BMI Calculator", page_icon="🤒", layout="centered")


st.title("BMI Calculator In python")
st.markdown("""
## Apna body index (html) calculator kren nechay apna **weight and height** enter kre """)

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("weight (in kg): " , min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("height (m): ", min_value=1.0, format="%.2f")

if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.subheader("Apka BMI hai:")
    st.markdown(f"{bmi:2f}",unsafe_allow_html=True)

    if bmi < 18.5:
        st.error("Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("Normal weight")
    elif 25 <= bmi < 29.9:
        st.warning("Overweight")
    else:
        st.error("Obesity 🚨")
else:
    st.info("Please enter a vaild weight and height")
