# 1) Escribir un programa que solicite la edad del usuario.
# Si el usuario es mayor de 18 años, mostrar "Es mayor de edad".

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

# 2) Escribir un programa que solicite su nota al usuario.
# Si la nota es mayor o igual a 6, mostrar "Aprobado"; en caso contrario, "Desaprobado".

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares.
# Si el número es par, mostrar mensaje correspondiente; si no, también.

numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que clasifique según edad en categorías.

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Programa que valida si la contraseña tiene entre 8 y 14 caracteres

contraseña = input("Ingrese una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. 
from statistics import mode, median, mean

# Definir la lista de números aleatorios
numeros_aleatorios = [10, 2, 5, 8, 7, 6, 10, 9, 12, 5]

# Calcular la moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Imprimir los resultados
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Determinar el tipo de sesgo
if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario.
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final 
# e imprimir el string resultante por pantalla; en caso contrario, dejar el string 
# tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Solicitar al usuario una frase o palabra
frase = input("Ingresa una frase o palabra: ")

# Verificar si la frase termina con una vocal
if frase[-1].lower() in 'aeiouáéíóú':
    print(f"{frase}!")
else:
    print(frase)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee.
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.

# Solicitar al usuario su nombre y opción de formato
nombre = input("Ingresa tu nombre: ")
opcion = int(input("Ingresa 1 para mayúsculas, 2 para minúsculas, 3 para primera letra mayúscula: "))

# Transformar el nombre según la opción seleccionada
if opcion == 1:
    print(nombre.upper())  # Convierte a mayúsculas
elif opcion == 2:
    print(nombre.lower())  # Convierte a minúsculas
elif opcion == 3:
    print(nombre.title())  # Convierte la primera letra de cada palabra a mayúsculas
else:
    print("Opción no válida")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto,
# clasifique la magnitud en una de las siguientes categorías según la escala de Richter 
# e imprima el resultado por pantalla:

# Menor que 3: "Muy leve" (imperceptible).
# Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Solicitar al usuario la magnitud del terremoto
magnitud = float(input("Ingresa la magnitud del terremoto: "))

# Clasificar según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año.
# El programa debe preguntar al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es 
# y qué día es. Utilizando esa información, el programa debe determinar la estación del año en el hemisferio correspondiente.

# Solicitar al usuario la información necesaria
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("¿Qué mes del año es? (1-12): "))
dia = int(input("¿Qué día del mes es? (1-31): "))

# Determinar la estación del año
if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)):
        estacion = "Verano"
    else:
        estacion = "Otoño"
else:  # Hemisferio Sur
    if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)):
        estacion = "Invierno"
    else:
        estacion = "Primavera"

# Imprimir la estación
print(f"La estación en el hemisferio {hemisferio} es: {estacion}")

