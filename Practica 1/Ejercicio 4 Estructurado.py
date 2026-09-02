import math

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def calcular_desviacion(numeros, promedio):
    n = len(numeros)
    if n <= 1:
        return 0.0
    suma_cuadrados = sum((x - promedio) ** 2 for x in numeros)
    return math.sqrt(suma_cuadrados / (n - 1))

def main_estructurado():
    entrada = input("Ingrese 10 números: ").split()
    if len(entrada) == 10:
        numeros = [float(x) for x in entrada]
        prom = calcular_promedio(numeros)
        desv = calcular_desviacion(numeros, prom)
        print(f"El promedio es {prom:.2f}")
        print(f"La desviacion estandard es {desv:.5f}")

if __name__ == "__main__":
    main_estructurado()