#CADENAS: FUNCIONES

print("******* CADENAS: FUNCIONES *******")

#Longitud de cadenas
print("- Longitud de cadenas")
dia="Lunes"
print(len(dia))
print()

#In - Not in
print("- In / Not In")
cad="Cadenas en Python"
cadenaBuscada= "nas"
print(cad)
if cadenaBuscada in cad:
    print(cadenaBuscada, "se encuentra en la cadena")
else:
    print(cadenaBuscada, "NO se encuentra en la cadena")

cadenaBuscada= "JAVA"
if "JAVA" not in cad:
    print(cadenaBuscada, "NO se encuentra en la cadena")
else:
    print(cadenaBuscada, "se encuentra en la cadena")
print()

#Iteraciones
print("- Iteraciones (For)")
cad="Python"
for letra in cad:
    print(letra)

print("- Iteraciones (While)")
i=0
while i < len(cad):
    print(cad[i])
    i+=1
print()

#Maximo y mínimo
print("- Max y min")
cad="JavaScript"
print(max(cad))
print(min(cad)) #Van por código ASCII https://elcodigoascii.com.ar/
print()

#Count e Index
print("- Count e Index")
cad="Cadenas de caracteres"
print(cad.count("c")) #2, no 3 porque es sensible a mayúsculas
print(cad.index("de")) #2
print(cad.index("de",3)) #8, desde pos 3