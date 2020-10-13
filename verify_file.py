
# import os
 
# filename = 'zen_python.txt'
# path = os.path.dirname(os.path.abspath(filename))
 
# print(os.path.isfile(filename))
# print(os.path.isdir(path))
# print(path)

# from collections import Counter
# from string import ascii_letters
 
# chars = ascii_letters + ' '
 
# def sanitize(s, chars):
#     return ''.join(c for c in s if c in chars)
 
# def reverse(s):
#     return s[::-1]
 
# with open('zen_python.txt') as stream:
#     lines = [line.rstrip() for line in stream]
 
# with open('nohtyp_nez.txt', 'w') as stream:
#     stream.write('\n'.join(reverse(line) for line in lines))
 
# # agora podemos calcular algumas estatísticas
# lines = [sanitize(line, chars) for line in lines]
# whole = ' '.join(lines)
# cnt = Counter(whole.lower().split())
# print(cnt.most_common(3))


import shutil
import os
 
BASE_PATH = 'ops_example'  # this will be our base path
os.mkdir(BASE_PATH)
 
path_b = os.path.join(BASE_PATH, 'A', 'B')
path_c = os.path.join(BASE_PATH, 'A', 'C')
path_d = os.path.join(BASE_PATH, 'A', 'D')
 
os.makedirs(path_b)
os.makedirs(path_c)
 
for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(os.path.join(path_b, filename), 'w', encoding='utf-8') as stream:
        stream.write(f'Alguns conteúdos aqui em {filename}\n')
 
shutil.move(path_b, path_d)
 
shutil.move(
    os.path.join(path_d, 'ex1.txt'),
    os.path.join(path_d, 'ex1d.txt')
)
