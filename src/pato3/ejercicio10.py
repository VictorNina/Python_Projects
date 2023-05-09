def capicua(m,n,y=""):
    if n==0:
        return int(y)==m
    y=y+str(n%10)

    return capicua(m,n//10,y)






n=int(input())
m=n
if capicua(m,n):
    print("S")
else:
    print("N")