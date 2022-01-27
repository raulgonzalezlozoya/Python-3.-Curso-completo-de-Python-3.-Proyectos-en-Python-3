# Ejercicio

# Crear una variable "minimo" con el valor 20.

minimo = 20

# Crear una variable "maximo" con el valor 500.

maximo = 500

# Recoge un valor del teclado y almacénalo en la variable "dato".

dato = imput()

# Convierte la variable "dato" en un número y almacénalo en la variable "numero".

numero = int(dato)

# Si el "numero" es menor que el valor "minimo", mostrar el texto "Valor bajo".

if (numero < minimo):
	print("Valor bajo")
	

# Si el "numero" es mayor que el valor de "maximo", mostrar el texto "Valor alto".

if (numero > maximo):
	print("Valor alto")

# Si el valor "numero" está entre el valor de "minimo" y "maximo", mostrar "Valor medio".

if (numero > minimo) and (numero < maximo):
	print("Valor medio")