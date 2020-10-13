
# import sys
# import json
 
# data = {
#     'big_number': 2 ** 3141,
#     'max_float': sys.float_info.max,
#     'a_list': [2, 3, 5, 7],
# }
 
# json_data = json.dumps(data)
# data_out = json.loads(json_data)
# print(data == data_out)

# import json
 
# info = {
#     'full_name': 'Sherlock Holmes',
#     'address': {
#         'street': '221B Baker St',
#         'zip': 'NW1 6XE',
#         'city': 'London',
#         'country': 'UK',
#     }
# }
 
# print(json.dumps(info, indent=2, sort_keys=True))


import json

data_in = {
    'a_tuple': (1, 2, 3, 4, 5),
}

json_data = json.dumps(data_in)
print(json_data)
data_out = json.loads(json_data)
print(data_out)







