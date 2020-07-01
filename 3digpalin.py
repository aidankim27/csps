def checkpalindrome(word):
    word = str(word)
    word = word.replace(" ", "")
    newstring = ""
    for i in word:
        newstring = i + newstring
    newstring = newstring.replace(" ", "")
    if newstring == word:
        return True


listp = []

for i in range(95000, 100000):
    for j in range(95000, 100000):
        placeholder = i * j
        a = checkpalindrome(placeholder)
        if a == True:
            listp.extend([placeholder])
print(listp)
