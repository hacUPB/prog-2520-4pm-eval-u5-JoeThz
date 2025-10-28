### Metodos de cadenas de caracteres:
permiten analizar, modificar y formatear texto de forma eficiente.
**Los métodos de cadenas en Python permiten analizar, modificar y formatear texto de forma eficiente. Aquí tienes los más útiles organizados por función.**

---

### 🔍 Métodos de análisis y búsqueda

- **`count(sub)`**: Cuenta cuántas veces aparece `sub` en la cadena.
- **`find(sub)`**: Devuelve el índice de la primera aparición de `sub`, o `-1` si no existe.
- **`index(sub)`**: Igual que `find`, pero lanza un error si no encuentra `sub`.
- **`startswith(prefix)` / `endswith(suffix)`**: Verifica si la cadena comienza o termina con el texto dado.

---

### 🔧 Métodos de modificación

- **`replace(old, new)`**: Reemplaza todas las apariciones de `old` por `new`.
- **`upper()` / `lower()`**: Convierte la cadena a mayúsculas o minúsculas.
- **`capitalize()`**: Convierte la primera letra en mayúscula.
- **`title()`**: Convierte la primera letra de cada palabra en mayúscula.
- **`strip()` / `lstrip()` / `rstrip()`**: Elimina espacios (o caracteres) al inicio y/o final.

---

### ✂️ Métodos de división y unión

- **`split(sep)`**: Divide la cadena en una lista usando el separador `sep`.
- **`join(lista)`**: Une los elementos de una lista en una sola cadena, usando el string como separador.

---

### ✅ Métodos de validación

- **`isalpha()`**: Verifica si todos los caracteres son letras.
- **`isdigit()`**: Verifica si todos los caracteres son dígitos.
- **`isalnum()`**: Verifica si todos los caracteres son alfanuméricos.
- **`isspace()`**: Verifica si todos los caracteres son espacios.

---

### 📌 Ejemplo práctico

```python
texto = "  Hola Mundo  "
print(texto.strip().upper())  # "HOLA MUNDO"
print(texto.find("Mundo"))    # 7
print(texto.replace("Mundo", "Python"))  # "  Hola Python  "
```

---

Yo usaría varios métodos de cadenas para procesar los datos que vienen de archivos `.txt` o `.csv`. Como cada línea que leo es una cadena, necesito limpiarla, dividirla y extraer lo que me interesa antes de graficar. Aquí te cuento cómo lo haría:

---

### 🧼 Primero limpio cada línea

Cuando leo una línea del archivo, suele venir con espacios o saltos de línea. Así que uso:

```python
linea = linea.strip()
```

Esto me deja la cadena lista para trabajar.

---

### ✂️ Luego la divido en partes

Si el archivo tiene datos separados por comas, como fechas, ciudades y temperaturas, uso:

```python
partes = linea.split(',')
```

Así obtengo una lista con cada dato por separado.

---

### 🔄 A veces reemplazo valores

Si encuentro valores como `"N/A"` o `"--"` que no sirven para graficar, los cambio por `"0"` o algo útil:

```python
linea = linea.replace('N/A', '0')
```

---

### 🔢 Verifico si los datos son válidos

Antes de convertir algo a número, me aseguro de que lo sea:

```python
if partes[2].isdigit():
    temperatura = float(partes[2])
```

---

### 📊 Y finalmente preparo los datos para graficar

Con los datos limpios, puedo usar Matplotlib para hacer gráficos de líneas, barras o lo que necesite.

---
