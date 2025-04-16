# Función para sumar dos números
def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b

# Función para restar dos números
def restar(a, b):
    """Devuelve la resta de dos números."""
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    """Devuelve el producto de dos números."""
    return a * b

# Función para dividir dos números
def dividir(a, b):
    """Devuelve la división de dos números. Maneja división por cero."""
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

# Función para calcular el módulo
def modulo(a, b):
    """Devuelve el resto de la división entre dos números."""
    if b == 0:
        return "Error: No se puede calcular el módulo con divisor cero"
    return a % b

# Función para calcular la potencia
def potencia(a, b):
    """Devuelve el resultado de elevar a a la potencia b."""
    return a ** b

# Función para verificar si un número es par
def es_par(numero):
    """Devuelve True si el número es par, False si es impar."""
    return numero % 2 == 0

# Función para calcular el factorial de un número
def factorial(n):
    """Devuelve el factorial de un número entero no negativo."""
    if n < 0:
        return "Error: El factorial no está definido para números negativos"
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Función para encontrar el mayor de dos números
def mayor(a, b):
    """Devuelve el mayor de dos números."""
    return a if a > b else b

# Función para encontrar el menor de dos números
def menor(a, b):
    """Devuelve el menor de dos números."""
    return a if a < b else b

# Función para verificar si dos valores son iguales
def es_igual(a, b):
    """Devuelve True si a es igual a b, False en caso contrario."""
    return a == b

# Función para verificar si dos valores son diferentes
def es_diferente(a, b):
    """Devuelve True si a es diferente de b, False en caso contrario."""
    return a != b

# Función para verificar si un valor es mayor que otro
def es_mayor(a, b):
    """Devuelve True si a es mayor que b, False en caso contrario."""
    return a > b

# Función para verificar si un valor es menor que otro
def es_menor(a, b):
    """Devuelve True si a es menor que b, False en caso contrario."""
    return a < b

# Función para verificar si un valor es mayor o igual que otro
def es_mayor_igual(a, b):
    """Devuelve True si a es mayor o igual que b, False en caso contrario."""
    return a >= b

# Función para verificar si un valor es menor o igual que otro
def es_menor_igual(a, b):
    """Devuelve True si a es menor o igual que b, False en caso contrario."""
    return a <= b

# Función para invertir una cadena
def invertir_cadena(cadena):
    """Devuelve la cadena invertida."""
    return cadena[::-1]

# Función para contar las palabras en una cadena
def contar_palabras(cadena):
    """Devuelve el número de palabras en una cadena."""
    return len(cadena.split())

# Función para verificar si una cadena es un palíndromo
def es_palindromo(cadena):
    """Devuelve True si la cadena es un palíndromo, False en caso contrario."""
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

# Función para generar una lista de números del 1 al n
def generar_lista(n):
    """Devuelve una lista de números del 1 al n."""
    return list(range(1, n + 1))