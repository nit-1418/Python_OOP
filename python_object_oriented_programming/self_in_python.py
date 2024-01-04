# class mynumber:
#     def __init__(self, value):
#         self.value = value
    
#     def print_value(self):
#         print(self.value)


# obj1 = mynumber(17)
# obj1.print_value()

# class Subject:
#     def __init__(self, attr1, attr2):
#         self.attr1 = attr1
#         self.attr2 = attr2

# obj = Subject("Math", "Science")
# print(obj.attr1)
# print(obj.attr2)

# class check:
#     def __init__(self):
#         print("Address of self = ", id(self))

# obj = check()
# print("Address of class object = ",id(obj))


###################### car example #####################

# class car():

#     # init method or constructor
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color

#     def show(self):
#         print("Model is", self.model)
#         print("Color is", self.color)

# # both objects have different self which contain their attributes
# audi = car("audi a4", "blue")
# ferrari = car("ferrari 488", "green")

# audi.show()  # or can write car.show(audi)
# ferrari.show()  # or can write car.show(ferrari)

# print("Model for audi is", audi.model)
# print("Color for ferrari is", ferrari.color)


################# end #####################################

# class check:
#     def __init__(self):
#         print("This is Constructor")

# object = check()
# print("worked fine")


# class this_is_class:
#     def __init__(in_place_of_self):
#         print("we have used another"
#               "parameter name in place of self")
        
# object = this_is_class()