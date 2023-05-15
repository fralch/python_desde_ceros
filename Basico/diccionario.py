### DICCIONARIOS ###

# Diccionario: Estructura de datos que almacena un conjunto de datos de la forma clave:valor

my_dict = { "David": 35, "Erika": 32, "Jaime": 50 , "lenguajes": {"python", "js", "java"}, 1: "hola"}
# print(my_dict)

my_other_dict = dict( name="David", age=35, country="MX" )
# print(my_other_dict)

# obtener un valor del diccionario
# print(my_dict["David"])

# obtener un valor del diccionario
# print(my_dict.get("David"))

# set dict value
my_dict.setdefault("Pedro", 0)

#obtener items del diccionario (llave y valor)
# print(my_dict.items())

# obtener las llaves del diccionario (keys)
# print(my_dict.keys())

# obtener los valores del diccionario (values)
# print(my_dict.values())

# agregar un valor al diccionario (llave:valor)
my_dict["Jose"] = 70
# print(my_dict)

# eliminar un valor del diccionario por su llave
del my_dict["Pedro"]

#buscar un valor en el diccionario por su llave 
print("David" in my_dict)


# Limpiar el diccionario
my_dict.clear()

# Eliminar el diccionario
del my_dict

#transformar un diccionario en una lista
my_dict = { "David": 35, "Erika": 32, "Jaime": 50 }
print(list(my_dict.keys()))

#transformar una lista en un diccionario
my_list = [ "David", "Erika", "Jaime" ]
my_dict = dict.fromkeys(my_list, 0)
print(my_dict)
