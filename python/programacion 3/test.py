lista = ["a", "b", "c", "d", "e"]

def a(n, pos):
    for i in lista:
        if i == pos and pos != len(lista)-1:
            lista[i] = n
            mover = True
        if mover:
            
            
