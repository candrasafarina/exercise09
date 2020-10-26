personAndPets = [
    {
        "name" : "Jhon Doe",
        "pets" : [
            {"name" : "Rooster"},
        ]
    },
    {
        "name" : "Luke Skywalker",
        "pets" : [
            {"name" : "Duck"},
            {"name" : "Camel"}
        ]
    },
    {
        "name" : "Padme Amidal",
        "pets" : [
            {"name" : "Bird"},
            {"name" : "Fish"}
        ]
    }
]

"""
for x in personAndPets:
    for p in x['pets']:
        print(p)"""



"""for x in personAndPets:
    if x['name'] == 'Padme Amidal':
        for p in x['pets']:
            print(p)"""
for x in personAndPets:
    if x['pets']:
        for u in x['name']:
            print(u)
""""
class personAndPets():

    def __init__(self, person=None, pet=None):
        self.person = person
        self.pet = pet

    def tampilkan_data(self):
        print('Nama pemilik :', self.person)
        print('Nama :', self.pet)

personAndPets1  = personAndPets("Jhone Doe","Rooster, Dog",)
personAndPets2 = personAndPets("Luke skywalker", "Duck, Camel")
personAndPets3 = personAndPets("Padme Amidal", "Bird, Fish")
personAndPets1.tampilkan_data()
personAndPets2.tampilkan_data()
personAndPets3.tampilkan_data()

"""
"""
personAndPets = [
    {
        "name" : "Jhon Doe",
        "pets" : [
            {"name" : "Rooster"},
        ]
    },
    {
        "name" : "Luke Skywalker",
        "pets" : [
            {"name" : "Duck"},
            {"name" : "Camel"}
        ]
    },
    {
        "name" : "Padme Amidal",
        "pets" : [
            {"name" : "Bird"},
            {"name" : "Fish"}
        ]
    }
]
class personPets:
    def __init__(self, person=None, pet=None):
        self.person = person
        self.pet = pet
    def getPetperson(self):
        for x in personAndPets:
            print(x)
    
pp = personPets()
pp.getPetperson()
"""

personAndPets = [
    {
        "name" : "Jhon Doe",
        "pets" : [
            {"name" : "Rooster"},
        ]
    },
    {
        "name" : "Luke Skywalker",
        "pets" : [
            {"name" : "Duck"},
            {"name" : "Camel"}
        ]
    },
    {
        "name" : "Padme Amidal",
        "pets" : [
            {"name" : "Bird"},
            {"name" : "Fish"}
        ]
    }
]
"""
class personPets2:
    def __init__(self, person=None, pet=None):
        self.person = person
        self.pet = pet
        
    def getPetperson2(self):
        for x in personAndPets:
            if x['name'] == self.person:
                for p in x['pets']:
                    print(p)

pp0 = personPets2(person='Padme Amidal')
PP0.getPetperson2()
"""
#menampilkan list data person dan pets
#menampilkan pets by person
#menampilkan person by pets
#menampilkan true or false jika di masukkan person & pets

