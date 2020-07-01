list1 = [10, 15, 3, 7]


def firstandlast(listname):
    print(listname[0])
    a = len(list1)
    b = a - 1
    print(listname[b])


firstandlast(list1)

list2 = [10, 15, 3, 7, 12, 33, 65, 45, 24, 9, 8]

for i in list2:
    print(i)
for i in list2:
    if i % 2 == 0:
        print("This number", i, " is  even")
    else:
        print("This number", i, " is odd")

list3 = ["ajifs", "gjaga", "igjaigraj"]
wordCheck = input()
for i in list3:
    if wordCheck == i:
        print("It is in the list")
