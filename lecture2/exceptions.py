x = int(input("x: "))
y = int(input("y: "))

result = x / y

print(f"{x} / {y} is equal to {result}.")

# The above code should work correctly. However, if I try to divide a number by zero it will generate an error.

# Let's fix this with the 'exception' property

# NOTE: Comment the code above first to run the code below

import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:  # Create a exception based on the error
    print("Value type is invalid.")
    sys.exit(1)  # Exit the code without returning error

try:
    result = x / y
except ZeroDivisionError:
    print("It's not possible to divide by 0")
    sys.exit(1)

print(f"{x} / {y} is equal to {result}.")
