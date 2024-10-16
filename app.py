import streamlit as st
import math

# Function to calculate the result
def calculate(expression):
    try:
        if expression.startswith("sin("):
            angle = float(expression[4:-1])
            result = math.sin(math.radians(angle))
        elif expression.startswith("cos("):
            angle = float(expression[4:-1])
            result = math.cos(math.radians(angle))
        elif expression.startswith("tan("):
            angle = float(expression[4:-1])
            result = math.tan(math.radians(angle))
        elif expression.startswith("log("):
            value = float(expression[4:-1])
            result = math.log(value)
        elif expression.startswith("sqrt("):
            value = float(expression[5:-1])
            result = math.sqrt(value)
        else:
            result = eval(expression)
        
        return result
    except Exception as e:
        return f"Error: {e}"

# Streamlit app layout
st.title("Scientific Calculator")

# User input
expression = st.text_input("Enter your calculation (e.g., sin(30), 2 + 3):")

if st.button("Calculate"):
    result = calculate(expression)
    st.write(f"Result: {result}")
