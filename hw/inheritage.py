
class Animal:
    pass
    def eat(self):
        print("This animal is eating")

class Cat(Animal):
    def meau(self):
        print("Meau Meau")

class Dog(Animal):
    def bark(self):
        print("Ham Ham")


# some_animal = Animal()
some_cat = Cat()
some_dog = Dog()

# some_animal.eat()
some_cat.eat()
some_cat.meau()

some_dog.eat()
some_dog.bark()

# Animal().eat()

# Cat().eat()
