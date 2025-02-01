class Animal:
    def speak(self):
        print("Animals")
class Dog(Animal):
    def speak(self):
        print("Dogs bark!!")
class Cat(Animal):
    def speak(self):
        print("Cats meow!!")
o1=Dog()
o1.speak()
o2=Cat()
o2.speak()
