def busca(vector,n):
    referencia = vector[n-1]
    if(vector[0] == vector[1] and referencia!= vector[0] ):
        return n-1
    for i in range(n):
        if vector[i] != referencia:
            return i
        
    return -1

t=int(input())
for _ in range(1,t+1):
    n=int(input())
    numeros = input()
    notas = [int(numero) for numero in numeros.split()]
    print(busca(notas,n))