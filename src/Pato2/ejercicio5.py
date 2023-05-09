t=int(input())
for _ in range(1,t+1):
    n=int(input())
    alturas = list(map(int, input().split()))
    edif_mas_alto = alturas.index(max(alturas))
    edif_mas_bajo = alturas.index(min(alturas))
    fealdad=max(alturas)-min(alturas)
    iteraciones=0
    while(fealdad>1):
        iteraciones +=1
        alturas[edif_mas_alto] -= 1
        alturas[edif_mas_bajo] += 1
        edif_mas_alto = alturas.index(max(alturas))
        edif_mas_bajo = alturas.index(min(alturas))
        fealdad=max(alturas)-min(alturas)
        if(iteraciones==n):
            break
    
    print(fealdad)
