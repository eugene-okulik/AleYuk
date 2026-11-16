def what_operation(func):

    def wrapper(a, b):
        if a < 0 or b < 0:
            operation = "*"
        elif a == b:
            operation = "+"
        elif a > b:
            operation = "-"
        else:
            operation = "/"
        return func(a, b, operation)
    return wrapper


@what_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    else:
        return first / second


first_num = int(input("Введите число №1: "))
second_num = int(input("Введите число №2: "))

print(calc(first_num, second_num))