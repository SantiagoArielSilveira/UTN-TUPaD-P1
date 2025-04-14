#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0,101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = int(input("Por favor ingrese un número entero: "))
digitos = 0
while numero > 0:
        numero //= 10
        digitos += 1
print(f"Digitos: {digitos}")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Por favor ingrese el primer número entero: "))
num2 = int(input("Por favor ingrese el segundo número entero: "))
sumatoria = 0
if num1 > num2:
      for i in range (num2,num1+1):
            sumatoria += i
else:
      for i in range (num1,num2+1):
            sumatoria += i
print(f"Sumatoria: {sumatoria}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

numero = 1
sumatoria = 0
while numero > 0:
    numero = int(input("Por favor ingrese un número entero: "))
    sumatoria += numero
print(f"Sumatoria: {sumatoria}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
aleatorio = random.randint(0,9)
numero = -1
contador = 0
while numero != aleatorio:
    numero = int(input("Por favor ingrese un número entero: "))
    contador += 1
print(f"Intentos: {contador} El número era: {aleatorio}")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100,0,-2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero = int(input("Por favor ingrese un número entero: "))
sumatoria = 0
for i in range(0,numero+1):
     sumatoria += i
print(f"Sumatoria: {sumatoria}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad_numeros = 100
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(0,cantidad_numeros):
    numero = int(input("Por favor ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero >= 0:
        positivos += 1
    else:
        negativos += 1
print(f"Pares: {pares} Impares: {impares} Positivos: {positivos} Negativos: {negativos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor,
#pero debe poder procesar 100 números cambiando solo un valor).

cantidad_numeros = 100
sumatoria = 0
for i in range(0,cantidad_numeros):
    numero = int(input("Por favor ingrese un número entero: "))
    sumatoria += numero
print(f"Promedio: {sumatoria/cantidad_numeros}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Por favor ingrese un número entero: "))
auxiliar = numero
digitos = 0
while auxiliar > 0:
        auxiliar //= 10
        digitos += 1
auxiliar = 0
invertido = 0
for i in range(0,digitos):
    auxiliar = numero % 10
    numero = (numero - auxiliar) / 10
    invertido += auxiliar
    if i + 1 < digitos:
        invertido *= 10
invertido = int(invertido)
print(f"Invertido: {invertido}")

#Santiago Ariel Silveira