size=input()
n=input()
n=n.strip()
n=n.split(" ")
nums=[]
maxnum=[]
for i in n:
    nums.extend([int(i)])

def createnewlist(list1,orig):
    holder=0
    for i in range(len(orig)):
        if orig[i]>holder:
            holder=orig[i]
        list1.extend([holder])
def compute(list1,orig):
    holder=0
    for i in range(len(orig)):
        holder+=list1[i]-orig[i]
    print(holder)

createnewlist(maxnum,nums)
compute(maxnum,nums)
