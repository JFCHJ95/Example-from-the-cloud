# First exercises
from distutils.command.build_scripts import first_line_re


saludo = "Hola mundo"
print(saludo)

# Suma
a: int = 5
b: int = 10
c: int = a + b
print("La suma de " + str(a) + " + " + str(b) + " es igual a " + str(c))

# Multiplicacion
def multip(first_value: int, second_value: int) -> int:
    """
    This funtion multiply two values
    """
    return first_value * second_value


print(multip(first_value=5, second_value=10))

# Repetir
d: int = 3
cadena: str = "Saludos "
texto: str
texto = d * cadena
print(texto)
