n=input()
pal=n.split()
n=' '.join(pal)
palabras = n.split(" ")
for i in range(palabras.__len__()):
    if "o" in palabras[i].lower():
        print(palabras[i].strip(","))