
# squares = []
# for n in range(10):
#     squares.append(n**2)
# print(squares)

# _=list
# squares = map(lambda n: n ** 2, range(10))
# print(_(squares))


# squares = [n ** 2 for n in range(10)]
# print(squares)

# usando map e filter
# sq1 = list(
#     map(lambda n: n ** 2, filter(lambda n: not n % 2, range(10)))
# )

# # equivalente, mas usando list comprehensions
# sq2 = [n ** 2 for n in range(10) if not n % 2]

# print(sq1, sq1 == sq2)

""" items = 'ABCD'

pairs = []
for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))

print(pairs)


items = 'ABCD'

pairs = [(items[a], items[b]) for a in range(len(items)) for b in range(a, len(items))]

print(pairs) """

""" from math import sqrt

mx = 10
triples = [(a, b, sqrt(a**2 + b**2))
            for a in range(1, mx) for b in range(a, mx)]
triples = filter(
  lambda triple: triple[2].is_integer(), triples)

# fazer o terceiro número na tupla inteira
triples = list(map(
  lambda triple: triple[:2] + (int(triple[2]),),triples))

print(triples) """


from math import sqrt

mx = 10
triples = [(a, b, sqrt(a**2 + b**2))
            for a in range(1, mx) for b in range(a, mx)]
triples = filter(
  lambda triple: triple[2].is_integer(), triples)

# fazer o terceiro número na tupla inteira
triples = [(a, b, int(c)) for a, b, c in triples if c.is_integer()]

print(triples)





