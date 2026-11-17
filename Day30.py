#practice of Exception handling

#1)Basic try-except (Handling Division by Zero)
#When a user provides unexpected input or a mathematical impossibility occurs (like dividing by zero), Python raises an exception. A try-except block catches this error so the program can keep running. 
#•	Task: Write a script that safely divides two numbers provided by the user

try:
    numerator =int(input("Enter number1:"))
    denominator = int(input("Enter number2:"))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero!")

print("Program continues running smoothly...")

#2)Handling Multiple Specific Exceptions
#A single try block can fail in different ways. You can provide multiple except blocks to handle each potential error type specifically. 
#•	Task: Ask the user for a number, convert it to an integer, and divide 100 by it. Handle both non-numeric inputs and zero inputs.
try:
    user_input = input("Enter a number to divide 100: ")
    number = int(user_input)
    result = 100 / number
    print(f"100 divided by {number} is {result}")
except ValueError:
    print("Error: Please enter a valid integer, not text.")
except ZeroDivisionError:
    print("Error: You cannot enter zero as the divisor.")

