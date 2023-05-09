def programa():
    caso_prueba=int(input())
    for _ in range(caso_prueba):
        n=int(input())
        vector=list(map(int, input().split()))
        vector_resultados=[]
        vector.sort()
        for i in range(n-1):
            vector_resultados.append(vector[i+1]-vector[i])
        print(min(vector_resultados))
            
programa()
                