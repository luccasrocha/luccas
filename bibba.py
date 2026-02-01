num = int(input('Digite um numero para\ncalcular seu fatorial: '))

if num < 0:
    print("Fatorial não definido para números negativos.")
elif num == 0:
    print('Calculando 0! = 1')
else:
    print(f'Calculando {num}! = ', end='')
    fatorial = 1
    for i in range(num, 0, -1):
        fatorial *= i
        if i > 1:
            print(f'{i} x ', end='')
        else:
            print(f'{i} = {fatorial}')