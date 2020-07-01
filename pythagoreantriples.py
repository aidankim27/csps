#find triple where a +b+c=1000

#find perfect sqaures list 
import math 
listofsqaures=[]
def sqaures(list1):
    for i in range(2,1000000):
        sqrt = math.sqrt(i)
        lenofsqrt=str(sqrt).replace(".","")
        if len(lenofsqrt)<5:
            list1.extend([i])
listofps=[]
def findPerfectSqs(list1,list2):
    for a in list1:
        for b in list1:
            for c in list1:
                if a+b==c:
                    d =math.sqrt(a)
                    e =math.sqrt(b)
                    f=math.sqrt(c)
                    if d+e+f==1000:
                        y=d*e*f
                        list2.extend([y])
sqaures(listofsqaures)

findPerfectSqs(listofsqaures,listofps)
print(listofps )
