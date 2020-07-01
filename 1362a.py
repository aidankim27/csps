import math
n=int(input())
ans=[]
b=[]



for i in range(n):
    a=input()
    a=a.split()
    ans.extend([a])

answers=[]
def makedivisor(a,divisor):
    divisor.clear()
    for i in range(1,math.floor(math.sqrt(a))+2):
        check=a/i
        if i==8:
            divisor.extend([i])
        if i==4:
            divisor.extend([i])
        if i==2:
            divisor.extend([i])
        if check==8:
            divisor.extend([check])
        if check==4:
            divisor.extend([check])
        if check==2:
            divisor.extend([check])
        divisor.sort(reverse=True)
def check(ans,answers,n):
    tracker=[]
    divisors=[]
    check=0
    trackers=0
    for i in ans:
        tracker.clear()
        divisors.clear()
        trackers=0
        check=0
        for j in i: 
            tracker.extend([int(j)])
        tracker.sort()
        a=tracker[1]/tracker[0]
        if tracker[1]==tracker[0]: 
            answers.extend([0])
        elif a%2!=0:
            answers.extend([-1])
        elif a%8!=0:
            answers.append(-1)
        else:
            makedivisor(a,divisors)
            divisors.sort(reverse=True)
            print(divisors)
            print(a)
            while a>1:
                a/=divisors[0]
                trackers+=1
                makedivisor(a,divisors)
                print("current:",a)
                print("divisors",divisors)
            answers.append(trackers)
    print(answers)





check(ans,answers,n)
import math
n=int(input())
ans=[]
b=[]



for i in range(n):
    a=input()
    a=a.split()
    ans.extend([a])

answers=[]
def makedivisor(a,divisor):
    divisor.clear()
    for i in range(1,math.floor(math.sqrt(a))+2):
        check=a/i
        if i==8:
            divisor.extend([i])
        if i==4:
            divisor.extend([i])
        if i==2:
            divisor.extend([i])
        if check==8:
            divisor.extend([check])
        if check==4:
            divisor.extend([check])
        if check==2:
            divisor.extend([check])
        divisor.sort(reverse=True)
def check(ans,answers,n):
    tracker=[]
    divisors=[]
    check=0
    trackers=0
    for i in ans:
        tracker.clear()
        divisors.clear()
        trackers=0
        check=0
        for j in i: 
            tracker.extend([int(j)])
        tracker.sort()
        a=tracker[1]/tracker[0]
        if tracker[1]==tracker[0]: 
            answers.extend([0])
        elif a%2!=0:
            answers.extend([-1])
        elif a%8!=0:
            answers.append(-1)
        else:
            makedivisor(a,divisors)
            divisors.sort(reverse=True)
            print(divisors)
            print(a)
            while a>1:
                a/=divisors[0]
                trackers+=1
                makedivisor(a,divisors)
                print("current:",a)
                print("divisors",divisors)
            answers.append(trackers)
    print(answers)





check(ans,answers,n)
