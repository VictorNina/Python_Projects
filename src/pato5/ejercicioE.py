def programa():
    while True:
        try:
            n=int(input())
            heros=set()
            for _ in range(n):
                vector=list(input().split())
                nhero=int(vector[0])
                for i in range(1,nhero+1,1):
                    heros.add(vector[i])
            heros=list(heros)
            heros.sort()
            hero_problem=input()
            print(heros.index(hero_problem))

        except:
            break   


programa()
