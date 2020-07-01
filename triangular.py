import math 
nums=[1]
divisor=[]
def findTnums(listnum):
    for i in range(1,15000):
        holder=listnum[i-1]
        holder+=i+1
        listnum.extend([holder])

def finddivisors(listnums,divisorlist):
    divisors=0
    for i in listnums: 
        a=math.sqrt(i)
        a=int(a)+1
        for j in range(1,a):
            if i%j==0:
                divisors+=1
        divisors*=2
        divisorlist.extend([divisors])
        divisors=0

findTnums(nums)
finddivisors(nums,divisor)
print(nums)
print(divisor)
print(max(divisor))
position=divisor.index(576)
print(position)
divisor.sort(reverse=True)

print(divisor)
print(nums[12374])