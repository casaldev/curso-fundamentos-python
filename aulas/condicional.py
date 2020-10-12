# late = True
# if late:
#     print('Vou ligar para o meu gerente!')
# else:
#     print('Não preciso ligar para meu gerente')

# chovendo = False
# if chovendo:
#     print('Vou pegar o guarda-chuva!')
# else:
#     print('Vou deixa-lo em casa!')

# dependents = 0
# dependent_value = 189.59

# if dependents == 1:
#     print(dependent_value)
# elif dependents >= 2:
#     print(dependents * dependent_value)
# else:
#     print(0.0)

""" salary = 3700.00
if salary <= 1903.00:
    print("Você está isento de pagar a tributação!")
elif salary >= 1903.99:
    if salary <= 2826.66:
        print("Sua aliquota é de 7.5% e a parcela a deduzir é de R$ 142.80")
    elif salary <= 3751.05:
        print("Sua aliquota é de 15% e a parcela a deduzir é de R$ 354.80")
    elif salary <= 4664.05:
        print("Sua aliquota é de 22% e a parcela a deduzir é de R$ 636.13")
    else:
        print("Sua aliquota é de 27% e a parcela a deduzir é de R$ 869.36") """

# order_total = 200
# if order_total > 100:
#     discount = '10%'
# else:
#     discount = 0

# print(order_total, discount)

# discount = '10%' if order_total > 100 else 0
# print(order_total, discount)

order_total = 500
discount = order_total * 0.10 if order_total > 100 else order_total
print(order_total, discount) 