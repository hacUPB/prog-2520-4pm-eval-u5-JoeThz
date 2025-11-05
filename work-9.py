# Solicitamos al usuario el nombre del archivo a crear
lista = ["Perché Perché", "imagine", "Dulcito e Coco", "El comelon", "Quando Quando"]
ruta = "C:\\Users\\VICTUS\\Documents"
file_name =  input("Ingrese el nombre del archivo de texto: ")
file_info = ruta+"\\"+file_name
modo = input("Ingrese el modo de apertura del archivo, r (leer), w(reescribir), a(añadir): ")

fp = open(ruta + "\\" + file_name, modo, encoding="utf-8")

# Usamos 'with' para crear el contexto y escribir datos en el archivo 
with open(file_name, "w") as archivo:
    # Solicitamos al usuario los datos a escribir en el archivo
    datos = input("Ingrese los datos que desea escribir en el archivo: ")
    archivo.write(datos)

# Ahora usamos 'with' para crear el contexto donde leer los datos del archivo
with open(file_name, "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)