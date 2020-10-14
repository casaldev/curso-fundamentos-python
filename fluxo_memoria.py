
# import io

# with io.StringIO() as stream:
#     stream.write('Fundamentos de Python.\n')
#     print('Bem-vindo ao mundo Python!', file=stream)

#     contents = stream.getvalue()
#     print(contents)
#     stream.close()


# import requests

# urls = {
#     'get': 'https://httpbin.org/get?title=fundamentos+de+python',
#     'headers': 'https://httpbin.org/headers',
#     'ip': 'https://httpbin.org/ip',
#     'user-agent': 'https://httpbin.org/user-agent',
#     'UUID': 'https://httpbin.org/uuid',
# }
 
# def get_content(title, url):
#     resp = requests.get(url)
#     print(f'Response for {title}')
#     print(resp.json())
 
# for title, url in urls.items():
#     get_content(title, url)
#     print('-' * 40)

import requests

url = 'https://httpbin.org/post'
data = dict(title='Fundamentos de Python')

resp = requests.post(url, data=data)
print('Response for POST')
print(resp.json())





