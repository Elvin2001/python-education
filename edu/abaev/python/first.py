class Address:

    def __init__(self, country, city, hood, house):
        self.country = country
        self.city = city
        self.hood = hood
        self.house = house

    def getInfo(self):
        print(f"Address: {self.country}, {self.city}, {self.hood}, {self.house}")


class Person:

    def __init__(self, firstName, lastName, age, isMarried, address):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.isMarried = isMarried
        self.address = address

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getAge(self):
        return self.age

    def getMarriageInfo(self):
        return self.isMarried

    def getInfo(self):
        print(
            f"Person name: {self.firstName} {self.lastName}, age: {self.age}, address: {self.address.country}, {self.address.city}, {self.address.hood}, {self.address.house}")


firstAddress = Address("Russian Federation", "Budennovsk", "Severniy", 1)
secondAddress = Address("Russian Federation", "Shali", "Shaliyskiy", 5)
thirdAddress = Address("Russian Federation", "Budennovsk", "Severniy", 14)

firstPerson = Person("Elvin", "Abaev", 23, False, firstAddress)
secondPerson = Person("Vladimir", "Kuzmenko", 22, False, secondAddress)
thirdPerson = Person("Polina", "Belousova", 18, True, thirdAddress)

persons = [firstPerson, secondPerson, thirdPerson]

for p in persons:
    p.getInfo()
