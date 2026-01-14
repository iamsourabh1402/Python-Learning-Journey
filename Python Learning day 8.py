# lets learn while loops
food = input ("Enter your fav food (press q to quit)")
# while age <= 0:
 #    print ("Age cannot be negative")
 #   age = int(input ("Enter your correct age")) 

    
   # print(f"Your age is {age}")



while not food == "q":
    print(f"I like {food} too!")
    food = input("Enter your another fav food (press q to quit)")

print("Thank you for sharing your fav food!")
