# Exemplo programação condicional

"""
Atrasado está definido como verdadeiro,
nesse caso "Eu preciso ligar para o meu gerente!"
"""
# Cláusula if
late = True
if late:
    print('Eu preciso ligar para o meu gerente!')

"""
Atrasado está definido como False,
nesse caso "Eu não preciso ligar para o meu gerente!"
"""
late = False
if late:
    print('Eu preciso ligar para o meu gerente')
else:
    print('Eu não preciso ligar para o meu gerente')


# else, elif
dependents = 2
dependent_value = 189.59

if dependents == 1:
    print(dependent_value)
elif dependents >= 2:
    print(dependents * dependent_value)
else:
    print(0.0)


# ifs aninhados

salary = 5000.00
if salary <= 1903.00:
    print("Você está isento de pagar a tributação")
elif salary >= 1903.99:
    if salary <= 2826.66:
        print("Sua aliquota é de 7.5% e a parcela a deduzir de R$ 142.80")
    elif salary <= 3751.05:
        print("Sua aliquota é de 15% e a parcela a deduzir de R$ 354.80")
    elif salary <= 4664.05:
        print("Sua aliquota é de 22% e a parcela a deduzir de R$ 636.13")
    else:
         print("Sua aliquota é de 27% e a parcela a deduzir de R$ 869.36")



order_total = 200    # Total do pedido

# Forma clássica de if/else
if order_total > 100:
    discount = 10
else:
    discount = 0
print(order_total, discount)

# Operador ternário
discount = 10 if order_total > 100 else 0
print(order_total, discount)


