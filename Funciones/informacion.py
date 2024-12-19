from datetime import datetime

nombre_paciente = []
def agregar_nombre(nombre, apellido):
    nombre_completo = nombre + " " + apellido
    nombre_paciente.append(nombre_completo)

edad = []
def agregar_edad(año_nacimiento):
    edad_actual = datetime.now().year - año_nacimiento
    edad.append(edad_actual)