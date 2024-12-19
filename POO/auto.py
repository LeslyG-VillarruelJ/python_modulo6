import datetime

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
            return "Estoy como nuevo"
        elif self.kilometraje >= 20000 and self.kilometraje <= 100000:
            return"Ya estoy usado"
        else:
            return "¡Ya dejame descansar, por favor!"

    # metodo de clase
    @classmethod
    def toyota(cls):
        marca = "Toyota"
        modelo = "Hilux"
        año = datetime.datetime.now().year
        return cls(marca, modelo, año)
    
    @classmethod
    def kia(cls):
        marca = "KIA"
        modelo = "Picanto"
        año = 2024
        return cls(marca, modelo, año)
    
    # Método estático
    @staticmethod
    def comparar_estado_auto(auto1, auto2):
        if auto1.estado_auto == auto2.estado_auto:
            return "Ambos autos están en condiciones similares"
        else:
            return "Los autos tienen condiciones diferentes"
        
    @staticmethod
    def comparar_año_fabricacion(auto1, auto2):
        if auto1.año == auto2.año:
            return "Ambos autos han sido fabricados en el mismo años"
        elif auto1.año > auto2.año:
            return "El segundo auto ha sido fabricado antes que el primero"
        elif auto1.año < auto2.año:
            return "El primer auto ha sido fabricado antes que el segundo auto"