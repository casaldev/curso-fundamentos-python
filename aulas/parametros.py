
# x = 3
# def func(y):
#     print(y)

# func(x)


# x = 3
# def func(x):
#     x = 7     # definindo um x local, não mudando o global

# func(x)
# print (x)

# x = [1, 2, 3]

# def func(x):
#     x[1] = 42     # isto afeta o interlocutor!

# func(x)
# print (x)

# x = [1, 2, 3]

# def func(x):
#     x[1] = 42         # isto muda o interlocutor!
#     x = 'algo mais'   # isto aponta x para um novo objeto string

# func(x)
# print (x)

# def func(a, b, c):
#     print(a, b, c)

# func(1, 2, 3)


# def func(a, b, c):
#     print(a, b, c)

# func(a=1, c=2, b=3)


# def func(a, b=4, c=88):
#     print(a, b, c)

# func(1)
# func(b=5, a=7, c=9)
# func(42, c=9)
# func(4, 43, 44)


# def func(a, b=4, c=88):
#     print(a, b, c)

# func(b=1, c=2, 42)      # argumento posicional após a palavra-chave um

# def minimum(*n):
#     # print(type(n))    # n is a tuple
#     if n:
#         mn = n[0]
#         for value in n[1:]:
#             if value < mn:
#               mn = value
#         print(mn)

# minimum(1, 3, -7, 9)    # n = (1, 3, -7, 9)
# minimum()               # n = ()

# def func(*args):
#     print(args)

# values = (1, 3, -7, 9)
# func(values)            # equivalente a: func((1, 3, -7, 9))
# func(*values)           # equivalente a: func(1, 3, -7, 9)

# def func(**kwargs):
#     print(kwargs)

# func(a=1, b=42)
# func(**{'a': 1, 'b': 42})
# func(**dict(a=1, b=42))



# def kwo(*a, c):
#     print(a, c)

# kwo(1, 2, 3, c=7)
# kwo(c=4)
# # kwo(1, 2)           # quebras, sintaxe inválida

# def kwo2(a, b=42, *, c):
#     print(a, b, c)

# kwo2(3, b=7, c=99)
# kwo2(3, c=13)
# kwo2(3, 23)           # quebras, sintaxe inválida


# def func(a, b, c=7, *args, **kwargs):
#     print('a, b, c:', a, b, c)
#     print('args:', args)
#     print('kwargs', kwargs)

# func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})
# func(1, 2, 3, 5, 7, 9, A='a', B='b')
    

# def func_with_kwonly(a, b=42, *args, c, d=256, **kwargs):
#     print('a, b:', a, b)
#     print('c, d:', c, d)
#     print('kwargs', kwargs)

# func_with_kwonly(3, 42 , c=0, d=1, *(7, 9, 11), e='E', f='F')
# func_with_kwonly(3, 42 , *(7, 9, 11), c=0, d=1, e='E', f='F')

# def addictional(*args, **kwargs):
#     print(args)
#     print(kwargs)
    
# args1 = (1, 2, 3)
# args2 = [4, 5]
# kwargs1 = dict(option1=10, option2=20)
# kwargs2 = {'option3': 30}
# addictional(*args1, *args2, **kwargs1, **kwargs2)

# def func(a=[], b={}):
#     print(a)
#     print(b)
#     print('#' * 12)
#     a.append(len(a))      # isto afetará o valor padrão dos a's
#     b[len(a)] = len(a)    # isto afetará o valor padrão dos b's
# func()
# func()
# func()

# def func(a=[], b={}):
#     print(a)
#     print(b)
#     print('#' * 12)
#     a.append(len(a))   # isto afetará o valor padrão de um
#     b[len(a)] = len(a)  # e isto afetará a b's one

func()
func(a=[1, 2, 3], b={'B': 1})
func()

def func(a=None):
    if a is None:
        a = []
        # faça o que quiser com `a` ...