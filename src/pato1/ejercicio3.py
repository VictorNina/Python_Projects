
while True:
    entrada=input()
    if not entrada:
        break
    for caracter in entrada:
        valor_ascii = ord(caracter)
        binario = format(valor_ascii, "08b")
        mitad = len(binario) // 2
        parte1 = binario[:mitad]
        parte2 = binario[mitad:]
        a=parte2+parte1
        numero=int((a),base=2)
        if(caracter==entrada[len(entrada)-1]):
            print(numero)
        else:
            print(numero,end=" ")
        