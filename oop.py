
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

# class Rectangle:
#     def __init__(self, side_a, side_b):
#         self.side_a = side_a
#         self.side_b = side_b

#     def area(self):
#         return self.side_a * self.side_b

# r1 = Rectangle(10, 4)
# print(r1.side_a, r1.side_b)
# print(r1.area())

# r2 = Rectangle(7, 3)
# print(r2.area())

# from class_inheritance import Car, RaceCar, F1Car

# car = Car()
# racecar = RaceCar()
# f1car = F1Car()
# cars = [(car, 'car'), (racecar, 'racecar'), (f1car, 'f1car')]
# car_classes = [Car, RaceCar, F1Car]

# for class1 in car_classes:
#     for class2 in car_classes:
#         is_subclass = (class1, class2)
#         msg = '{0} uma subclass de'. format(
#             'é' if is_subclass else 'não é'
#         )
#         print(class1.__name__, msg, class2.__name__)

# for car, car_name in cars:
#     for class_ in car_classes:
#         belongs = isinstance(car, class_)
#         msg = 'é um' if belongs else 'não é um'
#         print(car_name, msg, class_.__name__)


# class Course:
#     def __init__(self, title, provider, lessons):
#         self.title = title
#         self.provider = provider
#         self.lessons = lessons

# class Content(Course):
#     def __init__(self, title, provider, lessons, format_):
#         self.title = title
#         self.provider = provider
#         self.lessons = lessons
#         self.format_ = format_


# class Course:
#     def __init__(self, title, provider, lessons):
#         self.title = title
#         self.provider = provider
#         self.lessons = lessons
 
# class Content(Course):
#     def __init__(self, title, provider, lessons, format_):
#         Course.__init__(self, title, provider, lessons)
#         self.format_ = format_
 
# content = Content('Fundamentos de Python', 'casaldev', 8, 'Online')
 
# print(content.title)
# print(content.provider)
# print(content.lessons)
# print(content.format_)


# class Course:
#     def __init__(self, title, provider, lessons):
#         self.title = title
#         self.provider = provider
#         self.lessons = lessons
 
# class Content(Course):
#     def __init__(self, title, provider, lessons, format_):
#         super().__init__(title, provider, lessons)
#         # Outra maneira de fazer a mesma coisa é:
#         # super(Content, self).__init__(title, provider, lessons)
#         self.format_ = format_
 
# content = Content('Fundamentos de Python', 'casaldev', 8, 'Online')
 
# print(content.title)
# print(content.provider)
# print(content.lessons)
# print(content.format_)


# class A:
#     label = 'a'

# class B(A):
#     label = 'b'

# class C(A):
#     label = 'c'

# class D(B, C):
#     pass

# d = D()
# print(d.label) # Hipoteticamente, isto poderia ser 'b' ou 'c'.


# class A:
#     label = 'a'
 
# class B(A):
#     pass  # foi: label = 'b'
 
# class C(A):
#     label = 'c'
 
# class D(B, C):
#     pass
 
# d = D()
# print(d.label)
# print(d.__class__.mro())  # veja outra maneira de obter o MRO


# class StringUtil:

#     @staticmethod
#     def is_palindrome(s, case_insensitive=True):
#         s = ''.join(c for c in s if c.isalnum())    # permitimos apenas letras e números
#         if case_insensitive:
#             s = s.lower()   # para comparação sem distinção entre maiúsculas e minúsculas, nós colocamos s em minúsculas       
#         for c in range(len(s) // 2):
#             if s[c] != s[-c -1]:
#                 return False
#         return True

#     @staticmethod
#     def get_unique_words(sentence):
#         return set(sentence.split())    


# print(StringUtil.is_palindrome('Radar', case_insensitive=False))  
# print(StringUtil.is_palindrome('A mala nada na lama'))             
# print(StringUtil.is_palindrome('A base do teto desaba'))
# print(StringUtil.is_palindrome('Anotaram a data da maratona'))  # Latin!
 
# print(StringUtil.get_unique_words('Eu amo palindromos. Eu realmente os amo'))


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def from_tuple(cls, coords):    # cls é Point
#         return cls(*coords)

#     @classmethod
#     def from_point(cls, point):     # cls é Point
#         return cls(point.x, point.y)

# p = Point.from_tuple((3, 7))
# print(p.x, p.y)

# q = Point.from_point(p)
# print(q.x, q.y)


# class StringUtil:
 
#     @classmethod
#     def is_palindrome(cls, s, case_insensitive=True):
#         s = cls._strip_string(s)
#         if case_insensitive:
#             s = s.lower()  # Para comparação insensível a maiúsculas e minúsculas 
#         return cls._is_palindrome(s)
 
#     @staticmethod
#     def _strip_string(s):
#         return ''.join(c for c in s if c.isalnum())
 
#     @staticmethod
#     def _is_palindrome(s):
#         for c in range(len(s) // 2):
#             if s[c] != s[-c - 1]:
#                 return False
#         return True
 
#     @staticmethod
#     def get_unique_words(sentence):
#         return set(sentence.split())
 
 
# print(StringUtil.is_palindrome('A mala nada na lama'))
# print(StringUtil.is_palindrome('A mala nada no rio'))


# class A:
#     def __init__(self, factor):
#         self._factor = factor
 
#     def op1(self):
#         print(f'Op1 with factor {self._factor}...')
 
# class B(A):
#     def op2(self, factor):
#         self._factor = factor
#         print(f'Op2 with factor {self._factor}...')
 
 
# obj = B(100)
# obj.op1()
# obj.op2(42)
# obj.op1()     # <- Isso é RUIM
# print(obj.__dict__.keys())


# class A:
#     def __init__(self, factor):
#         self.__factor = factor
 
#     def op1(self):
#         print(f'Op1 with factor {self.__factor}...')
 
# class B(A):
#     def op2(self, factor):
#         self.__factor = factor
#         print(f'Op2 with factor {self.__factor}...')
 
 
# obj = B(100)
# obj.op1()
# obj.op2(42)
# obj.op1()       # Agora isso é BOM!
# print(obj.__dict__.keys())


class Weird:
    def __init__(self, s):
        self._s = s
 
    def __len__(self):
        return len(self._s)
 
    def __bool__(self):
        return '42' in self._s
 
 
weird = Weird('Olá! Eu tenho 9 anos!')
print(len(weird))
print(bool(weird))
 
weird2 = Weird('Olá! Eu tenho 42 anos!')
print(len(weird2))
print(bool(weird2))

