# from itertools import count

# for n in count(5, 3):
#     if n > 20:
#         break
#     print(n, end=', ') # ao invés de nova linha, vírgula e espaço


# from itertools import compress
# data = range(10)
# even_selector = [1, 0] * 10
# odd_selector = [0, 1] * 10

# even_numbers = list(compress(data, even_selector))
# odd_numbers = list(compress(data, odd_selector))

# print(odd_selector)
# print(list(data))
# print(even_numbers)
# print(odd_numbers)

from itertools import permutations
print(list(permutations('ABC')))

