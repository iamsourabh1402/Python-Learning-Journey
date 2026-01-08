#lets learn string methoda in python

name = input ("enter your full name: ")

if len(name) > 12:
    print("Your name is long thus will not be printed fully.")
elif not name.find(" ") == -1:
    print(f"Name cannot contain spaces")
elif not name.isalpha()== True:
    print("Name cannot contain numbers or special characters")

else:
    print(f"Name is {name}")

