def numeros(x,y=0):
    if(y==x):
        print(x)
        return
    else:
        print(y)
        numeros(x,y+1)

n=int(input())
numeros(n)
