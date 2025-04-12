#1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3
par = int(input("Ingrese un número par: "))
if (par % 2) == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4
edad = int(input("Ingrese su edad: "))
if edad > 0 or edad < 12:
    print("Niño/a")
elif edad >= 12 or edad < 18:
    print("Adolescente")
elif edad >= 18 or edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5
password = input("Ingrese una contraseña: ")
largo = len(password)
if largo >= 8 and largo <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana and mediana == moda:
    print("Sin sesgo")

#7
frase = input("Ingrese una frase")
ultima_letra = frase[-1].lower()
if ultima_letra in 'aeiou':
    frase += "!"
    print(frase)

#8
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese número 1, 2 o 3 dependiendo de la opción que desee: "))
if numero == 1:
    nombre = nombre.lower()
elif numero == 2:
    nombre = nombre.upper()
if numero == 3:
    nombre = nombre.title()
print(nombre)

#9
terremoto = int(input("Ingrese magnitud del terremoto: "))
if terremoto > 0 and terremoto < 3:
    print("Muy leve")
elif terremoto >= 3 and terremoto < 4:
    print("Leve")
elif terremoto >= 4 and terremoto < 5:
    print("Moderado")
elif terremoto >= 5 and terremoto < 6:
    print("Fuerte")
elif terremoto >= 6 and terremoto < 7:
    print("Muy Fuerte")
elif terremoto >= 7:
    print("Extremo")

#10
hemisferio = input("En cual hemisferio se encuentra(s/n): ")
mes = input("Ingrese el mes: ")
dia = int(input("Ingrese el dia: "))
if hemisferio == "n":
    if mes == "diciembre" and (dia >= 21 and dia <= 31) or mes == "enero" and (dia >= 1 and dia <= 31) or mes == "febrero" and (dia >= 1 and dia <= 28) or mes == "marzo" and (dia >= 1 and dia <= 20):
        print("Invierno")
    if mes == "marzo" and (dia >= 21 and dia <= 31) or mes == "abril" and (dia >= 1 and dia <= 30) or mes == "mayo" and (dia >= 1 and dia <= 31) or mes == "junio" and (dia >= 1 and dia <= 20):
        print("Primavera")
    if mes == "junio" and (dia >= 21 and dia <= 30) or mes == "julio" and (dia >= 1 and dia <= 31) or mes == "agosto" and (dia >= 1 and dia <= 31) or mes == "septiembre" and (dia >= 1 and dia <= 20):
        print("Verano")
    if mes == "septiembre" and (dia >= 21 and dia <= 30) or mes == "octubre" and (dia >= 1 and dia <= 31) or mes == "noviembre" and (dia >= 1 and dia <= 30) or mes == "diciembre" and (dia >= 1 and dia <= 20):
        print("Otoño")
elif hemisferio == "s":
    if mes == "diciembre" and (dia >= 21 and dia <= 31) or mes == "enero" and (dia >= 1 and dia <= 31) or mes == "febrero" and (dia >= 1 and dia <= 28) or mes == "marzo" and (dia >= 1 and dia <= 20):
        print("Verano")
    if mes == "marzo" and (dia >= 21 and dia <= 31) or mes == "abril" and (dia >= 1 and dia <= 30) or mes == "mayo" and (dia >= 1 and dia <= 31) or mes == "junio" and (dia >= 1 and dia <= 20):
        print("Otoño")
    if mes == "junio" and (dia >= 21 and dia <= 30) or mes == "julio" and (dia >= 1 and dia <= 31) or mes == "agosto" and (dia >= 1 and dia <= 31) or mes == "septiembre" and (dia >= 1 and dia <= 20):
        print("Invierno")
    if mes == "septiembre" and (dia >= 21 and dia <= 30) or mes == "octubre" and (dia >= 1 and dia <= 31) or mes == "noviembre" and (dia >= 1 and dia <= 30) or mes == "diciembre" and (dia >= 1 and dia <= 20):
        print("Primavera")