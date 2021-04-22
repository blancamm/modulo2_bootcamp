def factorial(numero):
    if numero > 0:
        return numero*factorial(numero-1)
    else:
        return 1
        

print (factorial(4))