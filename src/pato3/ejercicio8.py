def irregularidades(vector,n,cont1=0,sw=False,pos1=0,pos2=1):
    if(pos1==n-1):
        return cont1
    else:
        if(vector[pos2]>vector[pos1]):
            sw=True
        if sw:
            cont1=cont1+1
            sw=False
            pos1=pos1+1
            if(pos1==n-1):
                return cont1
            pos2=pos1+1
        else:
            if(pos2==n-1):
                pos1=pos1+1
                if(pos1==n-1):
                    return cont1
                pos2=pos1+1
            else:
                pos2=pos2+1
        return irregularidades(vector,n,cont1,sw,pos1,pos2)

t=int(input())
for _ in range(1,t+1):
    n=int(input())
    vector=list(map(int, input().split()))
    print(irregularidades(vector,n))