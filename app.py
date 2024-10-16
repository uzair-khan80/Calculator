import streamlit as st
import math

# Function to calculate the result
def calculate(expression):
    try:
        # Evaluate the expression
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

# Initialize session state for the current expression
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Streamlit app layout
st.title("Scientific Calculator")

# Display the current expression
st.write("Current Expression:", st.session_state.expression)

# Define a function to update the expression
def update_expression(value):
    st.session_state.expression += value

# Define buttons for digits and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'sin(', 'cos(', 'tan(', 'log(',
    'sqrt(', 'C'
]

# Create buttons dynamically
cols = st.columns(4)
for i, button in enumerate(buttons):
    with cols[i % 4]:
        if button == '=':
            if st.button(button):
                result = calculate(st.session_state.expression)
                st.session_state.expression = str(result)
        elif button == 'C':
            if st.button(button):
                st.session_state.expression = ""
        else:
            if st.button(button):
                update_expression(button)

# Input field for the expression
st.text_input("Expression", value=st.session_state.expression, key="input", disabled=True)
