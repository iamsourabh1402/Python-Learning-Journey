#convert USD to Inr

def convert_USD(USD):
    INR = USD * 82.74
    return INR


amount = float(input("Enter amount in USD: "))
print(f"Amount in INR is : {convert_USD(amount)}")
