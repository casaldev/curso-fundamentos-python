# primes = []
# upto = 100
# for n in range(2, upto + 1):
#     is_prime = True
#     for divisor in range(2, n):
#         if n % divisor == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(n)
# print(primes)

# primes = []
# upto = 100
# for n in range(2, upto + 1):
#     for divisor in range(2, n):
#         if n % divisor == 0:
#             break
#     else:
#         primes.append(n)
# print(primes)

# customers = [
#     dict(id=1, total=200.00, coupon_code='F20'),
#     dict(id=2, total=150.00, coupon_code='P30'),
#     dict(id=3, total=100.00, coupon_code='P50'),
#     dict(id=4, total=110.00, coupon_code='F15'),
# ]

# for customer in customers:
#     code = customer['coupon_code']
#     if code == 'F20':
#         customer['discount'] = customer['total'] - 20.00
#     elif code == 'F15':
#         customer['discount'] = customer['total'] - 15.00
#     elif code == 'P30':
#         customer['discount'] = customer['total'] * 0.3
#     elif code == 'P50':
#         customer['discount'] = customer['total'] * 0.5
#     else:
#         customer['discount'] = 0.0

# for customer in customers:
#     print(customer['id'], customer['total'], customer['discount'])


# customers = [
#     dict(id=1, total=200.00, coupon_code='F20'),
#     dict(id=2, total=150.00, coupon_code='P30'),
#     dict(id=3, total=100.00, coupon_code='P50'),
#     dict(id=4, total=110.00, coupon_code='F15'),
# ]

# discount = {
#     'F20': (0.0, 20.0),
#     'P30': (0.3, 0.0),
#     'P50': (0.5, 0.0),
#     'F15': (0.0, 15.0),
# }

# for customer in customers:
#     code = customer['coupon_code']
#     percent, fixed = discount.get(code, (0.0, 0.0))
#     customer['discount'] = percent * customer['total'] + fixed

# for customer in customers:
#     print(customer['id'], customer['total'], customer['discount'])


# def get_primes_numbers(upto):
#         primes = []
#         for n in range(2, upto + 1):
#             for divisor in range(2, n):
#                 if n % divisor == 0:
#                     break
#             else:
#                 primes.append(n)
#         return primes

# print(get_primes_numbers(50))
# print(get_primes_numbers(100))

def calculate_price_with_icms(price, icms):
    return price * (100 + icms) / 100

print(calculate_price_with_icms(100, 25))