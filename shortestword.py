string1 = "The quick brwn fox jumps over the lazy dog"


def findShortest(stringtaken):
    x = 0
    stringList = stringtaken.split()
    lengthlist = []
    for i in stringList:
        lengthlist.extend([len(stringList[x])])
        x += 1
    print("The shortest word is", len(min(stringList)), "letters long")


findShortest(string1)
