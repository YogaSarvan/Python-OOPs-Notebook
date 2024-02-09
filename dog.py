
## A simple Script for creating a Class "Dog" and Making an Instance from a Classs

class Dog:

    def __init__(self, name, age):
        """ we are initialized name and age attribute"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate a dog roll_over in response to a command"""
        print(f"{self.name} rolled over")


#Here we are calling instance of Dog class to sit
my_dog = Dog('Shiny', 10)
my_dog.sit()
print(f"\n My dog {my_dog.name} age is {my_dog.age}")

#Here we are calling other instance of Dog Class to Roll Over

your_dog = Dog('Atram', 13)
print(f"\nYour dog {your_dog.name} age is {your_dog.age}")
your_dog.sit()
your_dog.roll_over()


        