# Ejercicio

# 1.- Crear una variable "cadena" que contiene el texto "Esto es un texto de ejemplo".

cadena = "Esto es un texto de ejemplo"
print(cadena)

# 2.- Crear una variable "longitud" que contiene la longitud de la variable "cadena".

longitud = len(cadena)
print(longitud)

# 3.- Crear una variable "strlongitud" que tenga el valor de "longitud" pero convertida en cadena de caracteres o string.

strlongitud = str(longitud)
print(strlongitud)

# 4.- Crear una variable "mayusculas" que contiene la variable "cadena" en mayusculas.

mayusculas = cadena.upper()
print(mayusculas)

# 5.- Crear una variable "resultado" que concatene "mayusculas" con el texto " tiene longitud de " y "strlongitud".

resultado = mayusculas + " tiene longitud de " + strlongitud
print(resultado)