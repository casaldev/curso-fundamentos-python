
""" class Simplest():
    pass

print(type(Simplest))         # que tipo é este objeto?

simp = Simplest()             # criamos uma instância de Simplest: simp
print(type(simp))             # que tipo é simp?

print(type(simp) == Simplest) # simp é uma instância de Simplest """

""" class Person:
    species = 'Human'

print(Person.species)
Person.alive = True    # adicionado dinamicamente
print(Person.alive)

man = Person()
print(man.species)      # herdado
print(man.alive)        # herdado

Person.alive = False
print(man.alive)        # herdado

man.name = 'Darth'
man.surname = 'Vader'
print(man.name, man.surname) """

""" class Point:
    x = 10
    y = 7

p = Point()
print(p.x)      # do atributo de classe
print(p.y)      # do atributo de classe

p.x = 12        # p recebe seu próprio atributo 'x'
print(p.x)      # agora encontrado na instância
print(Point.x)  # atributo de classe ainda o mesmo

del p.x         # eliminamos o atributo de instância
print(p.x)      # agora a busca tem que ir novamente para encontrar o attr
p.z = 3         # Vamos fazer disso um ponto 3D 
print(p.z)

print(Point.z)  # AttributeError """

""" class Square:
    side = 8
    def area(self):     # self é uma referência a uma instância
        return self.side ** 2

sq = Square()
print(sq.area())        # lado é encontrado na classe 
print(Square.area(sq))  # equivalente a sq.area()

sq.side = 10
print(sq.area())        # lado é encontrado na instância """


# class Price:
#     def final_price(self, icms, discount=0):
#         """Preço de retorno após a aplicação do icms e desconto fixo."""
#         return (self.net_price * (100 + icms) / 100) - discount

# p1 = Price()
# p1.net_price = 100
# print(Price.final_price(p1, 20, 10))
# print(p1.final_price(20, 10))

class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a * self.side_b

r1 = Rectangle(10, 4)
print(r1.side_a, r1.side_b)
print(r1.area())

r2 = Rectangle(7, 3)
print(r2.area())
