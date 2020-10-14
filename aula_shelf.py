
# import shelve
 
# class Person:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
 
# with shelve.open('shelf1.shelve') as db:
#     db['obi1'] = Person('Helena', '001')
#     db['ani'] = Person('Julio', '002')
#     db['a_list'] = [2, 3, 5]
#     db['delete_me'] = 'teremos que apagar este aqui...'
 
#     print(list(db.keys()))
 
#     del db['delete_me']
 
#     print(list(db.keys()))
 
#     print('delete_me' in db)
#     print('ani' in db)
 
#     a_list = db['a_list']
#     a_list.append(7)
#     db['a_list'] = a_list
#     print(db['a_list'])

import shelve

with shelve.open('shelf2.shelve', writeback=True) as db:
    db['a_list'] = [11, 13, 17]
    db['a_list'].append(19)           # anexo no local
    print(db['a_list'])
    
    

