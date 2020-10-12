
A = 100
ex1 = [A for A in range(5)]
print(A)

ex2 = list(A for A in range(5))
print(A)

ex3 = dict((A, 2 * A) for A in range(5))
print(A)

ex4 = set(A for A in range(5))
print(A)

s = 0
for A in range(10):
    s += A
    print(s)
    print(A)
print(A)
print(globals())



A = 100

ex1 = [A for A in range(5)]
print(A)

ex2 = list(A for A in range(5))
print(A)

ex3 = dict((A, 2 * A) for A in range(5))
print(A)

ex4 = set(A for A in range(5))
print(A)

s = 0
for A in range(10):
    s += A
print(A)
print(globals())

