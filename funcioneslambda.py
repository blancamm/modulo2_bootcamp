from funciones1nivel import sumaTodos #asi ya puedo sumar lo que sea

#otra lambda seria
normal = lambda x: x

print(sumaTodos(3, lambda x: x**3)) #lambda funcion anonima, sin nombre

#para que se vea mejor es como poner:
'''
triple = lambda x: x**3
print(sumaTodos(3, triple))
'''

'''
las lambda se utilizan cunaod no quieres definir una funcion porque
no vas a reutilizar esa funcion en otro fichero
'''