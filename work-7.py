lista = ["Perché Perché", "imagine", "Dulcito e Coco", "El comelon", "Quando Quando"]
ruta = "C:\\Users\\VICTUS\\Documents"
file_name = "Canciones.txt"
file_info = ruta+"\\"+file_name
modo = "w"

# fp.writelines(lista)
for i in range(len(lista)):
    lista[i] += "\n"

fp = open(file_info, modo, encoding="utf-8")
fp.writelines(lista)
fp.close()