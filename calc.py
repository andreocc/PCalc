import streamlit as st

st.title("Calculator")

# Get input from the user
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

# Select operation
operation = st.selectbox("Select operation", ["+", "-", "*", "/"])

# Perform operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
else:
    result = num1 / num2

# Display result
st.write("The result is:", result)