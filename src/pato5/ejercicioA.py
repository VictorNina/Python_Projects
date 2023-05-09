def programa():
    casos_prueba=int(input())
    for _ in range(casos_prueba):
        n=int(input())
        vector=list(map(int, input().split()))
        vector=set(vector)
        vector=list(vector)
        vector.sort()
        if len(vector)>2:
            print(vector[1])
        else:
            print("NO")

programa()