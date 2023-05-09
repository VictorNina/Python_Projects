def programa():
    casos_prueba=int(input())
    for _ in range(casos_prueba):
        cadena=input()
        cadena=cadena.replace(" ","")
        caracteres=set(cadena)
        caracteres=list(caracteres)
        ocurrencias=[]
        for caracter in caracteres:
            ocurrencias.append(cadena.count(caracter))
        if ocurrencias.count(ocurrencias[0])==len(caracteres):
            print("No te lo tomes enserio")
        else:
            print("Meh")

programa()