import streamlit as st
from logic import multiply

st.title("Simple Multiplication App Virtusa -")

a = st.number_input("Enter first number", value=0)
b = st.number_input("Enter second number", value=0)

if st.button("Multiply"):
    result = multiply(a, b)
    st.success(f"Result: {result}")
