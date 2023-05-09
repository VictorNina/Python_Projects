def mostrar(vector,n):
    for i in range(n):
        if i==n-1:
            print(vector[i])
        else:
            print(vector[i],end=" ")


def programa():
    casos_prueba=int(input())
    for _ in range(casos_prueba):
        n=int(input())
        vector=list(map(int, input().split()))
        vector_resultante=vector.copy()
        cont=n-1
        cont2=0
        for i in range(n):
            if i%2==0:
                vector_resultante[i]=vector[cont2]
                cont2+=1
            else:
                vector_resultante[i]=vector[cont]
                cont-=1
        mostrar(vector_resultante,n)

programa()