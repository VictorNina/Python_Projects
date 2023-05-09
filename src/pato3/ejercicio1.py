def recursividad(x,y):
    if(x==y):
        print(x)
        return
    else:
        print(y)
        recursividad(x,y-1)


a,b=map(int, input().split())
if a>b:
    may=a
    men=b
else:
    may=b
    men=a

recursividad(men,may)
 