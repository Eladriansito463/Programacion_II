class AlgebraVectorial:
    # Sobrecarga de constructores (con valores deñ ejem)
    def __init__(self, a1=0.0, a2=0.0, a3=0.0):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
    # SOBRECARGA
    def __add__(self, b):
        return AlgebraVectorial(self.a1+b.a1, self.a2+b.a2, self.a3+b.a3)
    def __sub__(self, b):
        return AlgebraVectorial(self.a1-b.a1, self.a2-b.a2, self.a3-b.a3)
    # Sobrecargando la multiplicacion
    def __mul__(self, b):
        return (self.a1*b.a1) + (self.a2*b.a2) + (self.a3*b.a3)
    # METODOS AUX
    def mult_escalar(self, r):
        return AlgebraVectorial(self.a1*r, self.a2*r, self.a3*r)
    def prod_vectorial(self, b):
        c1 = (self.a2*b.a3) - (self.a3*b.a2)
        c2 = (self.a3*b.a1) - (self.a1*b.a3)
        c3 = (self.a1*b.a2) - (self.a2*b.a1)
        return AlgebraVectorial(c1, c2, c3)
    def longitud(self):
        return (self.a1**2 + self.a2**2 + self.a3**2) ** 0.5
    # Incisos
    # a perpendicular: |a+b|=|a-b|
    def perpendicular_a(self, b):
        suma = self + b   # usa __add__
        resta = self - b  # usa __sub__
        # Comparamos redondeado x si acaso 
        return round(suma.longitud(), 4) == round(resta.longitud(), 4)
    # c Perpendicular: a.b=0
    def perpendicular_c(self, b):
        return (self * b) == 0.0  # usa __mul__
    # f) Paralela: axb=0
    def paralela_f(self, b):
        c = self.prod_vectorial(b)
        return c.a1 == 0 and c.a2 == 0 and c.a3 == 0
    # g) Proyección de a sobre b:((a.b)/|b|^2)*b
    def proyeccion(self, b):
        escalar = (self * b) / (b.longitud() ** 2)
        return b.mult_escalar(escalar)
    # h) Componente de a en b: (a.b)/|b|
    def componente(self, b):
        return (self * b) / b.longitud()
    # Sobrecarga para imprimir
    def __str__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"

if __name__ == "__main__":
    v1 = AlgebraVectorial(1, 0, 0)
    v2 = AlgebraVectorial(0, 1, 0)
    v3 = AlgebraVectorial(2, 0, 0)

    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    print(f"Vector 3: {v3}")
    print("\n¿v1 y v2 son perpendiculares (método c)?", v1.perpendicular_c(v2))
    print("¿v1 y v3 son paralelos (método f)?", v1.paralela_f(v3))
    proy = v1.proyeccion(v3)
    print(f"Proyección de v1 sobre v3: {proy}")
    print(f"Componente de v1 en v3: {v1.componente(v3)}")