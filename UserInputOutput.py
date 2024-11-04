firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
Age = int(input("Enter your age: "))
print( "Your full name is" , firstname + " " + lastname," ,You are", Age , "years old" )

weight = float(input("Enter your weight: "))
if weight >= 80.0:
    print("You are endangering your health, you need to lose some weight.")
elif 45.0 <= weight < 80.0:
    print("You are not endangering your health, you are fit.")
else:
    print("You need to add some weight, you are underweight.")
