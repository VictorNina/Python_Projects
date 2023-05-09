import sympy
def promedios(primos,n):
    for i in range(n-1):
        print((primos[i]+primos[i+1])//2)

def programa():
    casos_prueba=int(input())
    for _ in range(casos_prueba):
        cant_lote=int(input())
        primos=[]
        for i in range(1,cant_lote+1):
            valor=int(input())
            if sympy.isprime(valor):
                primos.append(valor)

        if len(primos)<=1:
            print("No existen promedios")
        else:
            promedios(primos,len(primos))
    
programa()