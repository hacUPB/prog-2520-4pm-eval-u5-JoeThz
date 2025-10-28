import matplotlib.pyplot as plt
import numpy as np
import math

# Datos
# x = np.linspace(0, 10, 100)
# y = np.sin(x)

x = []
y = []

for i in range(100):
    dato = i/100
    x.append(dato)

for j in range(len(x)):
    dato = math.cos(2*math.pi*x[j])
    y.append(dato)

# x = [1, 3, 45, 67, 8, 10]
# y = [3, 5, 87, 2, 33, 44]

# Crear la gráfica
plt.scatter(x, y, )

# Agregar título y etiquetas
plt.title('Gráfica de Seno')
plt.xlabel('X')
plt.ylabel('sin(X)')

# Mostrar la gráfica
plt.show()