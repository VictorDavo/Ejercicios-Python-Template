# coding=utf-8
__Author__="Víctor Davó Antón"

#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.

# Implemente función esMayorEdad(e)

def esMayorEdad(edad,nombre):
    if (edad >= 18):
        print("Eres mayor de edad, puedes conducir " + nombre)
        return True
    else:
        print("No eres mayor de edad, no puedes conducir " + nombre)
        return False

# Programa principal
def main():
    nombre=input("Introduce tu nombre: ")
    edad=int(input(f"Introduce tu edad {nombre}"))

    # Utilice la función definida
    esMayorEdad(edad,nombre)
    # Estructura alternativa Si (condidición con función) entonces --> sino ...

if __name__== "__main__" :
   main()