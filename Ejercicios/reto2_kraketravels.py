# KRAKETRAVELS
import sys # para terminar el programa
# variables
print("*** Viaja con KrakeTravels ***")
lugar = (input("¿A qué país se dirige, *** Colombia, Ecuador o Perú ***? "))
zona = (input("¿En qué zona se encuantra, *** urbana, rural o perimetral ***? "))
velocidad = int(input("¿A qué velocidad en km/h se encuentra? "))

# validaciones
if lugar == "Ecuador":
    if zona == "urbana":
        velocidad_maxima = 50
        velocidad_minima = 10
    elif zona == "rural":
        velocidad_maxima = 70
        velocidad_minima = 51
    elif zona == "perimetral":
        velocidad_maxima = 90
        velocidad_minima = 71
    else:
        print("Ha ingresado mal la zona.")
elif lugar == "Colombia":
    if zona == "urbana":
        velocidad_maxima = 30
        velocidad_minima = 10
    elif zona == "rural":
        velocidad_maxima = 80
        velocidad_minima = 31
    elif zona == "perimetral":
        velocidad_maxima = 100
        velocidad_minima = 81
    else:
        print("Ha ingresado mal la zona.")
elif lugar == "Perú":
    if zona == "urbana":
        velocidad_maxima = 40
        velocidad_minima = 10
    elif zona == "rural":
        velocidad_maxima = 60
        velocidad_minima = 41
    elif zona == "perimetral":
        velocidad_maxima = 120
        velocidad_minima = 61
    else:
        print("Ha ingresado mal la zona.")
else:
    print("El país está mal ingresado")
    sys.exit()
    
# validacion de personal
if velocidad >= velocidad_maxima:
    print("Está yendo a exceso de velocidad")
elif velocidad <= velocidad_minima: 
    print("Está yendo a una velocidad menor al límite de velocidad mínima")
else:
    print("Se encuentra conduciendo a una velocidad óptima")
