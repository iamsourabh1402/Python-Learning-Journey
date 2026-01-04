# lets make an age calculator
from datetime import date
today = date.today()


year= int(input("Enter your birth year:"))
month = int(input("Enter your birth month:"))
day = int(input("Enter your birth day: "))
dob= date(year,month,day)

age = today.year - dob.year 

if (today.month, today.day) < (dob.month, dob.day):
    age-=1
print(f"Your age is {age} years")
