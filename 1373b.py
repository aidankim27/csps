n=int(input())
ans=[]
for i in range(n):
    b=[]
    a=input()
    a=a.replace(" ","")
    for j in a:
        b.append(int(j))
    ans.extend([b])

for b in range(n):
    tracker=0
    if max(ans[b])==min(ans[b]):
        print("NET")
    else:
        i=0
        while len(ans[b])>i+1:
            if ans[b][i]!=ans[b][i+1]:
                zed=ans[b].pop(i)
                zed1=ans[b].pop(i)
                print(zed1,zed)
                tracker+=1
                i-=1
            else:
                i+=1
        if tracker%2==0:
            print(tracker)
            print("NET")
        else:
            print("DA")
            print(tracker)