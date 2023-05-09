def programa():
    casos_prueba=int(input())
    for _ in range(casos_prueba):
        n,m,e=map(int, input().split())
        nombre_pokemon={}
        pokemon_ganador=[]
        for i in range(n):
            pokemon=input()
            nombre_pokemon[pokemon]=0
            pokemon_ganador.append(pokemon)
        for pokemon in nombre_pokemon.keys():
            batallas_ganadas=pokemon_ganador.count(pokemon)
            nombre_pokemon[pokemon]=batallas_ganadas*e

        max_pokemon=max(nombre_pokemon, key=nombre_pokemon.get)
        max_point=nombre_pokemon[max_pokemon]
        points_for_level=list(map(int, input().split()))
        point_level=0
        for i in range(m):
            point_level=point_level+points_for_level[i]
            if 10<point_level:
                print(i)
                break
            elif 10==point_level:
                print(i+1)
                break
programa()

