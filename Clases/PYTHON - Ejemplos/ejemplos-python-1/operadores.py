'''Tipos de operadores:
- Matemáticos / Aritméticos
- De asignación
- Relacionales
- Lógicos
- De pertenencia
'''

#Matemáticos/Aritméticos
print("Suma (+):", 12+13) #Suma
print("Resta (-):", 12-13) #Resta
print("Multiplicación (*):", 12*13) #Multiplciación
print("División (/) con decimales:", 12/13) #División con decimales
print("División entera (//):", 13//5) #División entera
print("Resto o módulo de la división entera (%):", 13%5) #Resto o módulo de la división entera

print("Número par: ", 2%2) #Par
print("Número impar: ",5%2) #Impar
print("Potencia:", 5**2) #Potencia (25)
print("Raíz cuadrada de 9:", 9**(1/2)) #Raíz cuadrada (3)
print("Raíz cúbica de 8:", 8**(1/3)) #Raíz cúbica (2)

#Asignación
print("+= y -=")
x=5
x+=2 # x=x+2
print(x)
x-=2
print(x)
print()

print("*= y /=")
x=10
x*=2
print(x)
x/=4
print(x)
print()

print("%= //= y **=")
x=15
x%=2
print(x)
x=15
x//=6
print(x)
x**=3
print(x)
print()

#Relacionales: > < >= <= == !=
print("Igual:", 5==5) #True
print("No igual:", 5!=5) #False
print("Mayor que (>):", 8>8) #False
print("Mayor o igual que (>=):", 8>=8) #True
print("Menor que (<):", 3<3) #False
print("Menor o igual que (<=):", 3<=3) #True
print("Jerarquía de operadores:", not((5+5)>10)) # jerarquía entre operadores: 
                                                 # 1° (5+5);
                                                 # 2° (10)>10;
                                                 # 3° not False = True

#Lógicos (AND, OR, NOT)
print("AND:", True and False) #AND (False)
print("OR:", True or False) #OR (True)
print("NOT:", not False) #NOT (True)
resultado= not (10>5) #(not True)
print("Resultado:", resultado) #False

#De Pertenencia
lista= [1, 3, 2, 7, 9, 8, 6]
print(lista)
print("¿4 está en lista?:", 4 in lista) #False
print("¿3 está en lista?:", 3 in lista) #True
print("¿4 no está en lista?:", 4 not in lista) #True