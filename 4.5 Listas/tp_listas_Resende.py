# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4.
# Utilizar la función range.
numeros_mult_4 = list(range(4, 101, 4))
print("Múltiplos de 4 entre 1 y 100:", numeros_mult_4)

# 2) Crear una lista con cinco elementos (los que más te gusten) y mostrar el penúltimo.
# Usar índices negativos para acceder al penúltimo elemento.
mi_lista = [1, 2, 3, 4, 5]
print("Penúltimo elemento de mi lista:", mi_lista[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante.
lista_vacia = []
lista_vacia.append("hola")
lista_vacia.append("mundo")
lista_vacia.append("python")
print("Lista con palabras agregadas:", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"  # Segundo valor
animales[-1] = "oso"  # Último valor
print("Lista de animales después del reemplazo:", animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print("Lista después de eliminar el máximo:", numeros)
# Explicación: El programa encuentra el valor máximo de la lista 'numeros' (22) y lo elimina.

# 6) Crear una lista con números del 10 al 30 (inclusive), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
numeros = list(range(10, 31, 5))
print("Primeros dos elementos de la lista:", numeros[:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "civic"
autos[2] = "corolla"
print("Lista de autos después del reemplazo:", autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante.
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista de dobles:", dobles)

# 9) Dada la lista “compras”, realizar las siguientes operaciones:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

# d) Imprimir la lista resultante.
print("Lista de compras después de las modificaciones:", compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” con los siguientes elementos:
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("Lista anidada:", lista_anidada)
