
# def fibonacci(N):
#     """Devolver todos os números de fibonacci até o N."""
#     result = [0]
#     next_n = 1
#     while next_n <= N:
#         result.append(next_n)
#         next_n = sum(result[-2:])
#     return result

# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(50))

# def fibonacci(N):
#     """Devolver todos os números de fibonacci até o N."""
#     yield 0
#     if N == 0:
#         return
#     a = 0
#     b = 1
#     while b<= N:
#         yield b
#         a, b = b, a + b

# _=list
# print(_(fibonacci(0)))
# print(_(fibonacci(1)))
# print(_(fibonacci(50)))

def fibonacci(N):
    """Devolver todos os números de fibonacci até o N."""
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

_=list
print(_(fibonacci(0)))
print(_(fibonacci(1)))
print(_(fibonacci(50)))