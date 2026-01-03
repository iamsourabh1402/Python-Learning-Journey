

#lets build a simple calculator using If else
num1 = int(input("Enter your first number "))
num2 = int(input("Enter your second number ")) 
operator = input("Enter operator (+, -, *, /): ")


if operator == '+':
    print (f"The sum of {num1} and {num2} is {num1 + num2}")
elif operator == '-':
    print (f"The difference of {num1} and {num2} is {num1-num2}")
elif operator == '*':
    print (f"The product of {num1} and {num2} is {num1 * num2}")
elif operator == '/':
    print (f"The division of {num1} and {num2} is {num1/num2}")
elif operator == '%':
    print (f"The modulous of {num1} and {num2} is {num1%num2}")
else:
    print ("invalid operator")