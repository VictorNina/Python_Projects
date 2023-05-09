def mostrar(vector,n):
    for i in range(n):
        if(i==n-1):
            print(vector[i])
        else:
            print(vector[i],end=" ")

def rotar(segmento,i):

    first_number=segmento[0]
    for j in range(i-1):
        segmento[j]=segmento[j+1]
    segmento[i-1]=first_number

def programa():
    while True:
        n,k=map(int , input().split())
        if n%k==0:
            break
    vector=list(map(int, input().split()))
    segmento=[]
    vector_resultante=[]
    for i in range(n):
        if i%k==0 and i!=0:
            rotar(segmento,k)
            vector_resultante.extend(segmento)
            segmento.clear()
            segmento.append(vector[i])
        else:
            segmento.append(vector[i])
        if i==n-1:
            rotar(segmento,k)
            vector_resultante.extend(segmento)
    mostrar(vector_resultante,n)

programa()
      

