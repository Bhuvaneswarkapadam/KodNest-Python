# Inbulit string Method -single perpose methods - single program

s = "kodNest Technologies 123"

# Original string
print("Original String:", s)

# Case Conversion Methods
print("upper():", s.upper())
print("lower():", s.lower())
print("capitalize():", s.capitalize())
print("title():", s.title())
print("swapcase():", s.swapcase())

# Searching and Counting
print("find('Tech'):", s.find("Tech"))
print("count('o'):", s.count("o"))

# Replace
print("replace():", s.replace("123", "2025"))

# Start and End Check
print("startswith('kod'):", s.startswith("kod"))
print("endswith('123'):", s.endswith("123"))

# Split and Join
words = s.split()
print("split():", words)
print("join():", "-".join(words))
# Strip spaces
print("strip():", s.strip())  # kodNest Technologies 123
print("lstrip():", s.lstrip())  # kodNest Technologies 123
print("rstrip():", s.rstrip())  # kodNest Technologies 123

s = "      "

# Checking methods
print("isalpha():", s.isalpha())  # False
print("isdigit():", s.isdigit())  # False
print("isspace():", s.isspace())  # False
print("isalnum():", s.isalnum())  # False
print("Hello".isalnum())  # True

#length
print("Length of string: ",len(s))