#Aprendiendo operadores de python

# Operadores aritmeticos
print("Operadores aritmeticos")
# Suma
print(10 + 5)
# Resta
print(10 - 5)
# Multiplicacion
print(10 * 5)
# Division
print(10 / 5)
# Modulo
print(10 % 5)
# Exponente
print(10 ** 5)
# Division entera
print(10 // 5)

# Multiplicacion de cadenas
print("Hola " * 5)

# Operadores de asignacion
print("Operadores de asignacion")
# Asignacion
x = 5
# Suma
x += 3
# Resta
x -= 3
# Multiplicacion
x *= 3
# Division
x /= 3
# Modulo
x %= 3
# Exponente
x **= 3
# Division entera
x //= 3

# Operadores de comparacion
print("Operadores de comparacion")
# Igualdad
print(10 == 5)
# Desigualdad
print(10 != 5)
# Mayor que
print(10 > 5)
# Menor que
print(10 < 5)
# Mayor o igual que
print(10 >= 5)
# Menor o igual que
print(10 <= 5)
# En el rango
print(10 in range(1, 11))
# No en el rango
print(10 not in range(1, 11))
# En la lista o array
print(10 in [1, 2, 3, 4, 5])
# No en la lista o array
print(10 not in [1, 2, 3, 4, 5])
# En el diccionario o map
print("nombre" in {"nombre": "Juan", "apellido": "Perez"})
# No en el diccionario o map
print("nombre" not in {"nombre": "Juan", "apellido": "Perez"})
# En el conjunto o set
print(10 in {1, 2, 3, 4, 5})
# No en el conjunto o set
print(10 not in {1, 2, 3, 4, 5})
# En el string
print("a" in "Hola Mundo")
# No en el string
print("a" not in "Hola Mundo")


# Operadores logicos}
print("Operadores logicos")
# AND
print(10 == 5 and 10 > 5)
print(10 == 5 & 10 > 5)
# OR
print(10 == 5 or 10 > 5)
print(10 == 5 | 10 > 5)
# NOT
print(not 10 == 5)
print(~10 == 5)
# XOR
print(10 == 5 ^ 10 > 5)
# Desplazamiento a la izquierda
# Explicacion: 10 en binario es 1010 y al desplazarlo a la izquierda 2 veces  se obtiene 101000 que en decimal es 40
print(10 << 2)
# Desplazamiento a la derecha
# Explicacion: 10 en binario es 1010 y al desplazarlo a la derecha 2 veces  se obtiene 10 que en decimal es 2
print(10 >> 2)
# AND bit a bit
# Explicacion: 10 en binario es 1010 y 5 en binario es 0101 y al aplicar el operador AND bit a bit se obtiene 0000 que en decimal es 0
print(10 & 5)
# OR bit a bit
# Explicacion: 10 en binario es 1010 y 5 en binario es 0101 y al aplicar el operador OR bit a bit se obtiene 1111 que en decimal es 15
print(10 | 5)
# XOR bit a bit
# Explicacion: 10 en binario es 1010 y 5 en binario es 0101 y al aplicar el operador XOR bit a bit se obtiene 1111 que en decimal es 15
print(10 ^ 5)
# NOT bit a bit
# Explicacion: 10 en binario es 1010 y al aplicar el operador NOT bit a bit se obtiene 0101 que en decimal es 5
print(~10)




# Operadores de identidad
print("Operadores de identidad")
# is
x = 5
y = 5
print(x is y)
# is not
x = 5
y = 5
print(x is not y)

# Operadores de membresia
print("Operadores de membresia")
# in
#explicacion: el operador in verifica si un elemento se encuentra en una lista o array
x = 5
y = [1, 2, 3, 4, 5]
print(x in y)
# not in
#explicacion: el operador not in verifica si un elemento no se encuentra en una lista o array
x = 5
y = [1, 2, 3, 4, 5]
print(x not in y)
# is
#explicacion: el operador is verifica si dos variables apuntan al mismo objeto en memoria
x = 5
y = [1, 2, 3, 4, 5] 
print(x is y)
# is not
#explicacion: el operador is not verifica si dos variables no apuntan al mismo objeto en memoria
x = 5
y = [1, 2, 3, 4, 5]
print(x is not y)

