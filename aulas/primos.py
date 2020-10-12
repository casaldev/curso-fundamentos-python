
# primes = []                     # isto conterá os números primos no final
# upto = 100                      # limite inclusive - até = 100
# for n in range(2, upto + 1):
#     is_prime = True             # flag is_prime, nova a cada iteração
#     for divisor in range(2, n):
#         if n % divisor == 0:
#             is_prime = False
#             break
#     if is_prime:                # verifica a flag
#         primes.append(n)
# print(primes)

primes = []                     # isto conterá os números primos no final
upto = 100                      # limite inclusive - até = 100
for n in range(2, upto + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:                       # verifica a flag
        primes.append(n)
print(primes)


customers = [
    dict(id=1, total=200.00, coupon_code='F20'),   # Fixo, R$20.00
    dict(id=2, total=150.00, coupon_code='P30'),   # Variável, 30%
    dict(id=3, total=100.00, coupon_code='F50'),   # Variável, 50%
    dict(id=4, total=110.00, coupon_code='F15'),   # Fixo, R$15.00
]

for customer in customers:
    code = customer['coupon_code']
    if code == 'F20':
        customer['discount'] = 20.0
    elif code == 'F15':
        customer['discount'] = 15.0
    elif code == 'P30':
        customer['discount'] = customer['total'] * 0.3
    elif code == 'P50':
        customer['discount'] = customer['salary'] * 0.5
    else:
        customer['discount'] = 0.0

for customer in customers:
    print(customer['id'], customer['total'], customer['discount']) 


customers = [
    dict(id=1, total=200.00, coupon_code='F20'),   # Fixo, R$20.00
    dict(id=2, total=150.00, coupon_code='P30'),   # Variável, 30%
    dict(id=3, total=100.00, coupon_code='F50'),   # Variável, 50%
    dict(id=4, total=110.00, coupon_code='F15'),   # Fixo, R$15.00
]

discount = {
    'F20': (0.0, 20.0),
    'P30': (0.3, 0.0),
    'P50': (0.5, 0.0),
    'F15': (0.0, 15.0),
}

for customer in customers:
    code = customer['coupon_code']
    percent, fixed = discount.get(code, (0.0, 0.0))
    customer['discount'] =  percent * customer['total'] + fixed

for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])