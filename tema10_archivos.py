

from io import open

texto= "una line con a"
archivo= open("archivo.txt", "w")
archivo.write(texto)
archivo.close()