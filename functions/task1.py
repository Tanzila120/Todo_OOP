def is_odd(number):
    number = number % 2 != 0
    if number == 0:
        return True
    else:
        return False

number1=int(input('Ввдите число:'))
number = is_odd(number1)
print ('Число является:', number)
