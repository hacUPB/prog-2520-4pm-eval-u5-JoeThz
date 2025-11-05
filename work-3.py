#Ejercicio 3
from random import randint

lista = []
for i in range(50):
    lista.append(randint(0,100))

maximo = str(max(lista))
minimo = str(min(lista))
prom = str(sum(lista)/len(lista))

file_datos = open("datos.txt","w", encoding="utf-8")
file_datos.write(maximo)
file_datos.write("\n")
file_datos.write(minimo)
file_datos.write("\n")
file_datos.write(prom)
file_datos.write("\n")
file_datos.close()
print("Archivo creado...")