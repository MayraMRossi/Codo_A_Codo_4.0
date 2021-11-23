#CADENAS: METODOS

print("******* CADENAS: METODOS *******")
#Join / Split / replace
print("- Join,  / Split / Replace")
cad="Juan Pablo"
cad='_'.join(cad)
print(cad) #Cadena devuelta con el separador _ entre cada caracter

cad="Cadenas de caracteres"
cad_lista=cad.split(' ')
print(cad_lista) #Convierte la cadena en una lista
print(cad_lista[2]) #Podemos acceder a un elemento de esa lista

cad="Programando en JAVA. JAVA es lo mejor!"
cad_nueva=cad.replace('JAVA', 'Python') # reemplaza todas las apariciones
print(cad_nueva)
cad2="Programando en JAVA. JAVA es lo mejor!"
cad_nueva_2=cad2.replace('JAVA', 'Python', 1) # para reemplazar solo una aparición
print(cad_nueva_2)
print()

#isalpha / isdigit / isalnum
print("- isalpha / isdigit / isalnum")
cad="Python"
cad2="Python3"
print(cad, "es alfabético?", cad.isalpha()) # True
print(cad2, "es alfabético?", cad2.isalpha()) # False
print()
cad="1234"
cad2="1234a"
print(cad, "es numérico?", cad.isdigit()) # True
print(cad2, "es numérico?", cad2.isdigit()) # False
print()
cad=""
cad2="1234"
cad3="ab"
cad4="12a"
print(cad, "es alfabético/numérico?", cad.isalnum()) # False
print(cad2, "es alfabético/numérico?", cad2.isalnum()) # True
print(cad3, "es alfabético/numérico?", cad3.isalnum()) # True
print(cad4, "es alfabético/numérico?", cad4.isalnum()) # True
print()

#isupper / islower
print("- isupper / islower")
cad="Python"
cad2="python"
print(cad, "está en mayúsculas?", cad.isupper()) # False
print(cad2, "está en minúsculas?", cad2.islower()) # True
print()

#upper / lower / capitalize / title
print("- upper / lower / capitalize / title")
cad="Estamos aprendiendo Python"
print("Upper:", cad.upper()) # ESTAMOS APRENDIENDO PYTHON
print("Lower:", cad.lower()) # estamos aprendiendo python
print("Capitalize:", cad.capitalize()) # estamos aprendiendo python
print("Title:", cad.title()) # Estamos Aprendiendo Python
print()

#center / ljust / rjust / zfill
print("- center / ljust / rjust / zfill")
cad1="Python"
cad2=cad1.center(14,"*")
print("Center:", cad2)# ****Python****
cad2=cad1.ljust(10, '-')
print("Ljust:", cad2)# Python---- 
cad2=cad1.rjust(10, '-')
print("Rjust:", cad2)# ----Python 
num=345
cad= str(num).zfill(7)
print(cad) # 0000345
print()

#lstrip / rstrip / strip
print("- lstrip / rstrip / strip")
cad="---Hola-Python----"
cad2="---Hola-Python----"
cad3="*****Hola-Python****"

print(cad)
cad= cad.lstrip("-")
print("Lstrip:", cad) # Hola-Python----

print(cad2)
cad2= cad2.rstrip("-")
print("Rstrip:", cad2) #---Hola-Python

print(cad3)
cad3= cad3.strip("*")
print("Strip:", cad3) #Hola-Python
print()

#find y rfind
print("- find y rfind")
cad="---Hola-Python----"
print(cad)
pos= cad.find("Python") #Desde la izquierda
print(pos) #8
cad="---Hola-Python--Python--"
pos= cad.rfind("Python")
print(pos) #16 Desde la derecha (última aparición de Python)