import math
class EcuacionCuadratica:
    # b Constructor para los argumentos abc
    def __init__(self, a: float, b: float, c: float):
        # a atributos privados
        self._a = a
        self._b = b
        self._c = c
    # c Devuelve el discriminante: b^2-4ac
    def getDiscriminante(self) -> float:
        return (self._b ** 2) - (4 * self._a * self._c)
    # d Retorna la primera raiz, si el discriminante es negativo devuelve 0
    def getRaiz1(self) -> float:
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return 0.0
        return (-self._b + math.sqrt(discriminante)) / (2 * self._a)
    # d igualito retorna la segunda raiz,igual tmb si el discriminante es negativo, devuelve 0
    def getRaiz2(self) -> float:
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return 0.0
        return (-self._b - math.sqrt(discriminante)) / (2 * self._a)

# Programa de prueba
def probar_ecuacion_cuadratica():
    entrada = input("Ingrese a, b, c: ").split()
    if len(entrada) == 3:
        a, b, c = map(float, entrada)
        ecuacion = EcuacionCuadratica(a, b, c)
        discriminante = ecuacion.getDiscriminante()
        if discriminante > 0:
            # aqui voi a redondear pal ejemplo
            r1 = round(ecuacion.getRaiz1(), 6)
            r2 = round(ecuacion.getRaiz2(), 5)
            print(f"La ecuación tiene dos raíces {r1} y {r2}")
        elif discriminante == 0:
            raiz = ecuacion.getRaiz1()
            # aqui evitamos que salga #.#
            if raiz.is_integer():
                raiz = int(raiz)
            print(f"La ecuación tiene una raíz {raiz}")
        else:
            print("La ecuación no tiene raíces reales")
if __name__ == "__main__":
    probar_ecuacion_cuadratica()