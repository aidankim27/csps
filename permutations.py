n=int(input())
nums=[]
numdict={}
f=[]
b=[]
#makignlist
for i in range(1,n):
    nums.extend([int(i)])

#making dict
def makedict(n,nums,numdict):
    trackfar=len(nums)
    if n%2!=0:
        for i in range(len(nums)//2):
            trackclose=nums[i]
            a={trackclose:trackfar}
            numdict.update(a)
            trackfar-=1
    else:
        for i in range(len(nums)//2+1):
            trackclose=nums[i]
            a={trackclose:trackfar}
            numdict.update(a)
            trackfar-=1
makedict(n,nums,numdict)
print(numdict)

track=2
while track<=n//2:
    f.extend([track])
    track+=2
track=1
while track<=n//2:
    f.extend([track])
    track+=2
for i in f:
    hold=numdict[i]
    b.extend([hold])
f.extend([n])
f+=b
def check(f):
    boolh=False
    for i in range(len(f)-1):
        if f[i]+1!=f[i+1]:
            pass
        else:
            boolh=True
    return boolh

boolh=check(f)

if boolh == True:
    track=2
    del f[:]
    del b[:]
    while track<=n//2:
        f.extend([numdict[track]])
        track+=2
    track=1
    while track<=n//2:
        f.extend([track])
        track+=2
    track=2
    for i in f:
        if i%2!=0:
            b.extend([track])  
            track+=2
        else:
            hold=numdict[i]
            b.extend([hold])
    f.extend([n])
    f+=b
ans=''
a=''
b=" "
if 1<n<=3:
    print("NO SOLUTION")
else:
    for i in f:
        a=str(i)
        ans+=a
        ans+=b
    print(ans)


ans=[]
n = int(input())
if 1<n<=3:
    print("NO SOLUTION")
else:
    for i in range(2,n+1,2):
        ans.extend([i])
    for i in range(1,n+1,2):
        ans.extend([i])
    answer=''
    a=''
    b=' '
    for i in ans:
        a=str(i)
        answer+=a
        answer+=b
    print(answer)
