# for number in [0, 1, 2, 3, 4]:
#     print(number)

# for number in range(5):
#     print(number)

# for number in range(10):
#     print(number)

# surnames = ['Souza', 'Rocha', 'Oliveira']
# for surname in surnames:
#     print(surname)

# people = ['Helena', 'Débora', 'Julio', 'André']
# ages = [36, 2, 42, 6]
# for position in range(len(people)):
#     print(f'{people[position]} - {position}')

    # person = people[position]
    # age = ages[position]
    # print(person, age)

# people = ['Helena', 'Débora', 'Julio', 'André']
# ages = [36, 2, 42, 6]
# for position, person in enumerate(people):
#     age = ages[position]
#     print(person, age)

# people = ['Helena', 'Débora', 'Julio', 'André']
# ages = [36, 2, 42, 6]
# for person, age in zip(people, ages):
#     print(person, age)

people = ['Helena', 'Débora', 'Julio', 'André']
ages = [36, 2, 42, 6]
family = ['Mãe', 'Filha', 'Pai', 'Filho']
for data in zip(people, ages, family):
    person, age, family = data
    print(person, age, family)

