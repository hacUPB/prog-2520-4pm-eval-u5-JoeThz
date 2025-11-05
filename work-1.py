#Ejercicio 1
fp = open("texto.txt","r", encoding="utf-8")
datos = fp.read(5)
print(datos)
datos = fp.read(5)
print(datos)
fp.close()

