import math

def es_primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i*i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

t = int(input())
for i in range(1, t+1):
    n = int(input())
    if es_primo(n):
        print(str(n) + ": ", end="")
        r = 1/n
        de = "{:.40f}".format(r)
        for j in range(2, len(de)):
            print(de[j] + " ", end="")
        print()
    else:
        print(str(n) + ": -1")
