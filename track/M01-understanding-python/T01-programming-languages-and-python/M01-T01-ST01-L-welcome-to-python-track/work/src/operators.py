# Arithmetic Operators

x = 15
y = 4

print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y) # Exponentiation
print(x // y) # Floor Division


# Assignment Operators

print("---------------- Assignment Operators ----------------")

x = 10
print("Starting value: x =", x)

x = 10
print("\nAfter = :", x)

x += 5
print("After += 5:", x)

x -= 3
print("After -= 3:", x)

x *= 2
print("After *= 2:", x)

x /= 4
print("After /= 4:", x)

x //= 2
print("After //= 2:", x)
x %= 3
print("After %= 3:", x)  # 0

x = 6
print("\nReset x =", x)  # 6

x **= 2
print("After **= 2:", x)  # 36


# Logical Bitwise Operators

x = 6
print("\nReset x =", x)  # 6

x &= 3
print("After &= 3:", x)

x |= 2
print("After |= 2:", x)

x ^= 5
print("After ^= 5:", x)
x = 4
print("\nReset x =", x)  # 4

x <<= 2
print("After <<= 2:", x)  # 16

x = 4
x >>= 1
print("After >>= 1:", x)  # 2


print("---------------- Bitwise Operators ----------------")

a = 5
b = 3

print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)
