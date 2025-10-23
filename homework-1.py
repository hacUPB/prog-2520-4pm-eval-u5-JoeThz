#"try except" sirve para capturar excepciones o errores en tiempo de ejecución
# para manejarla sin que el programa se detenga. Ejemplo breve y solución para el work-1.py:
# como el error era "FileNotFoundError" o sea que el archivo no existe,
# el siguiente código lo captura y muestra un mensaje.

try:
    with open("texto.txt", "r", encoding="utf-8") as fp:
        datos = fp.read(5)
        print(datos)
        datos = fp.read(5)
        print(datos)
except FileNotFoundError:
    print("Error: 'texto.txt' no existe. Crea el archivo en la misma carpeta o corrige la ruta.")
except Exception as e:
    print("Error al leer el archivo:", e)