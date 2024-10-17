def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise Error("Деление на ноль недоcтупно=/")
    return a / b

def calculator(a, b, calc='+'):
    if calc == '+':
        return addition(a, b)
    elif calc == '-':
        return subtraction(a, b)
    elif calc == '*':
        return multiplication(a, b)
    elif calc == '/':
        return division(a, b)
    else:
        raise Error("Операция не проходит: " + calc)

print(calculator(3, 2))
print(calculator(3, 2, '*'))
