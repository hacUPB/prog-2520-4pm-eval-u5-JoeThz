lista = ["Perché Perché", "imagine", "Dulcito e Coco", "El comelon", "Quando Quando"]
ruta = "C:\\Users\\VICTUS\\Documents"
file_name = "Canciones.txt"
file_info = ruta+"\\"+file_name
modo = "r"


with open(file_info, modo, encoding="utf-8") as archivo: #el "with" es un manejador de contextos.
    # Hacer operaciones con el archivo
    for dato in archivo:
        print(dato, end="")
# El archivo se cierra automáticamente al salir del bloque with
