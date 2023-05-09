def eliminar_por_izquierda_recursiva(cadena, eliminados=""):
    if cadena == "":
        return eliminados
    eliminado = cadena[0]
    cadena = cadena[1:]
    eliminados = eliminado+eliminados
    
    return eliminar_por_izquierda_recursiva(cadena, eliminados)

cadena = "hola mundo"
eliminados = eliminar_por_izquierda_recursiva(cadena)
print(eliminados)
print(cadena)


