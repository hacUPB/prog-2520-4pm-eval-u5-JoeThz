ruta = "C:\\Users\\VICTUS\\Documents"
#"\" secuencia de escape: \n \t \ ---> para rutas usar "\\"
file_name = "Aviones1.txt"
modo = "x"
fp = open(ruta + "\\" + file_name, modo, encoding="utf-8")

nombre = input("Ingrese un nombre de un avión: ")
peso = int(input("Ingrese el peso de un avión: "))
velocidad = float(input("Velocidad máxima: "))
fp.write(nombre + "\n")
fp.write(str(peso)) #Los argumentos de write deben ser str
fp.write("\n")
fp.write(str(velocidad))
fp.write("\n")
#fp.write(nombre+"\n"+peso+"\n"+velocidad+"\n")
fp.close()