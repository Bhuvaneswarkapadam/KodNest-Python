c = 30
def add():
    global a
a = 10
b = 20
print(a + b)
print(c)
add()
print (c)
# print (f "the value of a is {a}")
#print ( a + b)
x = 100
def display():
    x = 50
    print("Local x :",x)
display()
print("Global x :",x)

x = 10
def display():
    print( x )
display()
x = 20
print(x)

