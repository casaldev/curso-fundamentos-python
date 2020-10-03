# Considerando apenas números positivos
def is_prime(x):
    if x > 1:
        for n in range(2, x):
            if (x % n) == 0:
                return False
        return True
    return True
   
print(any(is_prime(x) for x in range(1328, 1361)))


late = True
if late:
    print('Eu preciso ligar para o meu gerente')
else:
    print('Eu não preciso ligar para o meu gerente')


late = True
workday = True
if all([late, workday]):
    print('Eu preciso ligar para o meu gerente')
else:
    print('Eu não preciso ligar para o meu gerente')
    

