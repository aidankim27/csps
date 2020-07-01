capnumber = 999

multiplecheck = [3, 5]


def findmultiples(numbers, capping):
    multiples = []
    for i in numbers:
        for j in range(capping + 1):
            a = i * j
            if a > capping:
                break
            multiples.extend(list([a]))
            multiples = list(dict.fromkeys(multiples))
    print(sum(multiples))


findmultiples(multiplecheck, capnumber)
