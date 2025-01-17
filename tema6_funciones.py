import os


def funcion1():
    print("Suma")
    print("Dame dos numeros: ")
    num1= int(input("Ingresa un numero"))
    num2= int(input("Ingresa el segundo numero"))
    print("La suma de los numeros es: ", num1 + num2)

def funcion2():
    print("Resta")
    print("Dame dos numeros: ")
    num1= int(input("Ingresa un numero"))
    num2= int(input("Ingresa el segundo numero"))
    print("La resta de los numeros es: ", num1 - num2)

def funcion3():
    print("Multiplicación")
    print("Dame dos numeros: ")
    num1= int(input("Ingresa un numero"))
    num2= int(input("Ingresa el segundo numero"))
    print("La resta de los numeros es: ", num1 * num2)

def funcion4():
    print("División")
    print("Dame dos numeros: ")
    num1= int(input("Ingresa un numero"))
    num2= int(input("Ingresa el segundo numero"))
    print("La resta de los numeros es: ", num1 / num2)

def volver():
    opc = int(input("¿Desea hacer otra consulta? 0-Salir 1-Seguir: "))
    if opc == 0:
        exit()
    if opc == 1:
        run()


def run():

    
    os.system("cls")
    print("Menu de opciones: ")
    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicación")
    print("4- División")
    print("5- Salir")


    opcion = int(input("Dame una opcion:")) 
    if opcion == 1:
        funcion1()
        volver()
    if opcion == 2:
        funcion2()
        volver()
    if opcion == 3:
        funcion3()
        volver()
    if opcion == 4:
        funcion4()
        volver()
    if opcion == 5:
        exit()


if __name__ == "__main__":
    run()

