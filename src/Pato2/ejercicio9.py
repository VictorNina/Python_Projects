def hacer_palindromo(cadena):
    # Si la cadena es palíndroma, devolverla tal cual
    if cadena == cadena[::-1]:
        return cadena
    
    encontrado = False
    inicio = 0
    fin = len(cadena) - 1
    
    while not encontrado and inicio < fin:
        if cadena[inicio] == cadena[fin]:
            subcadena = cadena[inicio:fin+1]
            if subcadena == subcadena[::-1]:
                encontrado = True
        if not encontrado:
            if len(cadena[inicio+1:fin+1]) > len(cadena[inicio:fin]):
                inicio += 1
            else:
                fin -= 1
    
    if encontrado:
        return cadena + cadena[inicio::-1] + cadena[fin+1:]
    else:
        return cadena + cadena[:-1][::-1]

# Ejemplo de uso
while True:
    n = input()
    if n == "END":
        break
    n = hacer_palindromo(n)
    print(n)
