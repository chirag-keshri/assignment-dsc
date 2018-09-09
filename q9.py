class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius*self.radius*3.14

NewCircle = Circle(2)
print(NewCircle.area())
