
# def factorial(n):
#     if n in (0, 1):   # caso base
#         return 1
#     return factorial(n - 1) * n   # caso recursivo


# def is_multiple_of_five(n):
#     return not n % 5

# def get_multiples_of_five(n):
#     return list(filter(is_multiple_of_five, range(n)))


# def get_multiples_of_five(n):
#     return list(filter(lambda k: not k % 5, range(n)))

# exemplo 1: adição
def adder(a, b):
    return a + b

# é equivalente a:
adder_lambda = lambda a, b: a + b
print(adder_lambda(10, 5))

# examplo 2: Maiúsculas
def to_upper(s):
    return s.upper()

# é equivalente a:
to_upper_lambda = lambda s: s.upper()
print(to_upper_lambda('julio'))

greet_lambda = lambda first, last: f"Olá {first} {last}!"
print(greet_lambda('Julio', 'Felipe'))