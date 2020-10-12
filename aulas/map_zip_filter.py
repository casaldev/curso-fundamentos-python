# def square1(n):
#     return n ** 2       # elevando ao quadrado  com exponenciação

# def square2(n):
#     return n * n        # elevando ao quadrado com multiplicação


# print(range(7))
# print(list(range(7)))   #colocar todos os elementos em uma lista para vê-los

# _ = list                # criar um "pseudônimo" para a lista
# print(_(range(7)))      # a mesma coisa do list(range(7))

# _ = list
# print(map(lambda *a: a, range(3)))                            # 1 interavel
# print(_(map(lambda *a: a, range(3))))                         # 1 interavel
# print(_(map(lambda *a: a, range(3), 'abc')))                  # 2 interaveis
# print(_(map(lambda *a: a, range(3), 'abc', range(4, 7))))     # 3 interaveis
# # o mapa para no iterador mais curto
# print(_(map(lambda *a: a, (), 'abc')))         # tupla vazia é a mais curta
# print(_(map(lambda *a: a, (1, 2), 'abc')))                   # (1, 2) mais curta
# print(_(map(lambda *a: a, (1, 2, 3, 4), 'abc')))             # 'abc' mais curta

# students = [
#     dict(id=0, credits=dict(math=9, physics=6, history=7)),
#     dict(id=1, credits=dict(math=6, physics=7, english=10)),
#     dict(id=2, credits=dict(math=8, physics=9, chemistry=10)),
#     dict(id=3, credits=dict(math=5, phisics=5, geography=7)),
# ]

# def decorate(student):
#     # cria uma segunda tupla (soma de créditos, estudante) a 
#     # partir do dict de estudantes
#     return (sum(student['credits'].values()), student['credits'])

# def undecorate(decorated_student):
#     # descarta a soma dos créditos, devolver o dict original do estudante
#     return decorated_student[1]

# print(sum(students[2]['credits'].values()))

# print(decorate(students[2]))



# _= list
# students = sorted(map(decorate, students), reverse=True)
# print(students)

# students = _(map(undecorate, students))
# print(students)

# _= list
# grades = [18, 23, 30, 27]                   # notas
# avgs = [22, 21, 29, 24]                     # medias
# print(_(zip(avgs, grades)))
# print(_(map(lambda *a: a, avgs, grades)))   # equivalente ao zip

# a = [5, 9, 2, 4, 7]
# b = [3, 7, 1, 9, 2]
# c = [6, 8, 0, 5, 3]

# _=list
# maxs = map(lambda n: max(*n), zip(a, b, c))
# print(_(maxs))

_=list
test = [2, 5, 8, 0, 0, 1, 0]
print(_(filter(None, test)))
print(_(filter(lambda x: x, test)))         # equivalente ao anterior
print(_(filter(lambda x: x > 4, test)))     # mantenha somente os items > 4





