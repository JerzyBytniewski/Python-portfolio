# Simple calculator; enter two numbers and operator - receive a result.

number1 = float(input("Enter a number: "))
operator = input("Enter an operator: ")
number2 = float(input("Enter another number: "))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("Invalid input")
