# Ejercicio

# 1. Crear una variable "tupla" que sea una tupla de los siguientes nombres: Antonio, Pedro y Maria.

tupla = ('Antonio','Pedro','Maria')

# 2. Mostrar el valor de la variable "tupla".

print(tupla)

# 3. Recoger un valor dato por teclado y almacenarlo en la variable "dato".

dato = input()

# 4. Si el valor de "dato" está dentro de los valores de la variable "tupla", mostrar "Si".

if(dato in tupla):
	print("Si")

# 5. Si el valor de "dato" no está dentro de los valores de la variable "tupla", mostrar "No".

if(dato not in tupla):
	print("No")