class Laptop:
    # creamos el constructor
    def __init__(self, marca, procesador, memoria, costo = 500, impuesto = 10):
        self.marca = marca # Es una autoreferencia, para crear los atributos de la instancia
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valor_final(self):
        return self.costo + self.impuesto
    
    def valor_descuento(self, descuento):
        return (self.costo * descuento)/100
    
    # metodos estáticos - no necesito instanciar mi clase
    @staticmethod
    def comparar_costo(laptop1, laptop2):
        if laptop1.costo == laptop2.costo:
            return "Los costos son iguales"
        else:
            return "Los costos son diferentes"
        
    # métodos de clase - modifica la clase para crear un objeto en específico
    @classmethod
    def asus_laptop(cls, costo): # cls - referencia a la propia clase
        marca = "Asus"
        procesador = "i5"
        memoria = 16
        return cls(marca, procesador, memoria, costo)