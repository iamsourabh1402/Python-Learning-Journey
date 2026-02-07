#def birthday(name, age):
 #   print("Happy Birthday to you!")
  #  print("Happy Birthday to you!")
   # print(f"Happy Birthday dear {name}")
    #print(f"You are now {age}")

#birthday("Alice", 25)

"""
def invoice():
    name= input("Input name:")
    amount= input("Input amount:")
    duedate= input("Input due date:")
    print(f"name is {name}")
    print(f"Amount is {amount}")
    print(f"Due date is {duedate}")

invoice()"""

"""def add(a, b):
    c = a + b
    return c

def sub(a, b):
    c = a - b
    return c

def mul(a, b):
    c = a * b
    return c

def div(a, b):
    c = a / b
    return c


print(add(10,5))
print(sub(10,5))
print(mul(10,5))
print(div(10,5))"""

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return  first + " " + last

full_name = create_name("sourabh", "kumar")
print(full_name)