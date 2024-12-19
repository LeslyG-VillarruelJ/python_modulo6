# AGREGAR ELEMENTOS A UNA LISTA
lista = [1, 2, 3, 4, 5, 6]
lista.append(7) # agregar un elemento a la lista al final de la lista
print(lista)
# agregar elemento en la posicion que se quiera
lista.insert(2, "Lesly")
print(lista)
# Agregar una lista de elementos a la lista ya existente
lista.extend([8, 9, 10])
print(lista)
lista2 = [6, 7, 8, 9]
lista3 = lista + lista2 # concatenar las listas
print(lista3)