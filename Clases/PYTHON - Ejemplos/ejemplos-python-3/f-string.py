legajo= 12212
nombre= "María"
nota= 10
#%-formato
print("Legajo: %d Nombre: %s Nota: %d" %(legajo,nombre,nota))
print("Legajo: {} Nombre: {} Nota: {}".format(legajo,nombre,nota))
# En ambos casos devuelve:
# Legajo: 12212 Nombre: María Nota: 10

#f-string
print(f"Legajo: {legajo} Nombre: {nombre} Nota: {nota}")
# Legajo: 12212 Nombre: María Nota: 10