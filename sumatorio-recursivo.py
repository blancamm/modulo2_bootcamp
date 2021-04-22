def sumatorio(n):
    if n > 0:
        return n + sumatorio(n-1)
       
       # return este return es como poner return none o return pass
       #y lo de atras seria 1 +None que peta. Hay que sumar numeros.
    else:
        return 0

print(sumatorio(4))

#es una maquina que tarda bastante, porque aqui esta esperando a que pare para volver para atras