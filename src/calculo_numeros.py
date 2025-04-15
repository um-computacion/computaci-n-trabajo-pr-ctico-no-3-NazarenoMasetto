
from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    entrada = input("Ingrese un número: ")
    numero = int(entrada)  # Puede lanzar ValueError si no es numérico
    if numero < 0:
        raise NumeroDebeSerPositivo("El número debe ser positivo.")
    return numero