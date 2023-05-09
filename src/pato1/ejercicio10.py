import sympy
n=int(input())
cont=0
for _ in range(1,n+1):
    x=int(input())
    suma=0
    while(x!=0):
        digito=x%10
        x=x//10
        if(sympy.isprime(digito)):
            suma=suma+digito
    print(suma)
    if(suma%2==0):
        cont+cont+1
print(cont)


