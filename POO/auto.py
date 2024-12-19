class Auto:
    def __init__(self, marca, modelo, año, kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def mostrar_información(self):
        return print(f"Auto --> marca: {self.marca}, modelo: {self.modelo}, año: {self.año}")
    
    def actualizar_kilometraje(self, kilometraje):
        if self.kilometraje < kilometraje:
            self.kilometraje = kilometraje
            print(f"Mi kilometraje actual es: {self.kilometraje}")
        else:
            print("El kilometraje proporcionado es menor al actual. No se puede reducir el kilometraje")

    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
            print(f"Mi kilometraje actual es: {self.kilometraje}")
        else:
            print("Los kilometros deben ser positivos")

    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif self.kilometraje >= 20000 and self.kilometraje <= 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya dejame descansar, por favor!")
    
# Instanciación de un Auto
# TEST
auto1 = Auto("KIA", "RIO", 2021)
auto1.mostrar_información()
auto1.actualizar_kilometraje(1000)
auto1.realizar_viaje(500)
auto1.estado_auto()