def retroContador(numero):
    if numero < 0:
        print('el numero debe ser positivo')
        return
    if numero == 0:
        print('0')
        return
    else:
        print('{},'.format(numero), end='')
        retroContador(numero - 1)
        
retroContador(30)