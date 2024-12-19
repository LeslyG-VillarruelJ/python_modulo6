import informacion

cantidad_pacientes = int(input("Cuantos pacientes desea ingresar: "))
for i in range(cantidad_pacientes):
    nombre_paciente = input(f"Ingrese nombre del paciente {i+1}: ")
    apellido_paciente = input(f"Ingrese apellido del paciente {i+1}: ")
    edad_paciente = int(input(f"Ingrese el año de nacimiento del paciente {i+1}: "))
    # ingresar paciente y edad
    informacion.agregar_nombre(nombre_paciente, apellido_paciente)
    informacion.agregar_edad(edad_paciente)

print(informacion.nombre_paciente)
print(informacion.edad)

edad_mayor = informacion.edad[0]
nombre = informacion.nombre_paciente[0]
for indice,ed in enumerate(informacion.edad):
    if ed > edad_mayor:
        edad_mayor = informacion.edad[indice]
        nombre = informacion.nombre_paciente[indice]

print(f"{nombre} con la edad de {edad_mayor} años es mayor a los demás pacientes")
