# First exercises
saludo = "Hola mundo"
print(saludo)

# Suma
a: int = 5
b: int = 10
c: int = a + b
print("La suma de " + str( a ) + " + "+ str( b ) + " es igual a " + str(c))

# Multiplicacion
def multip(n1: int, n2: int) ->int:
    x = n1 * n2
    return x

print(multip(5,10))

# Repetir 
d: int = 3
cadena: str = 'Saludos '
texto: str
texto = d*cadena
print(texto)