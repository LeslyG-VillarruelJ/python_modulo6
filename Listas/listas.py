# Listas
planetas = ["Mercurio", "Venus", "Tierra", "Marte"]
print(planetas[3]) # un elemento de la lista
print(planetas[-2]) # desde el último elemento de la lista - podemos acceder a los elementos de la lista
# realizar - crear  sublista
print(planetas[1: 4]) # imprime el numero anterior al del segundo indice
# al dejar vacio el segundo indice nos permite imprimir desde el primer indice al ultimo
print(planetas[1:])
# imprimir la longitud de la lista
print(len(planetas))

# combinar valores en las listas
planetas2 = ["Mercurio", "Venus", "Tierra", "Marte", 3.45, True]

# LISTA DE NUMEROS 
gravedad_en_planetas = [0.378, 0.907, 1, 0.377] # en Newtons
peso_bus_tierra = 124054 #en Newtons
print(f"En la tierra un autobus pesa {peso_bus_tierra} en Newtons")
print(f"En Mercurio, un autobus pesa {peso_bus_tierra * gravedad_en_planetas[0]} N")

# VALORES MINIMOS Y MAXIMOS
print(f"Lo más liviano que seria un autobus en el autobus en el sisterma solar es {peso_bus_tierra * min(gravedad_en_planetas)}")
print(f"Lo más pesado que seria de un autobus en el sistema solar es {peso_bus_tierra * max(gravedad_en_planetas)}")