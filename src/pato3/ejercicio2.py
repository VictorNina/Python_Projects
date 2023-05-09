#def suma(a,b,c):

while True:
    try:
        a,b=map(int, input().split())
        if not a and not b:
            break
        vector=list(map(int, input().split()))
        print(vector)

    except:
        break