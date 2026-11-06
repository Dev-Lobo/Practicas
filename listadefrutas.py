frutas = ['apple', 'banana', 'pear'] # Crear lista

frutas.append('watermelon') # Añadir elemento watermelon al final

print(frutas) # Imprimir la lista

frutas.insert(1,'strawberry') # Añadir "Strawberry" en la segunda posición

print(len(frutas)) # Imprimir cuantos elementos hay en la lista

for fruta in frutas: # Imprimir cada elemento por linea
    print(fruta)

frutas.remove('pear') # Eliminar pear

for posicion, fruta in enumerate(frutas): # Imprimir en que posicion esta banana
    if fruta == 'banana':
        print(posicion)

frutas.sort() # Imprimir la
print(frutas) # lista final ordenada
