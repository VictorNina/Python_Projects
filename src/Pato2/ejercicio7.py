while True:
    try:
        n, m = map(int, input().split())
        matriz = []
        for i in range(n):
            fila = list(map(int, input().split()))
            matriz.append(fila)
        max = -100*m*n
        suma = 0
        for j in range(m):
            for i in range(n):
                suma = suma+matriz[i][j]
                print(suma)
            if(suma>max):
                max=suma
        print(max)
    except:
        break 
