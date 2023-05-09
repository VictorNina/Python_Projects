def hacer_palindromo(cadena):
    if cadena == cadena[::-1]:
        return cadena
    
    n = len(cadena)
    start = 0
    end = 0
    
    for i in range(n):
        len1 = expandir_desde_centro(cadena, i, i) # Caso impar
        len2 = expandir_desde_centro(cadena, i, i+1) # Caso par
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return cadena + cadena[start:end][::-1]

def expandir_desde_centro(cadena, left, right):
    n = len(cadena)
    while left >= 0 and right < n and cadena[left] == cadena[right]:
        left -= 1
        right += 1
    return right - left - 1

while True:
    n = input()
    if n == "END":
        break
    n = hacer_palindromo(n)
    print(n)
