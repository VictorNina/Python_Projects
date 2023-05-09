def es_palindromo(vector):
    if len(vector) <= 1:
        return True
    if vector[0] != vector[-1]:
        return False
    return es_palindromo(vector[1:-1])


def programa():
    casos_prueba=int(input())
    for _ in range(casos_prueba):
        while True:
            n=int(input())
            if n>=3:
                break
        vector=list(map(int, input().split()))
        if es_palindromo(vector):
            print("YES")
            continue
        max=3
        sw=False
        while max!=n:
            for i in range(n):
                vector_aux=[]
                if(i+max<=n):
                    for j in range(i,max+i):
                        vector_aux.append(vector[j])
                    if es_palindromo(vector_aux):
                        print("YES")
                        sw=True
                else:
                    i=n-1
            max+=1
            if not sw :
                print("NO")
            else:
                break
            
programa()