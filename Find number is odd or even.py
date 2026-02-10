#find number is odd or even

def even_odd(num):
    if  num%2== 0:
      print("Number is EVEN")
    else:
       print("Number is ODD")


number = int(input("Enter the number: "))
even_odd(number)