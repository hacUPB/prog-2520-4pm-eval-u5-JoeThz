# Leer 1
#1. Abrir el archivo
lv = open("C:\\Users\\VICTUS\\Desktop\\Texto_90frases_inspiradoras.txt","r", encoding="utf-8")

#2. Leer el archivo
#datos = lv.read(14711)
#datos = lv.readline()

lv.readline()
lv.readline()
lv.readline()
lv.readline()
lv.readline()
lv.read(3)
datos = lv.readline()

#3. Cerrar el archivo
lv.close()

print(datos)