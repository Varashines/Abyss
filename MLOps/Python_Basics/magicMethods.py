class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"Person(name = {self.name}, age = {self.age})"

person = Person("Vara",25)
print(person)
print(repr(person))
