from functools import reduce
"""#Functions, arguments and default arguments
def hello(age, name = "my friend"):
    print(f"Hello {name}! Welcome to Amazing world graphics")
    print(f"Your are {age} years old!")


def tokenize(phrase):
    return phrase.split(" ")


words = tokenize("Python is very simple")

for word, index in enumerate(words):
    print(word, index)"""

#Lambda functions (like Macros in C)
pow = lambda a, b : a ** b
print(pow(3, 3))

#To run a function through each item in a list use map()
list1 = [1, 3, 4, 5, 8, 9, 5,]

list2 = list(map(lambda a : a ** 2, list1))
print(list2)

#To filter a list through a condition use filter()
def isEven(n):
    return n % 2 == 0
list3 = list(filter(lambda a : a % 2 == 0, list1))
print(list3)

#list of tupples, calculating sum using iteration and reduce()
expenses = [('Breakfast', 150), ('Dinner', 500)]
sum = 0
for meal in expenses:
    sum += meal[1]
print(sum)

sum = reduce(lambda a, b : a[1] + b[1], expenses)
print(sum)

#list compresions
numbers = [2, 4, 6, 2, 7, 1, 2]
numbers_pow3 = [n**3 for n in numbers]
print(numbers_pow3)
