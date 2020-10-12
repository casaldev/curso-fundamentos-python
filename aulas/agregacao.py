# print(any([False, False, False]))

# print(all([True, True, True]))

#print(all(cities == cities.title() for cities in (['Belo Horizonte', 'São Paulo', 'Rio de Janeiro'])))

# def is_prime(x):
#     if x > 1:
#         for n in range(2, x):
#             if x % n == 0:
#                 return False
#         return True
#     return True

# print(any(is_prime(x) for x in range(1328, 1361)))

late = True
workday = False
if all([late, workday]):
    print('Eu preciso ligar para o meu gerente')
else:
    print('Eu não preciso ligar para o meu gerente')