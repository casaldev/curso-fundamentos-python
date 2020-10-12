# from datetime import date, timedelta

# today = date.today()
# tomorrow = today + timedelta(days=1)
# products = [
#   {'sku': '1', 'expiration_date': today, 'price': 100.00},
#   {'sku': '2', 'expiration_date': tomorrow, 'price': 50.00},
#   {'sku': '3', 'expiration_date': today, 'price': 20.00},
# ]

# for product in products:
#     if product['expiration_date'] != today:
#         continue
#     product['price'] *= 0.8
#     print(f"O preço por sku {product['sku']} agora é {product['price']}")

# items = [0, None, 0.0, True, 0, 7]
# found = False
# for item in items:
#     print('Item de escaneamento', item)
#     if item:
#         found = True
#         break

# if found:
#     print('Pelo menos um item avaliado como True')
# else:
#     print('Todos os itens avaliados como False')

class DriverException(Exception):
    pass

people = [('Helena', 17), ('André', 13), ('Débora', 13), ('Julio', 16)] 

for person, age in people:
    if age >= 18:
        driver = (person, age)
        break

else:
    raise DriverException('Motorista não encontrado')