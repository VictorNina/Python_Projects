def programa():
    a=list(map(int, input().split()))
    elementos=set(a)
    izq=0
    der=0
    for elemento in elementos:
        if a.count(elemento)==1:
            if izq <= der:
                izq += 1
            else:
                der += 1
    print(izq, der)
    
programa()
