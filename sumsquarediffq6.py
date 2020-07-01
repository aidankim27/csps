def square():
    a=0
    for i in range(1,101):
        b=i*i
        a=b  + a 
    return a 

def sumsquare():
    a=0
    for i in range(1,101):
        a = i+a
    b=a*a
    return b 

if __name__ == "__main__":
	print(sumsquare()-square()) 