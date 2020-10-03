# for loop

for number in [0, 1, 2, 3, 4]:
    print(number)

for number in range(5):
    print(number)

# Interando sobre uma sequência

surnames = ['Souza', 'Rocha', 'Oliveira']
for surname in surnames:
    print(surname)

# Iterando em várias sequências
# Nível ineficiente
people = ['Helena', 'Débora', 'Julio', 'André']
ages = [36, 2, 42, 6]
for position in range(len(people)):
    person = people[position]
    age = ages[position]
    print(person, age)

# Nível melhor, mas não perfeito
people = ['Helena', 'Débora', 'Julio', 'André']
ages = [36, 2, 42, 6]
for position, person in enumerate(people):
    age = ages[position]
    print(person, age)

# Nível muito melhor
people = ['Helena', 'Débora', 'Julio', 'André']
ages = [36, 2, 42, 6]
for person, age in zip(people, ages):
    print(person, age)

# Expandindo
people = ['Helena', 'Débora', 'Julio', 'André']
ages = [36, 2, 42, 6]
family = ['Mãe', 'Filha', 'Pai', 'Filho']
for person, age, family in zip(people, ages, family):
    print(person, age, family)

# Explodindo
people = ['Helena', 'Débora', 'Julio', 'André']
ages = [36, 2, 42, 6]
family = ['Mãe', 'Filha', 'Pai', 'Filho']
for data in zip(people, ages, family):
    person, age, family = data
    print(person, age, family)








