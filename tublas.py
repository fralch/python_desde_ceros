### TUPLAS 
# la diferencia entre una tupla y una lista es que la tupla es inmutable o constante

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

my_other_tuplae = tuple([1, 2, 3, 4, 5])
print(my_other_tuplae)

my_tuple[0] = 10 # Error NO se puede modificar una tupla es inmutable o constante

#unir dos tuplas
my_tuple = my_tuple + my_other_tuplae
print(my_tuple)

# slice o rebanado
print(my_tuple[0:2])

# convetir una tupla en una lista
my_list = list(my_tuple)

# convertir una lista en una tupla
my_tuple = tuple(my_list)

#borrar una tupla
del my_tuple