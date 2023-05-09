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
    colu=0
    fila=n-1
    while fila>0 :
        for i in range(colu,fila+1):
            matriz[colu][i]=cont
        for j in range(colu+1,fila+1):
            matriz[j][fila]=cont
        for k in range(fila,colu-1,-1):
            matriz[fila][k]=cont
        for l in range(fila,colu-1,-1):
            matriz[l][colu]=cont
        colu+=1
        fila-=1
        cont+=1
    mostrar(matriz,n)
programa()