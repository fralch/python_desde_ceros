# listas o arrays

my_list = ["Hola", "Mundo", "Python", "Hola"]
other_list = list(["Hola", "Mundo", "Python"])
datos_usuario = ["Juan", "Perez", 30]

nombre, apellido, edad = datos_usuario #desempaquetado de listas

print(nombre)

print(my_list)
print(other_list)
print (my_list[0])
print(my_list.count("Hola")) #cuenta cuantas veces se repite un elemento

#slicing o rebanado de listas
print("Slicing o rebanado de listas")
print(my_list[0:2])
print(my_list[0:4:2])

#revertir una lista
my_list.reverse()
print(my_list)

#añadir un elemento al final de la lista
my_list.append("Juan")
print(my_list)

#insertar un elemento en una posicion especifica
my_list.insert(1, "Adios")
print(my_list)

#eliminar un elemento de la lista
my_list.remove("Adios")

#eliminar el ultimo elemento de la lista
my_list.pop()

#eliminar un elemento de la lista por su indice
my_list.pop(1)

#eliminar todos los elementos de la lista
my_list.clear()

#ordenar una lista
my_list = [1, 5, 3, 2, 4]
my_list.sort()

#ordenar una lista de forma inversa
my_list.sort(reverse=True)

#obtener el indice de un elemento
print(my_list.index(3))

#obtener la longitud de una lista
print(len(my_list))

#copiar una lista
my_list_copy = my_list.copy()

#unir dos listas
my_list.extend(other_list)

# Path: listas.py
# Compare this snippet from operadores.py:
# En la lista o array
print(10 in [1, 2, 3, 4, 5])
# No en la lista o array
print(10 not in [1, 2, 3, 4, 5])



#unir dos listas
my_list.extend(other_list)
print(my_list)
