class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(data):

    Person.people = {}

    persons = []

    for item in data:
        persons.append(Person(item["name"], item["age"]))

    for item in data:
        person = Person.people[item["name"]]
        if item.get("wife") is not None:
            person.wife = Person.people[item["wife"]]
        if item.get("husband") is not None:
            person.husband = Person.people[item["husband"]]

    return persons
