
def mostrar(matriz,n):
    for i in range(n):
        for j in range(n):
            if j==n-1:
                print(int(matriz[i][j]))
            else:
                print(int(matriz[i][j]),end=" ")


def programa():
    n=int(input())
    matriz = [[0] * n for i in range(n)]
    cont=1
    sw=False
    sw2=True
    ini=0
    lim=n-1
    for i in range(n):
        for j in range(n):
            if sw2:
                if i==j and ini!=lim:
                    sw=True
                    ini +=1
                if sw and i!=j and i+j!=n-1 and ini!=lim:
                    matriz[i][j]=cont
                    cont +=1
                if j+i==n-1 and ini!=lim:
                    sw=False
                    lim-=1
            else:
                if j+i==n-1 :
                    sw=True
                if sw and i!=j and i+j!=n-1 :
                    matriz[i][j]=cont
                    cont +=1
                if i==j :
                    sw=False  
            if ini==lim:
                sw=False
                sw2=False
                i+=1
                ini=0
                lim=n-1
    mostrar(matriz,n)
    
programa()