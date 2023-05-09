def programa():
    casos_prueba=int(input())
    for _ in range(casos_prueba):
        n=int(input())
        vector=list(input().split())
        vector=dir(vector)
        print(vector)

programa()