#LISTAS

#Creación e impresión de listas
print("************* LISTAS *************")
mundialesFutbol= [1998,2002,2006,2010,2014,2018] #Lista de números
apellidos= ["García", "López", "Rodríguez"] #Lista de strings
listaVacia= [] #Lista vacía
listaAnidada= [[1,3,5],[2,4,6]] #Listas anidadas
print(mundialesFutbol)
print(apellidos)
print(listaVacia)
print(listaAnidada) 
print()

#Acceso a elementos
print("*** Acceso a elementos ***")
print(mundialesFutbol[0]) #Primero
print(mundialesFutbol[-1]) #Último
print(mundialesFutbol[3]) #Cuarto (recordemos empieza en 0)
# print(listaVacia[1]); #Error out of range
# print(apellidos[4]); #Error out of range
print(listaAnidada[0]) 
print(listaAnidada[0][1])
print()

#Iteramos sobre una lista
print("*** Iterando listas ***")
vocales=['a','e','i','o','u']
print("- Con For:")
for i in vocales:
    # print(i, end="-")
    print(i)

print("- Con While:")
i=0
while i < len(vocales):
    # print(vocales[i], end="-")
    print(vocales[i])
    i+=1
print()

#Desempaquetado de listas
print("*** Desempaquetado de listas ***")
animales= ["Perro", "Gato", "Tortuga"] 
ani1, ani2, ani3 = animales #Dsempaquetamos: asignamos a cada variable un elemento de la lista
print(ani1)
print(ani2)
print(ani3)

listaAnidada= [[1,3,5],[2,4,6]] #Listas anidadas
lista1, lista2 = listaAnidada #Desempaquetamos las listas
print(lista1)
print(lista2)
v1L1, v2L1, v3L1 = lista1 #Desempaquetamos la primer lista
print(v1L1)