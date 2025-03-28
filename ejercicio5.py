# coding=utf-8
__Author__ = "Víctor Davó Antón"

import random

# Función que determina si un número es par o impar
def esPar(numero):
    return numero % 2 == 0

def esImpar(numero):
    return not esPar(numero)

def generarPares(valores, inicio):
    pares = []
    numero = inicio if esPar(inicio) else inicio + 1  # Asegurar que es par
    for _ in range(valores):
        pares.append(numero)
        numero += 2
    return pares

def generarImpares(valores, inicio):
    impares = []
    numero = inicio if esImpar(inicio) else inicio + 1  # Asegurar que es impar
    for _ in range(valores):
        impares.append(numero)
        numero += 2
    return impares

# Programa principal
def main():
    print("Par e impar")
    n = int(input("Introduzca un número: "))
    print(f"{n} es par --> {esPar(n)}.")

    valores = int(input("Introduzca el número de valores: "))
    inicio = int(input("Introduzca el número inicial: "))

    pares = generarPares(valores, inicio)
    impares = generarImpares(valores, inicio)

    print("Pares:", pares)
    print("Impares:", impares)

if __name__ == "__main__":
    main()