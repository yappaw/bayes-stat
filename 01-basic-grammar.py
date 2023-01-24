# 1. Variables

x = 5
y = 10
z = x + y
print(z)  # Output: 15

# 2. Data types

# Numbers (int, float)
a = 5
b = 10.5

# Strings
words = "Hello World"

# Lists
numbers = [1, 2, 3, 4, 5]
names = ["John", "Mike", "Emily"]

# Tuples
person = ("John", 30, "New York")

# 3. Conditional statements

x = 5
y = 10

if x < y:
    print("x is less than y")
else:
    print("x is greater than or equal to y")

# 4. Loops

# For loop
for i in range(5):
    print(i)

# While loop
i = 0
while i < 5:
    print(i)
    i += 1


# 5. Functions

def add(c, d):
    return c + d


result = add(5, 10)
print(result)  # Output: 15

# 6. Lists and for-loop

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# 7. Dictionaries

person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])  # Output: "John"

# 8. List comprehension

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# 9. Try-except

try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


# 10. Class

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog = Dog("Rex", "Golden Retriever")
print(dog.name)  # Output: "Rex"
