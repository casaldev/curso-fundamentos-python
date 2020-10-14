from alchemy_models import Person, Address, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

helena = Person(name='Helena Oliveira', age=36)
julio = Person(name='Julio Felipe', age=42)

helena.addresses = [
    Address(email='helena_oliveira@example.com'),
    Address(email='debora_oliveira@example.com'),
]

julio.addresses.append(Address(email='jcof@example.com'))
julio.addresses.append(Address(email='andreoliveira@example.com'))


session.add(julio)
session.add(helena)
session.commit()

helena = session.query(Person).filter(
    Person.name.like('Hel%')
).first()
print(helena, helena.addresses)

julio = session.query(Person).filter(
    Person.name == 'Julio Felipe'
).first()
print(julio, julio.addresses)

julio_id = julio.id
del julio


def display_info():
    # get all addresses first
    addresses = session.query(Address).all()

    # display results
    for address in addresses:
        print(f'{address.person.name} <{address.email}>')

    # display how many objects we have in total
    print(f'people: {session.query(Person).count()}',
          f'addresses: {session.query(Address).count()}')


display_info()

anakin = session.query(Person).get(julio_id)
session.delete(julio)
session.commit()

display_info()
