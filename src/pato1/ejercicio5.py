from collections import Counter

vector = [2, 2, 3, 2, 2, 2, 2, 2]

# Obtener el elemento distinto
contador = Counter(vector)
elemento_distinto = [x for x in contador if contador[x] == 1][0]

# Encontrar la posición del elemento distinto
posicion = vector.index(elemento_distinto)

print(f"El elemento distinto {elemento_distinto} está en la posición {posicion}")
