import random

def is_odd(number):
    return number % 2 != 0

def count_odd_even(n):
    odd_count = 0
    even_count = 0
    for _ in range(n):
        total = random.randint(0, 1000)
        if is_odd(total):
            odd_count += 1
        else:
            even_count += 1
    return {"odd": odd_count, "even": even_count}


result = count_odd_even(100)
print(result)
