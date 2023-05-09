def suma(x,y=1):
    if(x==5):
        print(y)
        return
    else:
        print(y)
        y=y+1
        suma(x+1,y)


suma(1)