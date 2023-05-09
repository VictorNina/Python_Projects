def programa():
    casos_prueba=int(input())
    for _ in range(casos_prueba):
        n,m=map(int, input().split())
        matriz=[]
        for i in range(n):
            fila=list(map(int, input().split()))
            matriz.append(fila)
        print(matriz)


programa()