import turtle

#hay un codigo encampsula que esta en el modulo turtle. En este codigo hay unas funciones
#definidas que hace que pueda avanzr o girar a la izquierda, etc
#pero uno se puede crear tantas instancias de este objeto como yo quiera (distintas tortuguitas)

tortuguita = turtle.Turtle()
otraTortuguita = turtle.Turtle()

#misma funcionalidad pero distintos comportamientos y atributos
tortuguita.shape('turtle')
tortuguita.fd(50)

otraTortuguita.color('green')
otraTortuguita.left(90)
otraTortuguita.fd(50)