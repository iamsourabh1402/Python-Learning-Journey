def create_words(letters, word=""):
    if len(word) == len(letters):
        print(word)
        return

    for ch in letters:
        if ch not in word:
            create_words(letters, word + ch)


create_words("abcde")
