#reverse each word of a string
"""def reverse_word(string):
    word = string.split()
    reverse = [i[::-1] for i in word]
    return " ".join(reverse)
string = input("Input string to reverse: ")
print(f"The Reversed string is: {reverse_word(string)}")"""

def average(num1, num2, num3):
    avg = (num1 + num2 + num3) /3
    return avg
num1= input("Enter number 1 for average: ")
num2= input("Enter number 2 for average: ")
num3= input("Enter number 3 for average: ")

print(average(int(num1), int(num2), int(num3)))
