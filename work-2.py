#Ejercicio 2
fichero = open("texto.txt","r", encoding="utf-8")
linea = fichero.readline()
print(linea)
linea = fichero.readline()
print(linea)
linea = fichero.readline()
print(linea)
fichero.close()