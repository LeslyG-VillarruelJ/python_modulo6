from auto import Auto

# Instanciación de un Auto
# TEST
auto1 = Auto("KIA", "RIO", 2021)
auto1.mostrar_información()
auto1.actualizar_kilometraje(1000)
auto1.realizar_viaje(500)
auto1.estado_auto()

# Test método de clase
auto2 = Auto.toyota()
print(auto2.__dict__)
auto3 = Auto.kia()
print(auto3.__dict__)

# Test metodos estáticos
print(Auto.comparar_estado_auto(auto1, auto2))
print(Auto.comparar_año_fabricacion(auto1, auto3))