n=input()
dnalist=[]
tracker=1
anslist=[1]
for i in n:
    dnalist.extend([i])
dnalist.extend([""])
for i in range(len(dnalist)-1):
    if dnalist[i]==dnalist[i+1]:
        tracker+=1
    else:
        anslist.extend([tracker])
        tracker=0
largest=max(anslist)
print(largest)
print(anslist)