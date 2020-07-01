tracker = 0

fibonaccilist = [1, 2]


def evennum(tracker1, list1):
    while True:
        evenlist = []
        a = list1[tracker1]
        tracker1 = tracker1 + 1
        b = list1[tracker1]
        c = a + b
        if c > 4000000:
            for i in list1:
                if i % 2 == 0:
                    evenlist.extend(list([i]))
            break
        list1.extend(list([c]))
    print(sum(evenlist))


evennum(tracker, fibonaccilist)
