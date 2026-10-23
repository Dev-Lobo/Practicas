import random

nrandom = random.randint(1, 10)
nusuario = ""

while nusuario != nrandom:
    nusuario = int(input("Intenta adivinar el numero: "))
    if nusuario != nrandom:
     print("Ese no era el numero, intentalo de nuevo")
    elif nusuario == nrandom:
       print("¡Has adivinado el numero!")
       break
    