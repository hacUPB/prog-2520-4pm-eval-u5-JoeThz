import os
import csv
import matplotlib.pyplot as plt

#  CONFIGURACIÓN DE RUTAS AUTOMÁTICAS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_TXT = os.path.join(BASE_DIR, "relatividad.txt")
RUTA_CSV = os.path.join(BASE_DIR, "salida_mensual_pasajeros_aeropuerto_destino_internacional.csv")

# FUNCIONES PARA ARCHIVOS DE TEXTO (.txt)

def contar_palabras_y_caracteres():
    try:
        with open(RUTA_TXT, "r", encoding="utf-8") as f:
            texto = f.read()
    except Exception as e:
        print("No se pudo abrir el archivo de texto:", e)
        return

    palabras = texto.split()
    num_palabras = len(palabras)
    total_car = len(texto)
    car_sin_espacios = sum(1 for c in texto if c not in (" ", "\n", "\t"))

    print("\n Resultados del archivo de texto:")
    print("Ruta:", RUTA_TXT)
    print(" - Número de palabras:", num_palabras)
    print(" - Caracteres (con espacios):", total_car)
    print(" - Caracteres (sin espacios):", car_sin_espacios)


def reemplazar_palabra_en_archivo():
    palabra_buscar = input("Palabra a buscar: ")
    palabra_reemplazo = input("Palabra de reemplazo: ")

    try:
        with open(RUTA_TXT, "r", encoding="utf-8") as f:
            contenido = f.read()
    except Exception as e:
        print("No se pudo abrir el archivo de texto:", e)
        return

    if palabra_buscar not in contenido:
        print("La palabra no se encontró en el texto.")
        return

    nuevo_contenido = contenido.replace(palabra_buscar, palabra_reemplazo)
    salida = os.path.join(BASE_DIR, "relatividad_modificado.txt")

    try:
        with open(salida, "w", encoding="utf-8") as f:
            f.write(nuevo_contenido)
        print("Archivo guardado como:", salida)
    except Exception as e:
        print("Error al guardar:", e)


def histograma_vocales_txt():
    try:
        with open(RUTA_TXT, "r", encoding="utf-8") as f:
            texto = f.read()
    except Exception as e:
        print("No se pudo abrir el archivo de texto:", e)
        return

    texto = texto.lower()
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    conteos = {v: texto.count(v) for v in vocales}

    print("\nConteo de vocales:")
    for v in vocales:
        print(f"{v}: {conteos[v]}")

    plt.bar(vocales, [conteos[v] for v in vocales], color="red")
    plt.title("Ocurrencia de vocales en el texto")
    plt.xlabel("Vocal")
    plt.ylabel("Frecuencia")
    plt.show()

# FUNCIONES PARA ARCHIVOS CSV

def mostrar_15_primeras_filas():
    try:
        with open(RUTA_CSV, "r", encoding="utf-8") as f:
            lector = csv.reader(f)
            print("\nPrimeras 15 filas del CSV:")
            for i, fila in enumerate(lector):
                print(fila)
                if i >= 14:
                    break
    except Exception as e:
        print("No se pudo abrir el archivo CSV:", e)


def calcular_estadisticas_columna():
    try:
        with open(RUTA_CSV, "r", encoding="utf-8") as f:
            lector = csv.reader(f)
            filas = list(lector)
    except Exception as e:
        print("Error al abrir el archivo CSV:", e)
        return

    if not filas:
        print("El archivo está vacío.")
        return

    cabecera = filas[0]
    print("\nColumnas disponibles:")
    for i, col in enumerate(cabecera):
        print(f"{i}: {col}")

    try:
        indice = int(input("Seleccione el índice de la columna numérica: "))
    except:
        print("Entrada inválida.")
        return

    datos = []
    for fila in filas[1:]:
        if indice < len(fila):
            try:
                datos.append(float(fila[indice]))
            except:
                pass

    if not datos:
        print("No se encontraron datos numéricos.")
        return

    n = len(datos)
    promedio = sum(datos) / n
    datos_orden = sorted(datos)
    mediana = datos_orden[n//2] if n % 2 else (datos_orden[n//2 - 1] + datos_orden[n//2]) / 2
    desv = (sum((x - promedio) ** 2 for x in datos) / n) ** 0.5
    maximo, minimo = max(datos), min(datos)

    print("\nEstadísticas:")
    print("Cantidad de datos:", n)
    print("Promedio:", promedio)
    print("Mediana:", mediana)
    print("Desviación estándar:", desv)
    print("Máximo:", maximo)
    print("Mínimo:", minimo)


def graficar_columna():
    try:
        with open(RUTA_CSV, "r", encoding="utf-8") as f:
            lector = csv.reader(f)
            filas = list(lector)
    except Exception as e:
        print("No se pudo abrir el archivo CSV:", e)
        return

    if not filas:
        print("Archivo vacío.")
        return

    cabecera = filas[0]
    print("\nColumnas disponibles:")
    for i, col in enumerate(cabecera):
        print(f"{i}: {col}")

    try:
        indice = int(input("Seleccione el índice de la columna numérica: "))
    except:
        print("Entrada inválida.")
        return

    datos, posiciones = [], []
    for i, fila in enumerate(filas[1:], start=1):
        if indice < len(fila):
            try:
                datos.append(float(fila[indice]))
                posiciones.append(i)
            except:
                pass

    if not datos:
        print("No se encontraron datos numéricos.")
        return

    plt.scatter(posiciones, datos, color="blue")
    plt.title(f"Gráfico de dispersión - {cabecera[indice]}")
    plt.xlabel("Fila")
    plt.ylabel(cabecera[indice])
    plt.grid(True)
    plt.show()

    min_val, max_val = min(datos), max(datos)
    rango = max_val - min_val
    bins = 5
    ancho = rango / bins if rango > 0 else 1
    etiquetas, conteos = [], [0]*bins

    for i in range(bins):
        inicio = min_val + i * ancho
        fin = inicio + ancho
        etiquetas.append(f"{inicio:.2f}-{fin:.2f}")
    for v in datos:
        for i in range(bins):
            inicio = min_val + i * ancho
            fin = inicio + ancho
            if (i == bins - 1 and v <= fin) or (v < fin):
                conteos[i] += 1
                break

    plt.bar(etiquetas, conteos, color="green")
    plt.title(f"Distribución de valores - {cabecera[indice]}")
    plt.xlabel("Intervalos")
    plt.ylabel("Frecuencia")
    plt.grid(axis="y", linestyle="--", linewidth=0.5)
    plt.show()


# MENÚS

def submenu_txt():
    while True:
        print("\n--- Submenú: Procesar archivo de texto ---")
        print("1. Contar palabras y caracteres")
        print("2. Reemplazar palabra")
        print("3. Histograma de vocales")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            contar_palabras_y_caracteres()
        elif opcion == "2":
            reemplazar_palabra_en_archivo()
        elif opcion == "3":
            histograma_vocales_txt()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def submenu_csv():
    while True:
        print("\n--- Submenú: Procesar archivo CSV ---")
        print("1. Mostrar primeras 15 filas")
        print("2. Calcular estadísticas")
        print("3. Graficar columna")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            mostrar_15_primeras_filas()
        elif opcion == "2":
            calcular_estadisticas_columna()
        elif opcion == "3":
            graficar_columna()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def main():
    while True:
        print("\n===== HERRAMIENTA DE PROCESAMIENTO DE ARCHIVOS =====")
        print("1. Procesar archivo de texto (.txt)")
        print("2. Procesar archivo separado por comas (.csv)")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            submenu_txt()
        elif opcion == "2":
            submenu_csv()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
