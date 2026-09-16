from multimethod import multimethod
class MiPunto:
    # b y c Constructor sin argumentos y con argumentos especificados
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    # a Metodos getter para x e y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    # d Metodo distancia que recibe un objeto del tipo MiPunto
    @multimethod
    def distancia(self, otro: object):
        return ((self.x - otro.get_x())**2 + (self.y - otro.get_y())**2) ** 0.5
    # e Metodo distancia (SOBRECARGADO) que recibe las coordenadas x e y
    @multimethod
    def distancia(self, x_otro: float, y_otro: float):
        return ((self.x - x_otro)**2 + (self.y - y_otro)**2) ** 0.5
    # Sobrecarga 
    def __str__(self):
        return "(x={}, y={})".format(self.x, self.y)


if __name__ == "__main__":
    # sin argumentos
    p1 = MiPunto()
    # punto (10, 30.5) con argumentos
    p2 = MiPunto(10.0, 30.5)
    print("Primer punto:", p1)
    print("Segundo punto:", p2)
    distancia_obj = p1.distancia(p2)
    print("Distancia calculada (enviando objeto MiPunto):", distancia_obj)
    distancia_coord = p1.distancia(10.0, 30.5)
    print("Distancia calculada (enviando coordenadas):", distancia_coord)