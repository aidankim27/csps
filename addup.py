list1 = [4, 125, 51, 43, 4, 51, 6, 61, 5]

number = 9


def doeslistequal(listname, numbername):
    holder = False
    for i in listname:
        for x in listname:
            if i + x == numbername:
                holder = True
    if holder == True:
        print("It adds up")
    else:
        print("It does not add up")


doeslistequal(list1, number)
