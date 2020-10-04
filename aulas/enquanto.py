# loop enquanto

n = 42
remainders = []
while n > 0:
    remainder = n % 2                 # restos da divisão por 2
    remainders.insert(0, remainder)   # mantemos registro dos restos
    n //= 2

print(remainders)


