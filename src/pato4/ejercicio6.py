N_O=49000
criba=[True]*(N_O+1)
primos=[]
def make_criba():
    criba[0]=criba[1]=False
    for i in range(2,N_O):
        if criba[i]==True:
            primos.append(i)
            for j in range(i+i,N_O,i):
                criba[j]=False
    

def mostrar(matriz,n,m):
    for i in range(n):
        for j in range(m):
            if j==m-1:
                print(matriz[i][j])
            else:
                print(matriz[i][j],end=" ")

def programa():
    make_criba()
    while True:
        n,m=map(int, input().split())
        if n%2==0 and m%2==0:
            break
    matriz = []
    for i in range(n):
        fila = [0] * m
        matriz.append(fila)

    i_primo=0
    i_impar=0
    for i in range(0,n,2):
        for j in range(m):
            print("entra")
            if j%2==0:
                matriz[i][j]=primos[i_primo]
                i_primo+=1
                matriz[i+1][j]=i_impar*2+1
                i_impar+=1
            else:
                matriz[i][j]=i_impar*2+1
                i_impar+=1
                matriz[i+1][j]=primos[i_primo]
                i_primo+=1
    mostrar(matriz,n,m)


programa()