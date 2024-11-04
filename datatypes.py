number = 25 #int
second = 56.78 #float
text = "Hello there" #String
isPythonInteresting = True #boolean

#DATA STRUCTURES. Multiple values stored in a single variable

cars = ["Toyota", "Nissan", "BMW"] #A list's elements are ordered and changeable
fruits = ("Banana","Orange", "Apple") # This is a tuple, it is always ordered but unchangeable
countries = {"Algeria", "Kenya", "Tunisia"} #Set, its elements are unordered and unchangeable
student = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "course" : "Python",
    "nationality": "Kenyan",
} #Dictionary - comes in form of a key and value pair

print(student["first_name"])
print(cars[0])
print(fruits)
print(countries)
print(student)
print(cars)
print(number)
print(second)
print(text)
print(isPythonInteresting)

#Determining a data type
print( type(countries))
print( type(fruits))
print( type(student))

#type casting - processing of converting from one data type to another

print(float(number))
print(int(second))
