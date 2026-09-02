import time
import random
class Cronometro:
    #b
    def __init__(self):
        self._inicia = time.time() * 1000
        self._finaliza = 0.0
    # a
    def get_inicia(self):
        return self._inicia
    def get_finaliza(self):
        return self._finaliza
    # c
    def inicia(self):
        self._inicia = time.time() * 1000
    # d
    def detener(self):
        self._finaliza = time.time() * 1000
    # e
    def lapsoDeTiempo(self):
        return self._finaliza - self._inicia
def ordenacion_por_seleccion(arreglo):
    n = len(arreglo)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arreglo[min_idx] > arreglo[j]:
                min_idx = j
        arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]

numeros = [random.randint(1, 100000) for _ in range(100000)]
cronometro = Cronometro()
cronometro.inicia()
ordenacion_por_seleccion(numeros)
cronometro.detener()
print(cronometro.lapsoDeTiempo())