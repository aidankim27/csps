n=input()
a=input()
n=int(n)
sump=0
suma=0
num = a.split()

def predsum(numint,sumholder):
    while numint>=1:
        sumholder+=numint
        numint-=1
    return sumholder
def checksum(numint,sumact):
    for i in numint:
        sumact+=int(i)
    return sumact


sump=predsum(n,sump)
suma=checksum(num,suma)
a=sump-suma

print(a)
