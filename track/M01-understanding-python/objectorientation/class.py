
'''class student:
    name = "bunny"
    age = 21
    gender = "male"

    def study(self):
        print(f"{self.name} is studying,  {self.age} years")

    def play(self):
        print(f"{self.name} is playing,  {self.age} years")


s1 = student()

print(s1.name)
print(s1.age)
print(s1.gender)

s1.study()
s1.play()'''

# constructor

class student:
    def __init__(self,name,age,gender,profession):
        self.name = name
        self.age = age
        self.gender = gender
        self.profession = profession
    

    def study(self):
        print(f"{self.name} is studying,  {self.age} years {self.profession}")

    def play(self):
        print(f"{self.name} is playing,  {self.age} years as a {self.profession}") 
s1 = student("bunny",21,"male","student")
print(f"Name : {s1.name}\nAge : {s1.age}\nGender : {s1.gender}\nProfession : {s1.profession}")
s2 = student("bhuvan",20,"male","student")
print(f"Name : {s2.name}\nAge : {s2.age}\nGender : {s2.gender}\nProfession : {s2.profession}")
s3 = student("balayya",50,"male","actor")
print(f"Name : {s3.name}\nAge : {s3.age}\nGender : {s3.gender}\nProfession : {s3.profession}")
s1.study()
s1.play()
s2.study()
s2.play()
s3.study()
s3.play()

