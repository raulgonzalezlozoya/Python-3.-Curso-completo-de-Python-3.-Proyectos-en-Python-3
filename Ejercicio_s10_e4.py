# Ejercicio

# 1. Crear una variable "diccionario" con los pares de valores siguientes:
#	clave=uno    valor=one
#	clave=dos    valor=two
#   clave=tres   valor=three

diccionario = {"uno":"one","dos":"two","tres":"three"}

# 2. Mostrar por pantalla el valor de la variable "diccionario".

print(diccionario)

# 3. Añadir un nuevo elemento al diccionario:
#	clave=cuatro  valor=four

diccionario["cuatro"] = "four"

# 4. Mostrar ahora el valor del diccionario.

print(diccionario)

# 5. Recoger un valor introducido por teclado y almacenarlo en "dato".

dato = input()

# 6. Utilizar "dato" como clave del diccionario para recuperar su valor.

valor = diccionario[dato]
print(valor)