def rm_mtpls(base, nums):
    for m in range(base*2, len(num), base):
        nums[m] = False

num=[True]*2000000
#remove 0 and 1 
num[0]=False
num[1]=False

listofprimes=[]

for i in  range(len(num)):
    if num[i]==True:
        rm_mtpls(i,num)
        listofprimes.extend([i])

ans=0
for i in listofprimes:
    ans+=i
print(ans)