#CADENAS

print("************* CADENAS *************")
#Escritura y concatenación
cadena1 = "Juan Pablo"
cadena2= 'Con comillas simples'
print(cadena1) 
print(cadena2)
cadenaExtensa= 'Estamos estudiando "Python" ' \
    "el tema 'Cadenas de caracteres'"
print(cadenaExtensa)
print(cadenaExtensa + " con el profesor " + cadena1)

edad = 20
altura = 1.70
datos= "La edad es " + str(edad) + " y la altura es " + str(altura)
print(datos) 
print()

#Replicación de cadenas
print("- Replicación de cadenas")
risa='ja'
carcajada=risa*5
print(carcajada)
print("-"*10)
print()

#Comparación de cadenas (case sensitive)
print("- Comparación de cadenas")
ciudad= input("¿En qué Ciudad reside?: ")
if ciudad == "Córdoba":
    print("El envío llegará mañana")
else:
    print("El envío llegará pasado mañana")
print()

#Subíndices
print("- Subíndices")
dia="Hoy es Lunes"
print(dia[2])
print()

#Rebanadas
print("- Rebanadas")
# [:] Todos los elementos.
cadena="Aprendiendo Python"
print(cadena[:]) 
# [start:] Todos los elementos desde el índice establecido(start).
print(cadena[12:]) #Desde el 12
# [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
print(cadena[:3]) #No incluye pos 3
# [start:end] Todos los elementos de un rango de índices.
print(cadena[1:11]) #No incluye pos 11
# [start:end:step] Todos los elementos de un rango de índices con saltos.
print(cadena[1:11:2])