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

# Create button layout in a grid
rows = len(buttons) // 4 + (len(buttons) % 4 > 0)
for i in range(rows):
    cols = st.columns(4)
    for j in range(4):
        index = i * 4 + j
        if index < len(buttons):
            button = buttons[index]
            with cols[j]:
                if button == '=':
                    if st.button(button, key=f'btn_{button}', help="Calculate the result"):
                        result = calculate(st.session_state.expression)
                        st.session_state.expression = str(result)
                elif button == 'C':
                    if st.button(button, key=f'btn_{button}', help="Clear the expression"):
                        st.session_state.expression = ""
                else:
                    if st.button(button, key=f'btn_{button}', help=f"Add {button} to expression"):
                        update_expression(button)

# Styling for a better UI
st.markdown(
    """
    <style>
    body {
        background-color: #2E2E2E;
        color: #FFFFFF;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 15px;
        border: 2px solid #388E3C;
        border-radius: 8px;
        cursor: pointer;
        font-size: 18px;
        margin: 5px 0;  /* Consistent margin for better alignment */
        transition: background-color 0.3s, transform 0.2s;
        width: 100%;
        height: 60px;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .stTextInput>div>input {
        font-size: 24px;
        padding: 15px;
        border: 2px solid #4CAF50;
        border-radius: 8px;
        background-color: #4C4C4C;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
