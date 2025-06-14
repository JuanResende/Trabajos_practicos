# EJERCICIO 1: Factorial de un número

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingresá un número: "))
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")


# EJERCICIO 2: Serie de Fibonacci hasta una posición dada

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

limite = int(input("¿Hasta qué posición querés mostrar la serie de Fibonacci?: "))
for i in range(limite + 1):
    print(f"Fibonacci({i}) = {fibonacci(i)}")


# EJERCICIO 3: Potencia de un número usando recursividad

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

b = int(input("Base: "))
e = int(input("Exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")


# EJERCICIO 4: Convertir un número decimal a binario

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingresá un número en decimal: "))
if numero == 0:
    print("Binario: 0")
else:
    print("Binario:", decimal_a_binario(numero))


# EJERCICIO 5: Verificar si una palabra es un palíndromo

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingresá una palabra: ").lower()
print("¿Es palíndromo?", es_palindromo(texto))


# EJERCICIO 6: Sumar los dígitos de un número

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

numero = int(input("Ingresá un número entero positivo: "))
print("Suma de dígitos:", suma_digitos(numero))


# EJERCICIO 7: Contar bloques en una pirámide

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel = int(input("¿Cuántos bloques tiene el nivel más bajo?: "))
print("Bloques totales necesarios:", contar_bloques(nivel))


# EJERCICIO 8: Contar cuántas veces aparece un dígito

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

num = int(input("Ingresá un número: "))
dig = int(input("Ingresá un dígito (0-9): "))
print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces.")