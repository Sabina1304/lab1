booleans

# ex 1
print(10 > 9)
True
# ex 2
print(10 == 9)
False
# ex 3
print(10 < 9)
False
# ex 4
print(bool("abc"))
True
# ex 5
print(bool(0))
False

dictionaries

# ex 1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
# ex 2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
# ex 3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
# ex 4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
# ex 5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

forloops

# ex 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# ex 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":    
        continue
    print(x)

# ex 3
for x in range(6):
    print(x)

# ex 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

 ifelse

 # ex 1
a = 50
b = 10
if a > b:
    print("Hello World")
# ex 2
a = 50
b = 10
if a != b:
    print("Hello World")
# ex 3
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")
# ex 4
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")
# ex 5
c = 30
d = 20
if a == b and c == d:
    print("Hello")
# ex 6
if a == b or c == d:
    print("Hello")
# ex 7
if 5 > 2:
    print("YES")
# ex 8
a = 2
b = 5
print("YES") if a == b else print("NO")
# ex 9
a = 2
b = 50
c = 2
if a == c or b == c:
   print("YES")