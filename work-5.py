# Archivo es interable

lv = open("C:\\Users\\VICTUS\\Desktop\\Texto_90frases_inspiradoras.txt","r", encoding="utf-8")

for i in lv:
   datos = lv.readline()
   print(datos[0], end="")
lv.close()
