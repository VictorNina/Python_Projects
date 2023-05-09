while True:
    try:
        n,m,k=map(int, input().split())
        matriz=[]
        for _ in range(n):
            fila=list(map(input().split("")))
            matriz.append(fila)
        print(matriz)
    except:
        break