#1
print("Hola Mundo!")

#2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

#3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese lugar de residencia: ")
print(f"“Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4
radio = int(input("Ingrese el radio de la circunferencia: "))
perimetro = 3.14 * 2 * radio
area = 3.14 * (radio**2)
print(f"El Area es {area} y el perimetro es {perimetro}")

#5
segundos = int(input("Ingrese los segundos: "))
horas = segundos / 60 / 60
print(f"La cantidad de horas es {horas}")

#6
tabla = int(input("Ingrese numero: "))
print(f"Tabla de multiplicar: {tabla},{tabla*2},{tabla*3},{tabla*4},{tabla*5},{tabla*6},{tabla*7},{tabla*8},{tabla*9},{tabla*10}")

#7
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
print(f"Suma: {num1 + num2} resta: {num1 - num2} division: {num1 / num2} multiplicacion: {num1 * num2}")

#8
altura = int(input("Ingrese su altura: "))
peso = int(input("Ingrese su peso: "))
print(f"Indice de masa corporal: {peso / (altura ** 2)}")

#9
celsius = int(input("Ingrese la temperatura: "))
print(f"La temperatura en fahrenheit es: {9 / 5 * celsius + 32}")

#10
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
print(f"El promedio es: {(num1 + num2 + num3) / 3}")

#Santiago_Ariel_Silveira