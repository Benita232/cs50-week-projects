'''''
first_input = (input("Enter first number: "))
second_input = input("Enter arithmetic operation (+, -, *, /): ")
third_input = (input("Enter second number: "))
expression = f"{first_input} {second_input} {third_input}"
# Evaluate the expression and print the result
result = eval(expression)

print(f"The result of {expression} is: {result:.1f}")
'''

expression = input("Expression: ").strip()
result = eval(expression)
print(f"{result:.1f}")