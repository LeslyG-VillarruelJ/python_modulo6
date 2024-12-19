# INGRESAR DATOS
cantidad_datos = int(input("Ingrese la cantidad de datos que desee ingresar: "))

datos = []

print("Ingrese cada uno de los datos")

for i in range(cantidad_datos):
    dato = input(f"Ingrese dato {i + 1}: ")
    type = ""
    try:
        int(dato)
        type = "entero"
    except ValueError:
        try:
            float(dato)
            type = "decimal"
        except ValueError:
            type = "string"
    print(type)
    datos.append(dato)

print(f"Su lista es: {datos}")