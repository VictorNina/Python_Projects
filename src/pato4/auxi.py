from itertools import product

lista = [1, 2, 3]
r = 2
combinaciones = []

# Genera todas las posibles combinaciones con repetición tomados de r en r
for comb in product(lista, repeat=r):
    # Divide la combinación en dos vectores de longitud igual
    a = list(comb)
    b = [x for x in lista if x not in a]
    # Agrega la combinación a la lista de combinaciones
    combinaciones.append((a, b))

# Imprime la lista de combinaciones
print(combinaciones)
