def process_order(*args, **info):
    
    print("Продукты:", end=' ')
    for i in args:
        print(i, end=', ' if i != args[-1] else '')
    
    print("\nИнформация:")
    
    for k in info:
        print(f"{k}: {info[k]}")

process_order('Пицца', 'Суши', name='Райан', surname='Гослинг')
