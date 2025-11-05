# Análisis del Proyecto

## Organización del código
- `main.py` contiene funciones separadas por responsabilidad:
  - Utilidades: listar archivos.
  - Archivo .txt: conteo, reemplazo, histograma vocales.
  - Archivo .csv: mostrar filas, estadísticas por columna, graficar.
  - Menús interactivos.

## Conceptos usados
- Condicionales: `if/elif/else` para control de flujo en menús.
- Bucles: `for`, `while` para recorrer archivos, filas y contar elementos.
- Listas: para almacenar filas y datos numéricos.
- Manejo de cadenas: `.split()`, `.strip()`, `.lower()`, `.replace()`.
- Manejo de CSV: módulo `csv` para lectura de archivos separados por comas.
- Estadística básica: módulo `statistics` para media, mediana, desviación.
- Visualización: `matplotlib` para gráficas.

## Decisiones de diseño
- No se usan list comprehensions ni librerías no vistas en clase.
- Lectura por filas para mantener claridad.
- En reemplazo, se pregunta si sobrescribir o guardar copia.

## Limitaciones
- Soporta CSV con separador coma. No maneja todos los casos de quoting complejos.

## Ayuda a IA
- Pedí ayuda a la IA para la explicación de algunas funciones al momento de manejar el archivo csv, debido a que durante de la explicación en clase, no pude entenderla bien porque mi computadora no tenia activado office y no pude practicar en clase lo que iban haciendo. tambien me dió la idea de usar una variable para las rutas y con explicaciones del modulo OS.