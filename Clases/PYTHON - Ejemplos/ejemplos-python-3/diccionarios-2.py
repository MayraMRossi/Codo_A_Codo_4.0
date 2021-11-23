'''
¿Qué es un Diccionario de datos?

'''
#Para definir un diccionario, se encierra el listado de valores entre llaves.
# Las parejas de clave y valor se separan con comas, y la clave y el valor se separan con dos puntos. 
diccionario = {'nombre': 'Carlos', 'edad': 22, 'cursos':  ['Python', 'Django', 'JavaScript']}

# Podemos acceder al elemento de un Diccionario mediante la clave de este elemento, 19 # como veremos a continuación:

print(diccionario['nombre']) #Carios
print(diccionario['edad']) #22
print(diccionario['cursos']) #[Python", 'Django", "JavaScript"]

# También es posible insertar uma lista dentro de un diccionario.
# Para acceder a cada uno de los cursos usamos los indices:
print(diccionario['cursos'][0]) #Python
print(diccionario['cursos'][1]) #Django
print(diccionario['cursos'][2]) #Javascript
# Para recorrer todo el Diccionario, podemos hacer uso de la estructura for:
for key in diccionario:
    print(key, ":", diccionario[key])