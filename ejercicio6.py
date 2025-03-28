# coding=utf-8
__Author__="Víctor Davó Antón"


# Función que determina si un numero es primo.

def esPrimo(numero) :
    contador = 0

    if numero==1 :
        return True

    if numero <= 3 :
        return True
    
    if numero %2 == 0 or numero %3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero %i == 0 or numero % (i +2) == 0:
            return False
        i += 6
    return True

# Programa principal
def main():
    print("ES PRIMO")
    n=int(input("Introduzca un numero: "))
    print("{0} es primo --> {1}.".format(n,esPrimo(n)))

if __name__== "__main__" :
   main()