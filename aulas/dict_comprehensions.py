# from string import ascii_lowercase

# lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
# print(lettermap)

""" lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))
print(lettermap)
 """

""" word = 'Hello'
swaps = {c: c.swapcase() for c in word}
print(swaps)

positions = {c: k for k, c in enumerate(word)}
print(positions) """

word = 'Hello'
letters1 = set(c for c in word)
letters2 = {c for c in word}
print(letters1)
print(letters1 == letters2)

