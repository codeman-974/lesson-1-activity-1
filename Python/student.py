class CSStudent:
    stream = 'cse'
    def __init__(self, roll):
        self.roll = roll

    def SetAdress(self, adress):
        self.adress = adress

    def getAdress(self):
        return self.adress

add = CSStudent(101)
add.SetAdress("Pune, Maharashtra")
print(add.getAdress())

a = CSStudent(101)
b = CSStudent(102)

print(a.stream)
print(b.stream)
print(a.roll)

print(CSStudent.stream)