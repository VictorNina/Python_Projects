def hacer_palindromo(cadena):
    # Verifica si la cadena ya es palíndromo
    if cadena == cadena[::-1]:
        return cadena
    
    # Añade el primer carácter de la cadena al final y vuelve a llamar a la función
    return cadena + hacer_palindromo(cadena[:-9])


cadena="amanaplanacanal"
print(cadena)
print(hacer_palindromo(cadena))