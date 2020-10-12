
""" def get_squares(n):       # abordagem clássica da função
    return [x ** 2 for x in range(n)]

print(get_squares(10))


def get_squares_gen(n):   # abordagem do gerador
    for x in range(n):
        yield x ** 2      # nós armazenamos, não retornamos

print(list(get_squares_gen(10))) """


# def get_squares(n):   # abordagem do gerador
#     for x in range(n):
#         print(x ** 2)
#         #return x ** 2      # nós cedemos, não retornamos

# print(list(get_squares(10)))

""" def get_squares_gen(n):
    for x in range(n):
        yield x ** 2

squares = get_squares_gen(4)      # criação do objeto gerador
print(squares)

print(next(squares))    # imprime: 0
print(next(squares))    # imprime: 1
print(next(squares))    # imprime: 4
print(next(squares))    # imprime: 9

# o seguinte aumenta a StopIteration à medida que o gerador se esgota...
# qualquer nova chamada para a próxima irá continuar a aumentar a StopIteration
print(next(squares)) """

""" def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q ** k
        if result <= 100000:
            yield result
        else:
            return
        k += 1

for n in geometric_progression(2, 5):
    print(n) """

""" def get_squares_gen(n):
    for x in range(n):
        yield x ** 2

squares = get_squares_gen(3)
print(squares.__next__())       # prints: 0
print(squares.__next__())       # prints: 1
print(squares.__next__())       # prints: 4

# o seguinte aumenta a StopIteration à medida que o gerador se esgota...
# qualquer nova chamada para a próxima irá continuar a aumentar a StopIteration
print(squares.__next__()) """

""" def print_squares(start, end):
    for n in range(start, end):
        yield n ** 2

for n in print_squares(2, 5):
    print(n) 


def print_squares(start, end):
    yield from  (n ** 2 for n in range(start, end))

for n in print_squares(2, 5):
    print(n)


cubes = [k**3 for k in range(10)]       # list regula
print(cubes)
print(type(cubes))

cubes_gen = (k**3 for k in range(10))   # criado como gerador
print(cubes_gen)
print(type(cubes_gen))

_=list
print(_(cubes_gen))                     # isto irá esgotar o gerador
print(_(cubes_gen))     """                 # nada mais a oferecer


def adder(*n):
    return sum(n)

s1 = sum(map(lambda *n: adder(*n), range(100), range(1, 101)))
s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))
print(s1, s1 == s2)


cubes = [x**3 for x in range(10)]
_=list
odd_cubes1 = filter(lambda cube: cube % 2, cubes)
odd_cubes2 = (cube for cube in cubes if cube % 2)
print(_(odd_cubes1))
print(_(odd_cubes2))

N = 20
cubes1 = map(lambda n: (n, n**3),
             filter(lambda n: n% 3 == 0 or n % 5 == 0, range(N)))
cubes2 = ((n, n**3) for n in range(N) if n % 3 == 0 or n % 5 == 0)

print(_(cubes1))
print(_(cubes2))


s1 = sum([n**2 for n in range(10**6)])
s2 = sum((n**2 for n in range(10**6)))
s3 = sum(n**2 for n in range(10**6))

s = sum([n**2 for n in range(100**8)])     # isto está morto
print(s)


s = sum(n**2 for n in range(100**8))
print(s)
