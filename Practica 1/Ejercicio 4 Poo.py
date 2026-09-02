import math
class Estadistica:
    # a atributos privados
    def __init__(self, numeros: list):
        self._numeros = numeros
    # b retorna el promedioo
    def promedio(self) -> float:
        suma = 0
        for i in range(len(self._numeros)):
            suma = suma + self._numeros[i]
        return suma / len(self._numeros)
    # c retorna la desviación estandar
    def desviacion(self) -> float:
        suma = 0
        prom = self.promedio()
        for i in range(len(self._numeros)):
            suma = suma + (self._numeros[i] - prom) ** 2
        return math.sqrt(suma / (len(self._numeros) - 1))
# Programa de prueba
def probar_estadistica():
    entrada = input("Ingrese 10 numeros: ").split()
    numeros = list(map(float, entrada))
    estadistica = Estadistica(numeros)
    print(f"El promedio es {estadistica.promedio():.2f}")
    print(f"La desviacion estandar es {estadistica.desviacion():.5f}")
if __name__ == "__main__":
    probar_estadistica()