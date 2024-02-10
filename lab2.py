# Booleans

# 1 exercise
print(10 > 9)

True

# 2 exercise
print(10 == 9)

False

# 3 exercise
print(10 < 9)

False

# 4 exercise
print(bool("abc"))

True

# 5 exercise
print(bool(0))

False

# Operators

# 1 exercise
print(10 * 5)

# 2 exercise
print(10 / 2)

# 3 exercise
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

# 4 exercise
if 5 != 10:
  print("5 and 10 is not equal")

# 5 exercise
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

# Lists

# 1 exercise
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# 2 exercise
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# 3 exercise
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# 4 exercise
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

# 5 exercise
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

# 6 exercise
fruits = ["apple", "banana", "cherry"]
print(fruits[-1:])

# 7 exercise
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

# 8 exercise
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

# tuples

# 1 exercise
fruits = ("apple", "banana", "cherry")
print(fruits[0])

# 2 exercise
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# 3 exercise
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

# 4 exercise
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

# Sets

# 1 exercise
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

# 2 exercise
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

# 3 exercise
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

# 4 exercise
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

# 5 exercise
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

# Dictionaries

# 1 exercise
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

# 2 exercise
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

# 3 exercise
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

# 4 exercise
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

# 5 exercise
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
# If...else

# 1 exercise
a = 50
b = 10
if a > b:
  print("Hello World")

# 2 exercise
a = 50
b = 10
if a != b:
  print("Hello World")

# 3 exercise
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

# 4 exercise
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

# 5 exercise
if a == b and c == d:
  print("Hello")

# 6 exercise
if a == b or c == d:
  print("Hello")

# 7 exercise
if 5 > 2:
    print("YES")

# 8 exercise
a = 2
b = 5
print("YES") if a == b else print("NO")

# 9 exercise
a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")

# While Loops

# 1 exercise
i = 1
while i < 6:
    print(i)
    i += 1

# 2 exercise
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# 3 exercise
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# 4 exercise
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# For Loops

# 1 exercise
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# 2 exercise
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# 3 exercise
for x in range(6):
    print(x)

# 4 exercise
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
