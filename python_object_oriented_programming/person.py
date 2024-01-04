# class GFG:
#     def __init__(self, name, company):
#         self.name = name
#         self.company = company

#     def show(self):
#         print("Hello my name is " + self.name + " and I " + "work in "+ self.company+ ".")

# obj = GFG("Nitesh", "SpaceX")
# obj.show()



### simple class with inti method
# class Person:

#     #init method or constructor
#     def __init__(self, name):
#         self.name = name

#     # simple method
#     def say_hi(self):
#         print("Hello, my name is", self.name)
    

# person1 = Person("Nitesh")
# person1.say_hi()


################ __str__() method ##############


# class GFG:
#     def __init__(self, name, company):
#         self.name = name
#         self.company = company

#     def __str__(self):
#         return f"My name is {self.name} and I work in {self.company}."


# my_obj = GFG("Nitesh", "SpaceX")
# print(my_obj)


############## Defining instance variables using a constructor.  ################
# to show that the variables with a value
# assigned in the class decleration, are class variables 
# variables inside methods and constructor are instance variables

# class Dog:
    
#     # Class Variable
#     animal = "dog"

#     # The init method or constructor
#     def __init__(self, breed, color):

#         # Instance Variable
#         self.breed = breed
#         self.color = color


# # Object of Dog Class
# Rodger = Dog("Pug", "brown")
# Buzo = Dog("Bulldog", "black")

# print('Rodger details: ')
# print('Rodger is a ', Rodger.animal)
# print('Breed: ',Rodger.breed)
# print('Color: ', Rodger.color)

# print('\nBuzo details:')
# print('Buzo is a', Buzo.animal)
# print('Breed: ', Buzo.breed)
# print('Color: ', Buzo.color)


# # Class variables can be accessed using class
# # name also
# print("\n Accessing class variable using class name")
# print(Dog.animal)



######### Defining instance variables using the normal method ################

# program to show that we can create
# instance variables inside methods

class Dog:

    # Class Varible
    animal = 'Dog'

    # The init method or constructor
    def __init__(self, breed):

        # Instance Varibale
        self.breed = breed

    # Add an instance variables
    def setColor(self, color):
        self.color = color

    # Retrieves instance Variable
    def getColor(self):
        return self.color
    
# Driver code
Rodger = Dog("Pug")
Rodger.setColor("brown")
print(Rodger.getColor())