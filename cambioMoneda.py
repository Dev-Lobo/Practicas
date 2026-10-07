cantidad = float(input("Introduce la cantidad a cambiar en euros: "))

print("Selecciona la divisa de destino:")
print("1. Dólares estadounidenses (USD)")
print("2. Libras esterlinas (GBP)")
print("3. Yenes japoneses (JPY)")
print("4. Francos suizos (CHF)")

opcion = int(input("Elige una opción (1-4): "))

if opcion == 1:
    cambio = cantidad * 1.09
    moneda = "USD"
elif opcion == 2:
    cambio = cantidad * 0.85
    moneda = "GBP"
elif opcion == 3:
    cambio = cantidad * 157.68
    moneda = "JPY"
elif opcion == 4:
    cambio = cantidad * 0.96
    moneda = "CHF"
else:
    print("Opción no válida.")
    exit()

print(f"{cantidad:.2f} EUR equivalen a {cambio:.2f} {moneda}.")
