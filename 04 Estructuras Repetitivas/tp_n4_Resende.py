# 1) Imprimir los numeros del 0 al 100 (inclusive), uno por linea
for i in range(0, 101):
    print(i)

# 2) Solicita un numero entero y muestra cuantos digitos tiene
numero = input("Ingresa un numero entero: ")
# Se quita el signo negativo si lo tiene y se cuenta la cantidad de caracteres
digitos = len(numero.lstrip('-'))
print("Cantidad de digitos:", digitos)

# 3) Suma los numeros enteros entre dos valores dados por el usuario, sin incluir los extremos
inicio = int(input("Ingrese el primer numero: "))
fin = int(input("Ingrese el segundo numero: "))

# Se asegura que el menor quede como inicio
if inicio > fin:
    inicio, fin = fin, inicio

suma = 0
for i in range(inicio + 1, fin):
    suma += i

print("La suma de los numeros entre los dos valores es:", suma)

# 4) Suma numeros ingresados por el usuario hasta que se ingrese un 0
total = 0
while True:
    numero = int(input("Ingresa un numero (0 para terminar): "))
    if numero == 0:
        break
    total += numero

print("La suma total es:", total)

# 5) Juego para adivinar un numero aleatorio entre 0 y 9
import random

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el numero (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        break

print("¡Correcto! Lo lograste en", intentos, "intento(s).")

# 6) Imprimir los numeros pares entre 0 y 100 en orden decreciente
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7) Suma de los numeros entre 0 y un numero positivo ingresado por el usuario
limite = int(input("Ingresa un numero entero positivo: "))
suma = 0
for i in range(1, limite):
    suma += i

print("La suma de los numeros desde 1 hasta", limite - 1, "es:", suma)

# 8) Contar pares, impares, positivos y negativos en una secuencia de 100 números
cantidad = 100  # Cambiar este valor para probar con menos
pares = impares = positivos = negativos = 0

for _ in range(cantidad):
    numero = int(input("Ingresa un numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# 9) Calcular la media de 100 numeros ingresados por el usuario
cantidad = 100  # Cambiar para probar con menos
suma = 0

for _ in range(cantidad):
    numero = int(input("Ingresa un numero: "))
    suma += numero

media = suma / cantidad
print("La media de los numeros ingresados es:", media)

# 10) Invertir los digitos de un numero ingresado por el usuario
numero = input("Ingresa un numero: ")
# Se invierte el numero con slicing
numero_invertido = numero[::-1]
print("Numero invertido:", numero_invertido)