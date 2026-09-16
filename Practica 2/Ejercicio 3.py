class Vector3D:
    # Constructor de la clase
    def __init__(self, a1=0.0, a2=0.0, a3=0.0):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
    # a suma de dos vectores con sobrecarga +
    def __add__(self, otro):
        return Vector3D(self.a1 + otro.a1, self.a2 + otro.a2, self.a3 + otro.a3)
    # b multi de un escalar r por un vector sobrecarga *
    def __mul__(self, r):
        return Vector3D(self.a1 * r, self.a2 * r, self.a3 * r)
    # c longitud de un vector (Magnitud)
    def longitud(self):
        return (self.a1**2 + self.a2**2 + self.a3**2) ** 0.5
    # division por un escalar (Sobrecarga del operador / útil para la normal)
    def __truediv__(self, r):
        return Vector3D(self.a1 / r, self.a2 / r, self.a3 / r)
    # d normal de un vector o vector unitario
    def normal(self):
        lon = self.longitud()
        # reutilizando la sobrecarga de division
        return self / lon 
    # e producto escalar de a y b
    def producto_escalar(self, otro):
        return (self.a1 * otro.a1) + (self.a2 * otro.a2) + (self.a3 * otro.a3)
    # f producto vectorial de a y b
    def producto_vectorial(self, otro):
        c1 = (self.a2 * otro.a3) - (self.a3 * otro.a2)
        c2 = (self.a3 * otro.a1) - (self.a1 * otro.a3)
        c3 = (self.a1 * otro.a2) - (self.a2 * otro.a1)
        return Vector3D(c1, c2, c3)
    # metodo para imprimir el vector (sobrecarga para mostrarlo)
    def __str__(self):
        return "({}, {}, {})".format(self.a1, self.a2, self.a3)

if __name__ == "__main__":
    a = Vector3D(1, 2, 3)
    b = Vector3D(4, 5, 6)
    
    print("Vector a:", a)
    print("Vector b:", b)
    # a Suma
    c = a + b
    print("Suma (a + b):", c)
    # b Multiplicación por escalar
    r = 2
    mult = a * r
    print("Multiplicación por escalar (2 * a):", mult)
    # c Longitud
    print("Longitud de a (|a|):", a.longitud())
    # d Normal
    print("Normal de a:", a.normal())
    # e Producto escalar
    print("Producto escalar (a . b):", a.producto_escalar(b))
    # f Producto vectorial
    print("Producto vectorial (a x b):", a.producto_vectorial(b))   