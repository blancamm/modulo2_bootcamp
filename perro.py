class Dog():
    def __init__(self):
        self.nombre = ''
        self.edad = None
        self.peso = None
#en este caso solo se puedo informar de los atributos desde fuera, desde la consola
        # no se puede informar de ellos al crear la instancia

class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
        
    def ladrar(self): #selfllama a la instacia de nuestro objeto
        if self.peso >= 8:
            print('GUAU, GUAU')
        else:
            print('guau,guau') #la funcionalidad cambia segun los atributos
    def __str__(self):
        return 'Soy el perro {} con edad: {}, y peso: {}'.format(self.nombre, self.edad, self.peso)
        
# salchicho = Perro('Salchicho', 3, 12)
#lola = Perro('Lola', 8, 1.5)

class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False #asi es privado yo no puedo preguntar por el
        
    def __str__(self): # se ha sobreescrito este metodo
        return 'Perro de asistencia de {}'.format(self.amo)
    
    def pasear(self):
        print('{} ayuda a su amo {} a pasear'.format(self.nombre, self.amo))
    
    def ladrar(self):
        if self.trabajando: #como poner true
            print ('shhh, no puedo ladrar')
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor = None): #para mdoficiar el atributo de trabajando de una manera mas elegante
        if valor == None: #para acceder al atributo __trabajando lo tengo que hacer mediante esta funcion
            return self.__trabajando
        else:
            self.__trabajando = valor

#yo puedo cambiar el atributo de trabajando desde la consola:
            #toby.trabajando = True
            #luego saldria lo de shhh