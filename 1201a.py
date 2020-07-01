n = input()
n=n.split( )
a=[]
#inting
for i in n:
    a.extend([int(i)])
ans=[]
listans=[]
ques=[]
#makinglistofit
for i in range(a[0]):
    sub=input()
    ans.extend([sub])

score = input()
score=score.split( )
scores=[]
for i in score:
    scores.extend([int(i)])


for j in range(a[0]):
    holder2=[]
    holder2.clear()
    for i in ans[j]:
        holder2.extend([i])

    listans.extend([holder2])



for c in range(a[1]):
    tracker=0
    holder={}
    letterlist=[]
    lib={"A":0,"B":0,"C":0,"D":0,"E":0}
    holder.clear()
    letterlist.clear()
    for i in range(a[0]):
        letter=ans[i][c]
        letterlist.extend([letter])
    for b in letterlist:
        lib[b]+=1
    max_key = max(lib, key=lib.get)        
    holder=lib[max_key]


    ques.extend([holder])

points=0
for i in range(a[1]):
    points+=ques[i]*scores[i]

print(points)