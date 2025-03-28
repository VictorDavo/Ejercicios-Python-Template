# coding=utf-8
__Author__="Víctor Davó Antón"

# Función que determina si un numero es primo.

def fibonacci(n) :
    vector = []

    if n<1 :
        return vector
    elif n==1 :
        vector.append(1)
        return vector
    elif n >=2 :
        # Implementa las series de Fibonacci
        # vector[0]=1
        # vector[1]=1
        # Creamos aquí el bucle WHILE
        # --> Implemente el código del Bucle
        x, y = 0, 1
        i = 0
        while i < n:
            x, y = y, x+y
            i += 1
            vector.append(x)
    return vector; # Retorno de la función

# Programa principal
def main():
    print("SERIE DE FIBONACCI")
    numero=int(input("Introduzca un numero: "))
    print("{0} elementos --> FIBONACCI: {1}.".format(numero,fibonacci(numero)))

if __name__== "__main__" :
   main()