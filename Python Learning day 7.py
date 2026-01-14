#lets make an email slicer 

email = input("Enter your email address: ")
index = email.index("@")

username = email [:index]
domain = email [index +1:]

print (f"Your username is {username} and Domain is {domain}")
