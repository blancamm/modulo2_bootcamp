


def MAX(*l):
    if len(l) ==0:
        return 0
    m = l[0]
    for i in range(1,len(l)): #comprobar el 0 ya esta comprobado antes y se pone l no *l
        if l[i] > m:
            m = l[i]
    return m

def MIN(*l):
    if len(l) ==0:
        return 0
    m = l[0]
    for i in range(1,len(l)): #comprobar el 0 ya esta comprobado antes y se pone l no *l
        if l[i] < m:
            m = l[i]
    return m

def media(*l):
    if len(l) ==0:
        return 0
    suma = 0
    for valor in l:
        suma += valor
        
    return suma/len(l)
#si loponemos al principio no se han definido las funciones y peta
funciones = {
    'max':MAX,
    'min':MIN,
    'media': media}

def returnFuncion(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    return None
    
print(returnFuncion('max')(3,5,78,9,0))