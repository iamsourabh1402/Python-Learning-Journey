# WAP to find factorial of a number


def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *=i
    return fact
    
num = int(input("Enter a number to find factorial: "))
print(cal_fact(num))