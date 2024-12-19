from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_bussiness import Laptop_Bussiness

# Instanciamos la clase
laptop_pepito = Laptop("lenovo", "17", 32)
laptop_maria = Laptop("lenovo", "17", 32, 600)


print(laptop_pepito.__dict__) # imprimir los valores del objeto
print(laptop_pepito.valor_final())
print(f"El valor del descuento es: {laptop_pepito.valor_descuento(10)}")

# test metodos estáticos
print(Laptop.comparar_costo(laptop_pepito, laptop_maria))

#test metodo de clase - se requiere 1000 laptop
for numero in range(1, 1001):
    asus_laptop = Laptop.asus_laptop(numero)
    print(asus_laptop.__dict__)

# Herencia
laptop_juanito = Laptop_Gaming("MSI", "i7", 4, "RTX 8GB")
print(laptop_juanito.costo)
print(laptop_juanito.realizar_diagnostico_sistema())

# laptop_bussiness - duracion baterias en horas
laptop_lesly = Laptop_Bussiness("MSI", "i7", 4, 0, 3)
print(laptop_lesly.realizar_diagnostico_sistema())