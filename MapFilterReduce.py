from functools import reduce

#se hace lo anterior porque si no reduce no funciona

lista = [1, 3, -1, 15, 9]

listaDobles = map(lambda x: x*2, lista)

#otra manera de ponerlo
def doble(x):
    return x*2
listaDobles = map(doble, lista)


a =list(listaDobles)
print(a)

listaPares =filter (lambda x: x%2==0, lista) #solo devuelve si el resto es 0, si no lo es el resultado en None

b =list(listaPares)
print(b)

sumatorio = reduce(lambda x, y: x + y, range(101))

sumatorioDobles = reduce(lambda x, y : x + y*2, lista) #no funciona porque el primer x no lo multiplica por dos

print(sumatorio)
print(sumatorioDobles)
