#LISTAS

# MÉTODOS PARA LISTAS
print("******* MÉTODOS PARA LISTAS *******")

#Append / Insert
print("- Append / Insert:")
autores= ["Cortázar", "Borges", "Sábato"]
musicos= ["León Gieco", "Fito Páez", "Carlos Gardel"]
autores.append("Bioy Casares") #Agrega al final
print(autores)

musicos.insert(0, "Charly García") #Agrega al principio
print(musicos)

#Agregamos al final sin append
musicos.insert(len(musicos), "Astor Piazzola") #Mismo efecto (anidamos métodos)
print(musicos)
print()

#Pop, Remove e Index
print("- Pop, Remove e Index:")
musicos.pop() #Elimina el último elemento
print(musicos)
musicos.pop(1) #Elimina el elemento en cierta pósición
print(musicos)

print(autores)
autores.remove("Borges")
print(autores)
print(autores.index("Sábato")) #pos 1
# print(autores.index("Borges"))#No lo encuentra porque fue eliminado
print()

#Count, Reverse, Sort y Clear
valores=[3,4,5,3,5,8,5]
print(valores.count(3)) # El 3 está 2 veces
print(valores.count(7)) #no está en la lista

print("Original:", valores)
valores.reverse()
print("Reverse:", valores) #Invierte la lista

valores.sort()
print("Orden Ascendente:", valores) #Orden de menor a mayor
valores.sort(reverse=True)
print("Orden Descendente:", valores) #Orden de mayor a menor

valores.clear() #Vacía la lista
print(valores)

nombres=['Juan','Ana','Luisa','Fernando']
print("Original:", nombres)
nombres.reverse()
print("Reverse:", nombres) #Invierte la lista

nombres.sort()
print("Orden Ascendente:", nombres) #Orden de A a Z
nombres.sort(reverse=True)
print("Orden Descendente:", nombres) #Orden de Z a A
