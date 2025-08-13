# This is a simple calculator program that asks the user for two numbers
# and an operation (+, -, *, /), then performs the calculation.

# Ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# Ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation based on the chosen operation
if operation == "+":
    result = num1 + num2  # Addition
elif operation == "-":
    result = num1 - num2  # Subtraction
elif operation == "*":
    result = num1 * num2  # Multiplication
elif operation == "/":
    # Check to avoid division by zero
    if num2 != 0:
        result = num1 / num2  # Division
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"  # If user enters something other than +, -, *, /

# Display the result
print("Result:", result)