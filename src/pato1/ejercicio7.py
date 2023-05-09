def suma3(n):
    if(n%9==4  or n%9==5):
        return False
    return True


t=int(input())
for _ in range(1,t+1):
    n=int(input())
    if(suma3(n)):
        print(str(n)+" se puede expresar como la suma de 3 cubos")
    else:
        print(str(n)+" no se puede expresar como la suma de 3 cubos")



