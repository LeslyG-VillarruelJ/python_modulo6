# eliminar elementos
lista = [1, 2, 3, 4, 5, "Lesly", "Francisco", 1, 2, 3, 4, "Lesly"]

lista.pop() # elimina el ultimo elemento
lista.pop(3) # elimina el elemento de ese indice
lista.remove("Francisco") # eliminar el primer elemento 
lista.clear() #elimina toda la lista

print(lista)

lista2 = [9, 7, 3, 4, 6, 5, 2, 8]

lista2.sort() # ordenar la lista del menor al mayor
print(lista2)

lista2.reverse() # dar la vuelta ami lista es decir el ultimo será el primero y asi sucesivamente
print(lista2)

lista2.sort(reverse=True) # ordenar del mayor al menor
print(lista2)
