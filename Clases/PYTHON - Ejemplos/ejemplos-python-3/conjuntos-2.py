# Crea un conjunto con una serie de elementos entre llaves
# Los elementos repetidos se eliminan
c = {1, 3, 2, 9, 3, 1}
print(c) #{1, 2, 3, 9}

# Crea un conjunto a partir de un string
# Los caracteres repetidos se eliminan
a = set('Hola Pythonista')
print(a) #{'y', 'P', 'h', 'i', 's', 'H', 'n', 't', 'l', 'o', ' ', 'a'}

# Crea un conjunto a partir de una lista
# Los elementos repetidos de la lista se eliminan
unicos = set([3, 5, 6, 1, 5])
print(unicos) #{1, 3, 5, 6} 

#Acceso:
mi_conjunto = {1, 3, 2, 9, 3, 1}
for e in mi_conjunto:
    print(e, end=' ')

