def split(word):
    return [char for char in word]


word = input("What word would you like us to find?")

lengthOfWord = len(word)


charList = split(word)


middle = lengthOfWord // 2


middleLetter = charList[middle]
print("Middle is", middleLetter)
