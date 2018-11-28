# Receive the largest and the smallest number in a collection.

def max_number(number1, number2, number3, number4, number5):
    if number1 >= number2 and number1 >= number3 and number1 >= number4 and number1 >= number5:
        return number1
    elif number2 >= number1 and number2 >= number3 and number2 >= number4 and number2 >= number5:
        return number2
    elif number3 >= number1 and number3 >= number2 and number3 >= number4 and number3 >= number5:
        return number3
    elif number4 >= number1 and number4 >= number2 and number4 >= number3 and number4 >= number5:
        return number4
    else:
        return number5

def min_number(number1, number2, number3, number4, number5):
    if number1 <= number2 and number1 <= number3 and number1 <= number4 and number1 <= number5:
        return number1
    elif number2 <= number1 and number2 <= number3 and number2 <= number4 and number2 <= number5:
        return number2
    elif number3 <= number1 and number3 <= number2 and number3 <= number4 and number3 <= number5:
        return number3
    elif number4 <= number1 and number4 <= number2 and number4 <= number3 and number4 <= number5:
        return number4
    else:
        return number5

print(max_number(30, 4, 554, 6587, -55))
print(min_number(30, 4, 554, 6587, -55))