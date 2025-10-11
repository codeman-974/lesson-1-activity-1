class Circle():
    def __init__(self, r):
        self.radius = r
        

    def circle_area(self):
      return 3.14*self.radius*self.radius


newCircle = Circle (10)
print ("Dimension of the circle - Radius: %d" % 
       (newCircle.radius ))

print("Area of the circle :", newCircle.circle_area())