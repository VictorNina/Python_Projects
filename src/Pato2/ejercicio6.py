import math
n=int(input())
while n%3!=0:
    n=int(input())
li=[]
for i in range(1,n+1):
    x=int(input())
    li.append(x)
    if i%3==0 :
        if li[0]+li[1]>li[2] and li[0]+li[2]>li[1] and li[1]+li[2]>li[0]:
            s=(li[0]+li[1]+li[2])/2
            area = math.sqrt(s * (s - li[0]) * (s - li[1]) * (s - li[2]))
            print("Area: {:.6f}".format(area))
        else:
            print("No hay area")
        li.clear()
    
