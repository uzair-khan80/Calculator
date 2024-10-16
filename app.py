import streamlit as st
import math

# Function to calculate the result
def calculate(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

# Initialize session state for the current expression
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Function to update the expression
def update_expression(value):
    st.session_state.expression += value

# Streamlit app layout
st.title("🧮 Scientific Calculator")
st.write("Enter your calculations below:")

# Display the current expression
st.write("Current Expression:")
st.text_input("Expression", value=st.session_state.expression, key="input", disabled=True)

# Define buttons for digits and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+',
    'sin(', 'cos(', 'tan(', 'log(',
    'sqrt(', '='
]

# Create button layout
cols = st.columns(4)
for i, button in enumerate(buttons):
    with cols[i % 4]:
        if button == '=':
            if st.button(button, key=f'btn_{button}'):
                result = calculate(st.session_state.expression)
                st.session_state.expression = str(result)
        elif button == 'C':
            if st.button(button, key=f'btn_{button}'):
                st.session_state.expression = ""
        else:
            if st.button(button, key=f'btn_{button}'):
                update_expression(button)

# Styling for a better UI
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 15px;
        border: 2px solid #388E3C;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        margin: 5px;
        transition: background-color 0.3s;
        width: 100%;
        height: 60px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>input {
        font-size: 24px;
        padding: 10px;
        border: 2px solid #4CAF50;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
