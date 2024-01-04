class person:

    # default constructor
    def __init__(self):
        self.man = "Nitesh Rajbanshi"

    # a method for printing data members
    def print_man(self):
        print(self.man)

# creating object of the class
obj = person()

# calling the instance method using the object obj
obj.print_man()