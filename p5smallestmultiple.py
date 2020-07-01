import math

a=1
for i in range(1,21):
    a*=i//math.gcd(a,i)

print(a)