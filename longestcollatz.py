size=input()
n=input()

nums=[]
nums.extend([n])

def compute(nint,list1):
    nint=int(nint)
    while nint!=1:
        if nint%2==0:
            nint=nint/2
        else:
            nint*=3
            nint+=1
        nint=int(nint)
        list1.extend([nint])

compute(n,nums)
for i in nums:
    print(i, end=' ')
