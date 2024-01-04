class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000,2000)

#  creating second object of same class
obj2 = Addition(20,30)

# perform Addition on obj1
obj1.calculate()
obj1.display()

# perform Addition on obj2
obj2.calculate()
obj2.display()

