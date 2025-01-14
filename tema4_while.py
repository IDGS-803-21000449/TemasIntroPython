
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))
contador = 1

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
