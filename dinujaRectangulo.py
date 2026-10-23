ancho = int(input("¿Cual es el ancho de tu rectangulo? -> "))
alto = int(input("¿Cual es el alto de tu rectangulo? -> "))

for x in range(alto):
    for y in range(ancho):
        print("*", end="")
    print()