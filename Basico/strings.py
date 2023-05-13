## Aprendiendo Strings en python ##
my_string = "Hola mundo"
my_other_string = "Mi nombre es Juan"
print(len(my_string))

print (my_string +" "+my_other_string)
print (my_string, my_other_string)

#salto de linea
salto = "Hola mundo\nMi nombre es Juan"
print(salto)

#tabulacion
tabulacion = "\t Hola mundo mi nombre es Juan"
print(tabulacion)

#formateo de strings
nombre = "Juan"
apellido = "Perez"
edad = 30 
print("Mi nombre es {} {} y tengo {} años".format(nombre, apellido, edad))
print("Mi nombre es {0} {1} y tengo {2} años".format(nombre, apellido, edad))
print("Mi nombre es {2} {1} y tengo {0} años".format(nombre, apellido, edad))
print("Mi nombre es {n} {a} y tengo {e} años".format(n=nombre, a=apellido, e=edad)) 
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años")
print ("Mi nombre es %s %s y tengo %d años" % (nombre, apellido, edad))

#desempaquetado de strings
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b) 

#slicing o rebanado de strings
language = "Python"
print(language[0]) 
print(language[1:4])
print(language[-2])
print(language[::-1])

#funciones de strings
texto = "Hola mundo"

#mayusculas en la primera letra
texto.capitalize()
#mayusculas en todas las letras
texto.upper()
# minusculas en todas las letras
texto.lower()
#mayusculas en la primera letra de cada palabra
texto.title()
#reemplazar una palabra por otra
texto.replace("Hola", "Adios")
#contar cuantas veces se repite una palabra
texto.count("o")
# es un string numerico
texto.isnumeric()
"123".isnumeric()
# es un string alfabetico
texto.isalpha()
# esta en mayusculas
texto.isupper()
# esta en minusculas
texto.islower()
# esta en mayusculas la primera letra
texto.istitle() 
#empienza con una palabra
texto.startswith("Hola") 
 
# separar un string por un caracter 
texto.split(" ")
