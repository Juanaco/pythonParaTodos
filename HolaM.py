# !/usr/bin/env python
# -*- coding: utf-8 -*-

print ("Hola Mundo")

cadena = "Hola Mundo"

entero = 23

print ("Es un:", type(cadena))

hexa = 0x32

print (hexa, "Está mal, esto no es un hexadecimal")

raw = r"/n"

print (raw)

a = "uno"
b = "dos"

c = a + b
d = a * 4
print (c, d)

lista = ["Hola", "Juan", 28, "años", [1, 2, "otra lista"]]

print (lista)
print (lista[4][2])

lista[1] = "Gabriel"

print (lista)

listados = ["Comer", "Fideos", "Hace", "Engordar", "Más", "Si", "Comes", "Con", "Crema"]

milis = listados[0:5]

print(milis)

milis2 = listados[0:9:2]

print (milis2)

tupla = ("esto seria tupla", "con algunos elementos", "gg")

print (tupla, type(tupla))

otraCadena = "Esto sería una cadena"

print (otraCadena, otraCadena[0], otraCadena[5:10], otraCadena[::3])

diccionario = {"Spirited Away": "Hayao Miyazaki",
               "My Neighbor Totoro": "Hayao Miyazaki",
               "Kaguya-hime no Monogatari": "Isao Takahata",
               "From Dusk till Dawn": "Quentin Tarantino"}

print ("Películas de Studio Ghibli para ver: ", diccionario)

numero = -1

if numero < 0:
    print ("Negativo")
elif numero > 0:
    print ("Positivo")
else:
    print ("Cero")

# if distinto :O
var = "par" if (numero % 2 == 0) else "impar"

print (var)

# while

horas = 0
while horas < 18:
    horas = horas + 1
    if horas == 18:
        print (" " + str(horas) + " ")
    elif horas == 1:
        print (" " + str(horas) + "")
    else:
        print (" " + str(horas) + " ")

# el continue

edad = 0
while edad < 21:
    edad = edad + 1
    if edad % 2 == 0:
        continue
    print ("feliz cumpleaños número " + str(edad))

    if edad == 21:
        print("Tomate un trago legalmente")

# ingreso de usuario

while True:
    entrada = raw_input("> ")
    if entrada == "chau":
        break
    else:
        print (entrada)

# otra forma de hacerlo

"""salir = False
while not salir:
    entrada = input()
    if entrada == "adios":
        salir = True
    else:
        print (entrada)"""

# un for

secuencia = ["uno", "dos", "tres"]

for elemento in secuencia:
    print (elemento)

print ("página 35") 

def una_funcion(param1, param2):
    """La primera función que vamos a hacer
    para probar en python """
    print param2
    print param1
una_funcion(param2 ="Cati", param1 = "Holi")

def otra_funcion(p1, p2, *otro):
    """Probamos función con parámetros variables
    a ver que pasa, genera una tupla con esto"""
    for val in otro:
        print val
otra_funcion("Tateti", 3, "A ver", "quease", "conesto")

def funcion(p1, p2, **otro):
    for i in otro.items():
        print i



funcion("alala", "aldksfj", letra = "a", numero = 3, otronum = 4)


# para que no corte solo el programa
# in    put()
