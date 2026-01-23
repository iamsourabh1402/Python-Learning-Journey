rows = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
symbol = input("Enter symbol to use: ")

for x in range(rows):
    for y in range (col):
        print(symbol, end=" ")
    print()