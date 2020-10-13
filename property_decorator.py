# Primeira versão - sem lógica de alcance
class Person:
    def __init__(self, age):
        self.age = age              # qualquer um pode modificar isto livremente


# Segunda versão - formato comumente usado em outras linguagens, por exemplo, Java
# private _age variable, getter and setter
class PersonWithAccessors:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('A idade deve estar dentro de [18, 99]')


# Terceira versão - Pythonica; utiliza decoradores
class PersonPythonic:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('A idade deve estar dentro de [18, 99]')


person = PersonPythonic(39)
print(person.age)                   # Aviso que acessamos como atributo de dados
person.age = 42                     # Aviso que acessamos como atributo de dados
print(person.age)                   
person.age = 100                    # ValueError: A idade deve estar dentro de [18, 99]


