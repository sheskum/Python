# variables

"""
Es un espacio en memoria para almacenar datos modificables

Tiene ciertas reglas:

* Debe comenzar por letra o underscor _
* No puede comenzar por un numero
* Solo puede contener caracteres alfanumericos y guion bajo
"""

# Forma correcta

#first_name = "juan"
#age = 45
#_nationality = "Venezuela"

# Forma incorrecta

'''
last-name
last@place
last$age
num-1
1num

'''
# examples

first_name = "Marwin"
country = "Venezuela"
age = 35

print("Hola ", first_name)
print("Donde vives: ", country)
print(len(country))

# variables en una sola linea

print(first_name, country, age)

# Tipos de datos

a = "Hola"  # str
b = 7       # int
c = 15.2    # float
d = 2 + 2j  # complex
e = [1, "hi", 3.5]  # list
f = (2, 2.3, "hi")  # tuple
g = {"name": "maria", "age": "25"}  # dict

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))
print(g)
print(type(g))

# convertir de un tipo a otro

number_int = 10
number_float = 17.2
number_str = "15"
number_list = "python"

#converti de entero a float
print(float(number_int))

# de float a entero
print(int(number_float))

# de str a int o float

print(int(number_str))
print(float(number_str))

# de str a lista

print(list(number_list))