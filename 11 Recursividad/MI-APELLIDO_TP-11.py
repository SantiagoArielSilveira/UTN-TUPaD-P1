#1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Ingrese un numero: "))
print("Factoriales: ")
for i in range(1,n + 1):
    print(f"{i}: {factorial(i)}")

#2
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

numero = int(input("Ingrese un numero: "))
print("Fibonacci: ")
for i in range(0,numero + 1):
    print(f"{i}: {fibonacci(i)}")

#3
def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)

#4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

cadena = decimal_a_binario(25)
print(cadena)

#5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

print(es_palindromo("radar"))

#6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

print(suma_digitos(1234))

#7
def contar_bloques(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print(contar_bloques(10))

#8
def contar_digito(numero, digito):
    numero_cadena = str(numero)
    digito_cadena = str(digito)
    
    if len(numero_cadena) == 1:
        if numero_cadena == digito_cadena:
            return 1 
        else: 
            return 0
    else:
        if numero_cadena[-1] == digito_cadena:
            contador = 1
        else:
            contador = 0
        return contador + contar_digito(int(numero_cadena[:-1]), digito)

print(contar_digito(3221234523,3))

#Silveira Santiago