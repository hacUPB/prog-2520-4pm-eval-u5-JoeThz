import csv

datos1 = []
datos2 = []
datos3 = []
datos4 = []

datos = {'datos1': datos1, 'datos2': datos2, 'datos3': datos3, 'datos4': datos4}

with open("C:\\Users\\VICTUS\\Documents\\variables.csv", "r") as csvfile:
    lector = csv.reader(csvfile, delimiter=";") #se utiliza el metodo reader
    encabezado = next(lector)
    
    for fila in lector:     
        datos1.append(int(fila[0]))
        datos2.append(int(fila[1]))
        datos3.append(float(fila[2].replace(",",".")))
        datos4.append(float(fila[3].replace(",",".")))
i=0
for key, value in datos.items():
    print(encabezado[i])
    print(value)
    i += 1
    