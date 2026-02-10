#Finding duplicates in a list

numbers = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 1]
duplicates = []
for i in numbers:
    if numbers.count(i)>1 and i not in duplicates:
     duplicates.append(i)



print(duplicates)

             