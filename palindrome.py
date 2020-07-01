palindromecheck = "taco cat"


def checkpalindrome(word):
    word = str(word)
    word = word.replace(" ", "")
    newstring = ""
    for i in word:
        newstring = i + newstring
    newstring = newstring.replace(" ", "")
    if newstring == word:
        print("This is a palindrome")
    else:
        print(palindromecheck, "is not a palindrome")


checkpalindrome(palindromecheck)
