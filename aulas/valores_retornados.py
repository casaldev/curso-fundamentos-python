
# def func():
#     pass

# func()      # o retorno desta chamada não será coletado. Está perdido.
# a = func()  # o retorno desta em vez disso é coletado em 'a'
# print(a)

# def factorial(n):
#     if n in(0, 1):
#         return 1
#     result = n
#     for k in range(2, n):
#         result *= k
#     return result

# f5 = factorial(5)
# print(f5)




# from functools import reduce
# from operator import mul

# def factorial(n):
#     return reduce(mul, range(1, n + 1), 1)

# f5 = factorial(5)
# print(f5)


def moddiv(a, b):
    return a // b, a % b

print(moddiv(20, 7))

