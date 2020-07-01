n=input()
n=int(n)
liststr=[]

for i in range(n):
    s=input()
    liststr.append(s)
def solve(list1):
    lis2=[]
    for j in list1:
        if len(j)>10:
            for a in j:
                lis2.append(a)
            print(lis2[0],len(lis2)-2,lis2[len(lis2)-1],sep="")
            lis2.clear()
        else:
            print(j)


solve(liststr)
