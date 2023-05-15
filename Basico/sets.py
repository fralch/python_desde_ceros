### SETs ###

# Los sets son colecciones desordenadas de elementos unicos e inmutables

my_set = {1, 2, 3, 4, 5, 5, 5} # No se repiten los valores
# print(my_set)

my_other_set = set([1, 2, 3, 4, 5, 5, 5]) # No se repiten los valores
# print(my_other_set)
# print(type(my_set))


# Agregar un elemento al set
my_set.add(6)
# print(my_set)

# Eliminar un elemento del set
my_set.remove(6)

# Eliminar un elemento del set
my_set.discard(6)

# Eliminar un elemento del set
my_set.pop()

# Limpiar el set
my_set.clear()

# Eliminar el set
del my_set

# Operaciones con sets

# Union
my_set = {1, 2, 3, 4, 5}
my_other_set = {4, 5, 6, 7, 8}

# print(my_set | my_other_set)
# print(my_set.union(my_other_set))

# Interseccion
print(my_set & my_other_set)
print(my_set.intersection(my_other_set))


# Diferencia: Elementos que estan en un set pero no en el otro
print(my_set - my_other_set)
print(my_set.difference(my_other_set))

# Diferencia simetrica: Elementos que estan en un set o en el otro pero no en ambos
print(my_set ^ my_other_set)
print(my_set.symmetric_difference(my_other_set))

# Subsets: Saber si un set es un subconjunto de otro set
print(my_set <= my_other_set)
print(my_set.issubset(my_other_set))

#comprobar si un elemento esta en un set
print(1 in my_set)



