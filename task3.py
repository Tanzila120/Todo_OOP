def multiple(*number):
    result = 1
    for i in number:
        result *= i
    return result
print(multiple(2, 3, 4))
