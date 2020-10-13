
# f = open('zen_python.txt', 'rt', encoding='utf-8')    # r: read, t: text

# for line in f.readlines():
#     print(line.strip())             # remove espaços em branco e mostra na tela

# f.close()

# try:
#     f = open('zen_python.txt', 'rt', encoding='utf-8')    # r: read, t: text
#     for line in f.readlines():
#         print(line.strip())     # remove espaços em branco e mostra na tela
# finally:
#     f.close()


# try:
#     f = open('zen_python.txt', 'rt', encoding='utf-8')    # rt é padrão
#     for line in f:                      # vamos interar diretamento no f 
#         print(line.strip())     
# finally:
#     f.close()


# with open('zen_python.txt', 'rt', encoding='utf-8') as f:
#     for line in f:
#         print(line.strip())

# with open('print_example.txt', 'w') as fw:
#     print('Ei, eu estou imprimindo em um arquivo!!!', file=fw)

# with open('zen_python.txt') as f:
#     lines = [line.rstrip() for line in f]

# with open('zen_python_copy.txt', 'w') as fw:
#     fw.write('\n'.join(lines))

# with open('example.bin', 'wb') as fw:
#     fw.write(b'Estes sao dados binarios...')
 
# with open('example.bin', 'rb') as f:
#     print(f.read())

with open('write_x.txt', 'x') as fw:
    fw.write('Escrevendo na linha 1') # isto é bem sucedido
 
with open('write_x.txt', 'x') as fw:
    fw.write('Escrevendo na linha 2') # isto falha


