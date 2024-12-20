import random
from laptop import Laptop

class Laptop_Bussiness(Laptop):
    def __init__(self, marca, procesador, memoria, espacio_disco, duracion_bateria, costo = 500, impuesto = 10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.espacio_disco = espacio_disco
        self.duracion_bateria = duracion_bateria

    def __str__(self):
        return f"Marca: {self.marca}\nProcesador: {self.procesador}\nMemoria: {self.memoria}\nEspacio memoria: {self.espacio_disco}\nDuración batería: {self.duracion_bateria}\nPrecio: {self.costo}"

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_espacio_disco = "No hay espacio en disco, elimine algunos archivos" if self.espacio_disco == 0 else "OK"
        resultado_diagnostico["ESPACIO DISCO"] = resultado_espacio_disco
        resultado_conectividad = self.verificar_conectividad_red()
        resultado_diagnostico["RESULTADOS CONECTIVIDAD"] = resultado_conectividad
        return resultado_diagnostico
    
    def verificar_conectividad_red(self):
         # Simulación de la disponibilidad de Wi-Fi (True si está disponible, False si no)
        disponibilidad_wifi = random.choice([True, False])
    
        # Simulación de acceso a servidores empresariales (True si hay acceso, False si no)
        acceso_servidores = random.choice([True, False])
        
        # Simulación de latencia de la red (True si la latencia es aceptable, False si es alta)
        latencia_red = random.choice([True, False])
        
        # Crear el diccionario con los resultados de la conectividad
        resultados_conectividad = {
            "disponibilidad_wifi": disponibilidad_wifi,
            "acceso_servidores_empresariales": acceso_servidores,
            "latencia_red": latencia_red
        }
    
        return resultados_conectividad

    pass