from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    entrada = input("Ingrese un número: ")
    numero = int(entrada)  # Puede lanzar ValueError si no es numérico
    if numero < 0:
        raise NumeroDebeSerPositivo("El número debe ser positivo.")
    return numero

if __name__ == '__main__':
    try:
        numero = ingrese_numero()
        print(f"Número válido: {numero}")
    except ValueError:
        print("Error: La entrada debe ser un número válido.")
    except NumeroDebeSerPositivo as e:
        print(f"Error: {e}")
