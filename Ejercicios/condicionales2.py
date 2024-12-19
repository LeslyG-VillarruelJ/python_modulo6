import random

aleatorio = random.randint(1,9)
aleatorio2 = random.randint(1,9)

if aleatorio == 4:
    print("Te gansate un chupete")
elif aleatorio == 8:
    print("Te ganaste un balon")
elif aleatorio == 3 and aleatorio2 == 7:
    print("Te ganaste un televisor")
else:
    print("Persiste!!!!")