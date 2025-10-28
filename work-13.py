import matplotlib.pyplot as plt
import numpy as np
import math

# Datos
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 12]

# Crear la gráfica de barras
plt.bar(categorias, valores, color=["#B80606", "#F6FF00", "#000000", "#FFFFFF"])

# Agregar título y etiquetas
plt.title('Gráfica de Barras')
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Mostrar la gráfica
plt.show()
