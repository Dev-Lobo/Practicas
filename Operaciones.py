# Operaciones.py
# - Pedir dos números desde la terminal
# - Imprimir por pantalla la suma, la resta, la multiplicación y la división (decimal) de ambos números

num1 = float(input("¿Primer numero? "))
num2 = float(input("¿Segundo numero? "))

def suma(a, b): # Suma
    return a + b

def resta(a, b): # Resta
    return a - b

def multiplicacion(a, b): # Multiplicación
    return a * b

def division(a, b): # División
    return a / b

print("Suma:",suma(num1, num2), "Resta:",resta(num1, num2), "Multiplicación:",multiplicacion(num1, num2), "División:",division(num1, num2))