'''
# Cadenas de caracteres
diaDeSemana="Lunes"
diaFinDeSemana='Domingo'
print(diaDeSemana+diaFinDeSemana)
print(diaDeSemana,diaFinDeSemana)
'''

'''
apellido="Martínez"
print(apellido[0])
print(len(apellido))
posUltimoCaracter = len(apellido)-1 #Es -1 porque arranca de 0.
print(apellido[posUltimoCaracter])
'''
'''
cadena= input("Ingrese su nombre:")
posUltimoCaracter = len(cadena)-1
print("Primer caracter", cadena[0])
print("Último caracter", cadena[posUltimoCaracter])
print("Largo de la cadena", len(cadena))
'''

apellido="Martínez"
print(apellido.lower()) #minúsculas
print(apellido.upper()) #mayúsculas
apellido="martínez"
print(apellido.capitalize()) #primer letra de la cadena

nombre="CARLOS"
apellido="rodriguez"
print(nombre.capitalize(), apellido.capitalize())
'''


apellido="Martínez"
if apellido[0]=="M":
    print(apellido)
    print("Comienza con M")

print(len(apellido)) # 8
print(apellido.lower()) #martínez
print(apellido.upper()) #MARTÍNEZ
nombre="carlos"
print(nombre.capitalize()) #Carlos
nombre= nombre.capitalize()
print(nombre, apellido) #Carlos Martínez
'''