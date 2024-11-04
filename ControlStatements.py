temp = 34
if (
        temp > 22):
    print("It's too hot")
else:
    print("It's too cold")

# Python program to check three numbers and returns the smallest number
num1 = 75
num2 = 25
num3 = 85
if (
    num1 < num2 and num1 < num3):
    print(num1, "is the smallest number")
elif (
    num2 < num1 and num2 < num3):
    print(num2, "is the smallest number")
else:
    print(num3, "is the smallest number")

# Python program to check three numbers and returns the largest number
x = 10
y = 5
z = 20
if (
    x > y and x > z):
    print(x, "is the largest number")
elif (
        y > x and y > z):
        print( y, "is the smallest number")
else:
    print( z, "is the largest number")

# A program to check whether a number is even or odd
number = 45
if (
    number % 2 == 0):
    print(number, "is a even number")
else:
    print(number, "is an odd number")