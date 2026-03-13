# Exercise: Write a Python program to create a calculator class.
# Include methods for basic arithmetic operations.

# Define a class called Calculator to perform basic arithmetic operations
class Calculator:
    # Define a method for addition that takes two arguments and returns their sum
    def add(self, x, y):
        return x + y

    # Define a method for subtraction that takes two arguments and returns their difference
    def subtract(self, x, y):
        return x - y

    # Define a method for multiplication that takes two arguments and returns their product
    def multiply(self, x, y):
        return x * y

    # Define a method for division that takes two arguments and returns the result if the denominator is not zero,
    # or an error message if the denominator is zero
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")

# Example usage
# Create an instance of the Calculator class
calculator = Calculator()

# Perform addition and print the result
result = calculator.add(7, 5)
print("7 + 5 =", result)

# Perform subtraction and print the result
result = calculator.subtract(34, 21)
print("34 - 21 =", result)

# Perform multiplication and print the result
result = calculator.multiply(54, 2)
print("54 * 2 =", result)

# Perform division and print the result
result = calculator.divide(144, 2)
print("144 / 2 =", result)

# Attempt to perform division by zero, which raises an error, and print the error message
result = calculator.divide(45, 0)
print("45 / 0 =", result)
