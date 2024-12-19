import emoji

cantidad_frase = int(input("Cuantas frases desea ingresar: "))
for i in range(cantidad_frase):
    frase = input("Ingrese una frase: ")
    emoji.encontrar_palabra(frase)
    emoji.agragar_frase(frase)