#LISTAS

#Operaciones sobre listas
print("******* OPERACIONES SOBRE LISTAS *******")
print("- Concatenar:")
paises= ["Argentina", "Uruguay", "Brasil"]
ciudades= ["Buenos Aires", "Montevideo", "San Pablo"]
todos=paises + ciudades
print(todos)
print(paises + ["Venezuela"]) #Concatena, no agrega
print(paises) #No fue agregado Venezuela
print()

#Modificar valores por posición
print("- Modificar valores por posición:")
print(paises) #Original
paises[2]="Chile"
print(paises) #Cambiada
print()

#Cantidad de elementos
print("- Cantidad de elementos:")
print("Cantidad de ciudades:", len(ciudades))
print()

#Operaciones con listas numeradas
print("- Suma, máximo, mínimo y promedio:")
notas= [3,10,9,8,7,5]
print("Notas:", notas)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas)) 
print("Suma de notas:", sum(notas))
print("Promedio:", (sum(notas)/len(notas)))
print()

#list / in - not in
print("- list / in - not in:")
cadena=list("Juan Pablo")
print(cadena)
numeros=list(range(4))
print(numeros)
print("n" in cadena)
print(4 in numeros)
print("x" not in cadena)
print("u" not in cadena) 