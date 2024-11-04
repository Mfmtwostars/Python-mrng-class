#buil-in library functions
y = max(56,78,90,23,12)
print("The maximum value is", y)

x = min(67, 10,45,32,67)
print("The minimum value is", x)

z = pow(2,3)
print(z)

#User defined functions
def greeting():
    print("Hello there!")
greeting() # function calling

def multiply():
    num1 = 23
    num2 = 45
    print(num1*num2)
multiply()

#parameters/Variable and arguments/values
def add(a,b):
    print(a+b)
add(4,5)
add(76, 24)

def employee( fullname, age, position, status):
    print(fullname, age, position, status)
employee("John Smith", "32", "Manager", "Married")
employee("Victor Wepukuru", "43", "C.E.O", "Single")
employee("Mary Wangechi", "46", "Assistant Manager", "Married")
employee("Turuphosa waya", "29", "Clerk", "Married")
