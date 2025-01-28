import os

class Diccionario:

    def __init__(self, palabra1="", palabra2=""):
        self.palabra1 = palabra1
        self.palabra2 = palabra2

    def agregar_palabra(self):
        print("Escribe una palabra en español:")
        self.palabra1 = input("Español: ")
        print("Escribe su traducción en inglés:")
        self.palabra2 = input("Inglés: ")

        archivo = open("mi_diccionario.txt", "a")
        archivo.write(self.palabra1)
        archivo.write(" ")
        archivo.write(self.palabra2)
        archivo.write("\n")
        archivo.close()

        print(f"Se agregó: {self.palabra1} - {self.palabra2}")
        input("Pulsa Enter para continuar...")

    def buscar_palabra(self):
        print("Selecciona el idioma para buscar:")
        print("1. Español")
        print("2. Inglés")
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            palabra = input("Palabra en español: ")
        elif opcion == 2:
            palabra = input("Palabra en inglés: ")
        else:
            print("Opción no válida.")
            return

        txt = ""
        archivo = open("mi_diccionario.txt", "r")
        for linea in archivo:
            txt += linea
        archivo.close()

        if palabra in txt:
            archivo = open("mi_diccionario.txt", "r")
            for linea in archivo:
                espanol, ingles = linea.strip().split(" ")
                if palabra == espanol or palabra == ingles:
                    print(f"Palabra encontrada: {espanol} - {ingles}")
                    break
            archivo.close()
        else:
            print(f"La palabra '{palabra}' no se ha encontrado en el diccionario.")

        input("Pulsa Enter para continuar...")



def menu():
    diccionario = Diccionario()

    while True:
        os.system("cls")
        print("¿Que desea hacer?")
        print("1. Agregar palabra")
        print("2. Buscar palabra")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            diccionario.agregar_palabra()
        if opcion == "2":
            diccionario.buscar_palabra()
        if opcion == "3":
            print("Adios")
            break

if __name__ == "__main__":
    menu()


    