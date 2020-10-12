
# def my_function(input):
#     ...
#     ...
#     return output

# primes = []                     
# upto = 100                      
# for n in range(2, upto + 1):
#     for divisor in range(2, n):
#         if n % divisor == 0:
#             break
#     else:                       
#         primes.append(n)
# print(primes)


# def get_primes_numbers(upto):
#     primes = []
#     for n in range(2, upto + 1):
#         for divisor in range(2, n):
#             if n % divisor == 0:
#                 break
#         else:                      
#             primes.append(n)
#     return primes

# print(get_primes_numbers(50))
  

# def fetch_data(data):
#     pass

# def parse_data(data):
#     pass

# def filter_data(data):
#     pass

# def polish_data(data):
#     pass

# def analyse(data):
#     pass

# class Report(self, data):
#     pass

# def do_report(data_source):
#     # busca e prepara os dados
#     data = fetch_data(data_source)
#     parsed_data = parse_data(data)
#     filtered_data = filter_data(parsed_data)
#     polished_data = polish_data(filtered_data)

#     # executa algoritmo nos dados
#     final_data = analyse(polished_data)

#     # cria e devolve o relatório
#     report = Report(final_data)
#     return report

# a = [[1, 2], [2, 4]]
# b = [[5, 1], [2, 1]]

# c = [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)]
#     for r in a]


# def matrix_mult(a, b):
#     return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)]for r in a]

# a = [[1, 2], [2, 4]]
# b = [[5, 1], [2, 1]]
# c = matrix_mult(a, b)

price = 100.00   # sem ICMS
final_price1 = price * 1.25
final_price2 = price + price / 4.0
final_price3 = price * (100 + 25) / 100.00
final_price4 = price + price * 0.25

print(final_price1)


def calculate_price_with_icms(price, icms):
    return price * (100 + icms) / 100

print(calculate_price_with_icms(100.00, 25))



