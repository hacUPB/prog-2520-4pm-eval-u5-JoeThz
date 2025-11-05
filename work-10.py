try:
    #entero = int(input("Ingresa un número: "))
    lista =[1,2,3]
    print(lista[5])
except Exception as e:
    print(f"ocurrió un error tipo {e}")
except ValueError:
    print("Error: Debes ingresar un número valido.")
else:
    print("La operación se realizó correctamente.")
finally:
    print("Puedes continuar con el programa.")