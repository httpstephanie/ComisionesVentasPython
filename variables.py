#nombre = "Juan"
#print(nombre)
#nombre = "Estefania"
#print(nombre)
#----------------------------_
# #edad1 = 30
#edad2 = 15
#print(edad1 + edad2)]
#nombre = "Hola "
#nombre2 = "Python"
#frase = nombre + nombre2
#print(frase)
#----------------------------
#mi_numero = 1.8 + 3
#print(mi_numero + mi_numero)
#print(type(mi_numero))
#----------------------------
#edad = input("Dime tu edad: ")
#print("Tu edad es " + edad )
#nueva_edad = 1 + edad
#print("Vas a cumplir " + nueva_edad)
#-----------------------------------
#num1 = 20
#num2 =30.5
#num1 = num1 + num2
#print(type(num1))
#print(type(num2))
#ESTE EJERCICIO IMPRIME QUE AMBOS SON FLOATS
#---------------------------------------
#num1 = 5.8
#print(num1)
#print(type(num1))
#num2 = int(num1)
#print(num2)
#(print(type(num2)))
#edad = input("Dime tu edad")
#print(type(edad))
#edad = int (edad)
#print(type(edad))
#nueva_edad = 1 + edad
#print(nueva_edad)
#-------------------------------------------------------
#CONCAQUENACION CADENAS
#x = 10
#y = 5
#print("La suma de {} y {} es igual a {}" .format(x,y,x+y ))
#--------------------------------------------------------
#color = "rojo"
#matricula = 1010101
#print(f"El auto es {color} y su matricula es {matricula}")
#--------------------------------------------------------------
#Operaciones
#x = 6
#y = 2
#z = 7
#print(f"{x} + {y} es igual a {x + y}")
#print(f"{x} + {y} es igual a {x - y}")
#print(f"{x} + {y} es igual a {x * y}")
#print(f"{x} + {y} es igual a {x / y}")
#print(f"{z} dividido al piso de {y} es igual a {z//y}")
#print(f"{z} modulo de {y} es igual a {z%y}") #LO USAMOS PARA SABER SI ES PAR O IMPAR
#print(f"{x} elevado a la {y} es igual a {x**y}")
#print(f"{x} elevado a  la {3} es igual a {x**3}")
#print(f"La raiz cuadrada de {x} es {x**0.5}")
#----------------------------------------------------------
#REDONDEAR NUMEROS
#resultado = round(90/7)
#print(resultado)
#con las comas eliges la cantidad de decimales
#valor = round(95.666666,2)
#print(valor)
#valor = round(95.666666,2)
#print(valor)
#print(type(valor))
#x = 5
#print(f"{round(x**0.5,4),}")
nombre = input("Escribe tu nombre: ")
ventas = input("Cuatas fueron tus ventas totales del mes? ")
ventas = int(ventas)
comision = ventas * 13 / 100
comision = round(comision,2)
print(f"Hola {nombre} tu comision de este mes es de $ {comision} BUEN TRABAJO!")
