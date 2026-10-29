class student:
    company = "KodNest"

    def __init__(self, name, age, company=None):
        self.name = name
        self.age = age
        if company is not None:
            self.company = company

    def study(self):
        a = 10
        print(a)
        print(f"{self.name} is studying")

    def getDetails(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Company : {self.company}")

    @staticmethod
    def trip(name):
        print(f"{name} goes for a trip")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


student.change_company("KodNest Technologies Pvt Ltd")

s1 = student("Bhuvaneswar", 21)
print(student.company)
print(s1.company)
print(s1.name)
s1.study()
s1.getDetails()

print("\n")

s2 = student("Priya", 22)
student.trip(s2.name)
print(s2.name)
s2.study()
s2.getDetails()
s2.trip(s2.name)