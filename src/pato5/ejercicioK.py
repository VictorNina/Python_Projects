def programa():
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    c=list(map(int, input().split()))
    cont=0
    for numero in c:
        if b[numero-1] in a:
            contar=a.count(b[numero-1])
            cont=cont+contar
    print(cont)

programa()