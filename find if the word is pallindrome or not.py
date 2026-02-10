#find if the word is pallindrome or not
def is_pallindrome(word):
    return word == word[::-1]

word = input("Enter the word to check pallindrome: " )
if is_pallindrome(word):
    print(f"{word} is a pallindrome")
else:
    print(f"{word} is not a pallindrome")