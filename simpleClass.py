class Person:
    name = None
    family = None

    def __init__(self, name, family):
        self.name = name
        self.family = family

    def say_hello(self):
        print(f"Hello, my full name is {self.name} {self.family}.")

name = input("Enter name: ")
family = input("Enter family: ")

p1 = Person(name, family)
p1.say_hello()