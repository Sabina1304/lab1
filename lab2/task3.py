
operators

# ex 1
print(10 * 5)

# ex 2
print(10 / 5)

# ex 3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

# ex 4
if 5 != 10:
  print("5 and 10 is not equal")

# ex 5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")


sets 

# ex 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

# ex 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

# ex 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

# ex 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

# ex 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

tuples

# ex 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

# ex 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# ex 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

# ex 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
