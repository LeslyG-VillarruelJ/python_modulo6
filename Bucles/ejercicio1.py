# BUCLES
lista = [1, 2, 3, 4, 5, "Lesly", "Francisco", 1, 2, 3, 4, "Lesly"]

for i in lista:
    print(i) # con salto de linea

for i in lista:
    print(i, end=(", ")) # sin salto de linea

# saber que elemento está dentro de mi lista
elemento = "Lesly"
for i in lista:
    if elemento == i:
        print(f"El elemento {elemento} está dentro de la lista")