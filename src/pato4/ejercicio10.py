
def mostrar(tablero,fila,colu):
    for i in range(fila):
        for j in range(colu):
            print(tablero[i][j],end="")
        print()
    print("----------")


while True:
    filas,colu=map(int, input().split())
    if not filas and not colu:
        break
    tablero=[]
    par_impar=0
    if (filas+colu-2)%2!=0:
        par_impar=1
    for i in range(filas):
        fila=[]
        for j in range(colu):
            if (i+j)%2==par_impar:
                fila.append(".")
            else:
                fila.append("X")
        tablero.append(fila)

    mostrar(tablero,filas,colu)

