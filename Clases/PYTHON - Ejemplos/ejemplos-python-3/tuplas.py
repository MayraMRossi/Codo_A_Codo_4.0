# TUPLAS
# Ejemplos de tuplas

()                                              # tupla vacía
'un valor',                                     # tupla con un valor
('uno', 'dos', 'tres')	             	        # cadenas	
('Palotes, Juan de', (1930, 11, 13), 3000936)   # datos de persona
'Palotes, Juan de', (1930, 11, 13), 3000936     # datos de persona

# Creación: más ejemplos
tupla= (1, 2, 3)
fecha= (25, "Diciembre", 2016)
punto= (10, 2)
persona= ("Rodriguez", "Pablo", 43)
print(tupla)
print(fecha)
print(punto)
print(persona)
print(fecha[1]) 
print(persona[2]) 
# fecha[1] = "Noviembre" # Error

#Empaquetado (zip)
nombre= 'Carlos'
apellido= 'Rodriguez'
datos= nombre,apellido,32
print(datos) 

#Desempaquetado (unpack)
fecha= (10, "noviembre", 2021)
print(fecha)
dd,mm,aa= fecha
print("Dia:",dd)
print("Mes:",mm)
print("Año:",aa)

#Tuplas anidadas
empleado= ["juan", 53, (25, 11, 1999)]
print(empleado)
empleado.append((1, 1, 2016))
print(empleado)

alumno= ("pedro",[7, 9])
print(alumno)
alumno[1].append(10)
print(alumno)

# Accesos
tupla = ('Pérez', 'Ana', (1930, 11, 13), 12093644) 

#Desempaquetando
apellido, nombre, fecha, dni = tupla
print('Nombre:', nombre + '. Nombre:', apellido +'. Fecha nac.:', fecha, '. DNI:', dni)

#Con un índice, comenzando de la posición 0
print('Nombre:', tupla[1] + '. Apellido:', tupla[0] +'. Fecha nac.:', tupla[2], '. DNI:', tupla[3])

# Por método rebanada o Slicing tupla[comienzo:fin:salto]
print(tupla[::]) #Toda la tupla
print(tupla[0:2:1]) #Desde 0 a 1 (no se incluye 2)
print(tupla[0:4:2]) #Solo valores 0 y 2