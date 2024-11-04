class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def movement(self):
        print("person is walking")

a = person ("John", "24", "Male")
print("Name:", a.name, "Age:", a.age,"Gender:",  a.gender)

b = person ("Mary", "21", "Female")
print(b.name)

c = person ("Victor", 25, "Male")
print(c.name)
