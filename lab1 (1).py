print("Hello World!")




import sys


print(sys.version)








if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
         print("Five is greater than two!")







print("Hello, World!") #This is a comment example 1 

#print("Hello, World!") example 2
print("Cheers, Mate!")


"""
This is a comment
written in
more than just one line
"""
print("Hello, World!") #example 3









x = 5
y = "John"
print(x)
print(y) #example 1


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x) 
# example 2


#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


#Get the Type
#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))


#Single or Double Quotes?
#String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'



#Case-Sensitive
a = 4
A = "Sally"
#A will not overwrite a









#Variable Names
   

#Camel Case
myVariableName = "John"

#Pascal Cas

MyVariableName = "John"

# Snake Case

my_variable_name = "John"








#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)










x = "Python is awesome"
print(x) #The Python print() function is often used to output variables


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

## In the print() function, you output multiple variables, separated by a comma:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z) #You can also use the + operator to output multiple variables:









#global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

##2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

##3
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


##4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)









#Built-in Data Types
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
x = 5
print(type(x))











x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

#Complex:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))









"""
int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

"""
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3 #integers

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2 #floats

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
#strings



