#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola mundo!")
    return

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. 
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}")
    return

saludar_usuario("Marcos")

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    return

nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
edad = input("Ingrese edad: ")
residencia = input("Ingrese residencia: ")
informacion_personal(nombre,apellido,edad,residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

from math import pi

def calcular_area_circulo(radio):
    return pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

radio = int(input("Ingrese el radio: "))
print(f"Area: {calcular_area_circulo(radio)}")
print(f"Perimetro: {calcular_perimetro_circulo(radio)}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 60 / 60

segundos = int(input("Ingrese segundos: "))
print(f"Horas: {segundos_a_horas(segundos)}")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} multiplicado por {i} es: {numero*i}")
    return

numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
#  Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    print(f"Suma: {a+b}")
    print(f"Resta: {a-b}")
    print(f"Multiplicacion: {a*b}")
    print(f"Division: {a/b}")
    return

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))
operaciones_basicas(numero1,numero2)

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC).
#  Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = int(input("Ingrese su peso(Kg): "))
altura = int(input("Ingrese su altura(m): "))
print(f"Su IMC es: {calcular_imc(peso,altura)}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
#  Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius * (9/5)) + 32

celsius = int(input("Ingrese temperatura(°C): "))
print(f"°C: {celsius} a °F: {celsius_a_fahrenheit(celsius)}")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    return (a+b+c) / 3

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))
print(f"Promedio: {calcular_promedio(a,b,c)}")

#Santiago Ariel Silveira