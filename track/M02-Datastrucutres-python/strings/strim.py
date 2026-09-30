'''s1 = "hello"
print(id(s1),s1)'''

'''s1 = "hello"
print(id(s1))
print(s1)
s1=(s1 +" world")
print(id(s1))
print(s1)'''


'''s1 = "hello"
s2 = s1 + "world"
print(id(s1),s1)
print(id(s2),s2)'''

s1 = "bunny"
s2 = "bunny"
print(id(s1),s1)
print(id(s2),s2)
print(s1 == s2)
print(s1 is s2)


s1 = "bunny"
s2 = "Bunny"
print(id(s1),s1)
print(id(s2),s2)
print(s1 == s2)
print(s1 is s2)
