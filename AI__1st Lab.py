print("Hello, World!")
#This is a comment
"""
This is a comment
written in
more than just one line
"""
x = 5
y = "John"
print(x)
print(y)
print(type(x))
print(type(y))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is "
y = "awesome"
z = x + y
print(z)

a = "awesome"
def my_func():
 print("Python is " + a)
my_func()

b = "awesome"
def myfunc():
 b = "fantastic"
 print("Python is " + b)
 myfunc()
print("Python is " + b)


if 5 > 2:
 print("Five is greater than two!")