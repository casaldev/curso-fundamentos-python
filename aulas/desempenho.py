""" from time import time
mx = 3000

# cronometrando o loop
t = time()
floop = []
for a in range(1, mx):
    for b in range(a, mx):
        floop.append(divmod(a, b))

print(f'for loop: {time() - t:.4f} s')    # tempo decorrido

# tempo de compreensão da lista
t = time()
compr = [divmod(a, b) for a in range(1, mx) for b in range(a, mx)]

print(f'list comprehension: {time() - t:.4f} s')

# tempo da expressão geradora
t = time()
gener = list(divmod(a, b) for a in range(1, mx) for b in range(a, mx))

print(f'generation expression: {time() - t:.4f} s') """

""" from time import time
mx = 2 * 10 ** 6

t = time()
absloop = []
for n in range(mx):
    absloop.append(abs(n))
print(f'for loop: {time() - t:.4f} s')

t = time()
abslist = [abs(n) for n in range(mx)]
print(f'list comprehension: {time() - t:.4f} s')

t = time()
absmap = list(map(abs, range(mx)))
print(f'map: {time() - t:.4f} s') """

def mdc(a, b):
    """Calcula o Máximo Divisor Comum de (a, b)."""
    while b != 0:
        a, b = b, a % b
    return a

#print(mdc(20, 24))

""" N = 50

triples = sorted(                                     # 1
   ((a, b, c) for a, b, c in (                        # 2
       ((m**2 - n**2), (2 * m * n), (m**2 + n**2) )   # 3
       for m in range(1, int(N**.5) + 1)              # 4
       for n in range(1, m)                           # 5
       if (m - n) % 2 and mdc(m, n) == 1              # 6
   ) if c<=N), key=lambda *triple: sum(*triple)       # 7
)
print(triples) """

def gen_triples(N):
    for m in range(1, int(N**.5) + 1):                 # 1
        for n in range(1, m):                          # 2
            if (m - n) % 2 and mdc(m, n) == 1:         # 3
                c = m**2 + n**2                        # 4
                if c <= N:                             # 5
                    a = m**2 - n**2                    # 6
                    b = 2 * m * n                      # 7
                    yield(a, b, c)                     # 8

triples = sorted(gen_triples(50), key=lambda *triple: sum(*triple)) # 9
print(triples)