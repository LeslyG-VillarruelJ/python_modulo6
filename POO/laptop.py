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

# Instanciamos la clase
laptop_pepito = Laptop("lenovo", "17", 32)

print(laptop_pepito.__dict__) # imprimir los valores del objeto
print(laptop_pepito.valor_final())
print(f"El valor del descuento es: {laptop_pepito.valor_descuento(10)}")