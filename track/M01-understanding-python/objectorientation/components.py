
# Component
class student:
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company

    def study(self):
        print(f"{self.name} is studying")

    def getDetails(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Company : {self.company}")

    def trip(self):
        print(f"{self.name} goes for a trip")

s1 = student("Bhuvaneswar", 21, "KodNest")
s1.study()
s1.getDetails()
s1.trip()

print("\n")

s2 = student("priya", 22, "amazon")
s2.study()
s2.getDetails()
s2.trip()


