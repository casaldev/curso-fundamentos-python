
# n = 3
# address = "Rua Correia de Melo, 1234"
# employee = {
#     'age': 38,
#     'role': 'Extractive metallurgical engineer',
# }

# print(n)
# print(address)
# print(employee)

# from library.second_floor.section_x.row_three import book

# def my_function():
#     test = 1        # isto é definido no escopo da função
#     print('my_function:', test)
    
# test = 0            # isto é definido no escopo global
# my_function()
# print('global', test)

# def outer():
#     test = 1      # escopo externo

#     def inner():  
#         test = 2  # escopo interno
#         print('inner:', test)
    
#     inner()
#     print('outer:', test)

# test = 0           # escopo global
# outer()
# print('global:', test)

# def outer():
#     test = 1      # escopo externo

#     def inner():  
#         nonlocal test
#         test = 2  # escopo de fechamento mais próximo (que é 'externo')
#         print('inner:', test)
    
#     inner()
#     print('outer:', test)

# test = 0           # escopo global
# outer()
# print('global:', test)


def outer():
    test = 1      # escopo externo

    def inner():  
        global test
        test = 2  # escopo global
        print('inner:', test)
    
    inner()
    print('outer:', test)

test = 0           # escopo global
outer()
print('global:', test)




