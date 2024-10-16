import ipywidgets as widgets
from IPython.display import display
import math

# Function to calculate the result
def calculate(button):
    expression = entry.value
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
        
        output.value = f"Result: {result}"
    except Exception as e:
        output.value = f"Error: {e}"

# Create input field
entry = widgets.Text(
    description='Input:',
    placeholder='Enter expression'
)

# Create calculate button
calc_button = widgets.Button(
    description='Calculate',
    button_style='success'
)
calc_button.on_click(calculate)

# Create output area
output = widgets.Label(value="Result will be displayed here.")

# Display widgets
display(entry, calc_button, output)
