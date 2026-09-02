class EcuacionLineal:
    # b constructor elementos abcdef
    def __init__(self, a: float, b: float, c: float, d: float, e: float, f: float):
        # a los atributos privados
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f

    # c Devuelve verdad si ad - bc != 0
    def tieneSolucion(self) -> bool:
        return (self._a * self._d - self._b * self._c) != 0

    # d Solucion pa x (ed-bf)/(ad-bc)
    def getX(self) -> float:
        denominador = self._a * self._d - self._b * self._c
        numerador = self._e * self._d - self._b * self._f
        return numerador / denominador

    # d solucion pa y (af-ec)/(ad-bc)
    def getY(self) -> float:
        denominador = self._a * self._d - self._b * self._c
        numerador = self._a * self._f - self._e * self._c
        return numerador / denominador


# Programa de prueba
def probar_ecuacion():
    entrada = input("Ingrese a, b, c, d, e, f: ").split()
    
    if len(entrada) == 6:
        a, b, c, d, e, f = map(float, entrada)
        sistema = EcuacionLineal(a, b, c, d, e, f)
        
        if sistema.tieneSolucion():
            print(f"x = {sistema.getX()}, y = {sistema.getY()}")
        else:
            print("La ecuación no tiene solución")

if __name__ == "__main__":
    probar_ecuacion()