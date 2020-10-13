class Shape:
    geometric_type = 'Generic Shape'

    def area(self):                     # Isto atua como porta-objetos para a interface
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type


class Plotter:
    def plot(self, ratio, topleft):
        # Imagine uma boa lógica de plotagem aqui ...
        print(f'Plotando em {topleft}, proporção {ratio}')


class Polygon(Shape, Plotter):          # classe base para polígonos
    geometric_type = 'Polygon'


class RegularPolygon(Polygon):          # É um Poligono
    geometric_type = 'Regular Polygon'
    
    def __init__(self, side):
        self.side = side


class RegularHexagon(RegularPolygon):   # É um poligono regular
    geometric_type = 'RegularHexagon'
    
    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)


class Square(RegularPolygon):           # É um poligono regular
    geometric_type = 'Square'
    
    def area(self):
        return self.side * self.side


hexagon = RegularHexagon(10)
print(hexagon.area())
print(hexagon.get_geometric_type())
hexagon.plot(0.8, (75, 77))

square = Square(12)
print(square.area())
print(square.get_geometric_type())
square.plot(0.93, (74, 75))

print(square.__class__.__mro__)

