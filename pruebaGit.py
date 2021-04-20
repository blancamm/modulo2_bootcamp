def sumaTodos(limitTo):
    resultado = 0
    for i in range (0, limitTo+1):
        resultado += i
        
    return resultado



#total =  sumaTodos(6) #el poder hacer esto, es decir, meter en variables funciones es una cosa seminueva y son de funciones de 1º clase

def sumaTodosLosCuadrados(limitTo):
    resultado = 0
    for i in range (limitTo+1):#si no se pone inicio coge 0
        resultado += i*i
        
    return resultado
        
print(sumaTodos(100))
print(sumaTodosLosCuadrados(3))
