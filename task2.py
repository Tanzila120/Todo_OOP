import random 

odd = 0 
even = 0 

for i in range(random.randint(1, 100)):
    total = random.randint(1, 1000)
    print(total, end=' ')

    if total % 2 == 0: 
        even += 1 
    else: 
        odd += 1 

print('\nЧетные:',even) 
print('Не четные:', odd)
