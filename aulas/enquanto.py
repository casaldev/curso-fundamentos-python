# loop enquanto

# n = 42
# remainders = []
# while n > 0:
#     remainder = n % 2                   # restos da divisão por 2
#     remainders.insert(0, remainder)     # mantemos registro dos restos
#     n //= 2                             # dividimos n por 2

# print(remainders)


# n = 42
# remainders = []
# while n > 0:                            # condição
#     n, remainder = divmod(n, 2)
#     remainders.insert(0, remainder)

# print(remainders)


people = ['Helena', 'Débora', 'Julio', 'André']
ages = [36, 2, 42, 6]
position = 0                        # inicialização
while position < len(people):       # condição
    person = people[position]
    age = ages[position]
    print(person, age)
    position += 1                   # atualização
    