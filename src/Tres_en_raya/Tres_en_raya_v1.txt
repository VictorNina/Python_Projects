import random

def mostrar(v):
    for fila in v:
        print(fila)

def detecta_ganada(tablero,jugador):
    for i in range(3):
        if tablero[i][0] == jugador and tablero[i][1] == jugador :
            if tablero[i][2]=="-":
                tablero[i][0]=jugador
                return True
        if tablero[i][0] == jugador and tablero[i][2] == jugador :
            if tablero[i][1]=="-":
                tablero[i][1]=jugador
                return True
        if tablero[i][1] == jugador and tablero[i][2] == jugador :
            if tablero[i][0]=="-":
                tablero[i][0]=jugador
                return True

        if tablero[0][i] == jugador and tablero[1][i] == jugador :
            if tablero[2][i]=="-":
                tablero[2][i]=jugador                
                return True
        if tablero[0][i] == jugador and tablero[2][i] == jugador :
            if tablero[1][i]=="-":
                tablero[1][i]=jugador                
                return True
        if tablero[1][i] == jugador and tablero[2][i] == jugador :
            if tablero[0][i]=="-":
                tablero[0][i]=jugador                
                return True
            
        
    if tablero[0][0] == jugador and tablero[1][1] == jugador :
        if tablero[2][2]=="-":
            tablero[2][2]=jugador
            return True
    if tablero[0][0] == jugador and tablero[2][2] == jugador :
        if tablero[1][1]=="-":
            tablero[1][1]=jugador
            return True
    if tablero[1][1] == jugador and tablero[2][2] == jugador :
        if tablero[0][0]=="-":
            tablero[0][0]=jugador
            return True    
        
    if tablero[0][2] == jugador and tablero[1][1] == jugador :
        if tablero[2][0]=="-":
            tablero[2][0]=jugador
            return True    
    if tablero[0][2] == jugador and tablero[2][0] == jugador :
        if tablero[0][2]=="-":
            tablero[0][2]=jugador
            return True 
    if tablero[0][2] == jugador and tablero[2][0] == jugador :
        if tablero[1][1]=="-":
            tablero[1][1]=jugador
            return True 
    return False




def detecta_perdida(tablero,jugador,jugador2):
    for i in range(3):
        if tablero[i][0] == jugador2 and tablero[i][1] == jugador2 :
            if tablero[i][2]=="-":
                tablero[i][0]=jugador
                return True
        if tablero[i][0] == jugador2 and tablero[i][2] == jugador2 :
            if tablero[i][1]=="-":
                tablero[i][1]=jugador
                return True
        if tablero[i][1] == jugador2 and tablero[i][2] == jugador2 :
            if tablero[i][0]=="-":
                tablero[i][0]=jugador
                return True

        if tablero[0][i] == jugador2 and tablero[1][i] == jugador2 :
            if tablero[2][i]=="-":
                tablero[2][i]=jugador                
                return True
        if tablero[0][i] == jugador2 and tablero[2][i] == jugador2 :
            if tablero[1][i]=="-":
                tablero[1][i]=jugador                
                return True
        if tablero[1][i] == jugador2 and tablero[2][i] == jugador2 :
            if tablero[0][i]=="-":
                tablero[0][i]=jugador                
                return True
            
        
    if tablero[0][0] == jugador2 and tablero[1][1] == jugador2 :
        if tablero[2][2]=="-":
            tablero[2][2]=jugador
            return True
    if tablero[0][0] == jugador2 and tablero[2][2] == jugador2 :
        if tablero[1][1]=="-":
            tablero[1][1]=jugador
            return True
    if tablero[1][1] == jugador2 and tablero[2][2] == jugador2 :
        if tablero[0][0]=="-":
            tablero[0][0]=jugador
            return True    
        
    if tablero[0][2] == jugador2 and tablero[1][1] == jugador2 :
        if tablero[2][0]=="-":
            tablero[2][0]=jugador
            return True    
    if tablero[0][2] == jugador2 and tablero[2][0] == jugador2 :
        if tablero[0][2]=="-":
            tablero[0][2]=jugador
            return True 
    if tablero[0][2] == jugador2 and tablero[2][0] == jugador2 :
        if tablero[1][1]=="-":
            tablero[1][1]=jugador
            return True 
    

    
    return False
def ganador(tablero,jugador):
    for i in range(3):
        if tablero[i][0] == jugador and tablero[i][1] == jugador and tablero[i][2] == jugador:
            return True
        
        if tablero[0][i] == jugador and tablero[1][i] == jugador and tablero[2][i] == jugador:
            return True
        
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True
    return False
def empate(tablero):
    sw=False
    for fila in tablero:
        if fila[0]!="-" and fila[1]!="-" and fila[2]!="-":
            sw=True
        else:
            sw=False
    return sw
    
    
def jugar():
    tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    jugador=input("Ingrese queries ser  x u o : ")
    sw=True
    eleccion=input("Deseas empezar primero   Si o No: ")
    if eleccion!="Si":
        sw=False
        if jugador=="x" :
            jugador="o"
        else:
            jugador="x"
    cont=0
    while True:
        mostrar(tablero)
        
        if sw:
            fila,columna=map(int, input("Jugador "+jugador+" ingrese fila y columna: ").split())
            while  fila < 0 or fila > 2 or columna < 0 or columna > 2:
                print("Coordenadas invalidas, por favor intente de nuevo")
                fila,columna=map(int, input("Jugador "+jugador+" ingrese fila y columna: ").split())
            while tablero[fila][columna] != "-":
                print("Esa casilla ya esta ocupada, por favor intente de nuevo")
                fila,columna=map(int, input("Jugador "+jugador+" ingrese fila y columna: ").split())
            tablero[fila][columna]=jugador
            sw=False
        else:
            print("Jugada de la maquina")
            jugador2=""
            if jugador=="x" :
                jugador2="o"
            else:
                jugador2="x"
            if  not detecta_ganada(tablero,jugador):
                if not detecta_perdida(tablero,jugador,jugador2):
                    fila=random.randint(0,2)
                    columna=random.randint(0,2)
                    while tablero[fila][columna] != "-":
                        fila=random.randint(0,2)
                        columna=random.randint(0,2)
                    tablero[fila][columna]=jugador
            sw=True


        cont=cont+1
        if cont>4 :
            if ganador(tablero,jugador):
                mostrar(tablero)
                print("Jugador " + jugador + " gano")
                break
        if cont>=9 :
            print("Empate")
            break

        if jugador=="x" :
            jugador="o"
        else:
            jugador="x"

jugar()