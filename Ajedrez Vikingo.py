#Tablero

#Estado del juego, tupla de tablero y jugador actual 1 negro 2 blanco

#Movimiento tupla de 4 numeros, (fila inicial, columna inicial, fila final, columnafinal)

#Estado inicial
#0 casilla vacia, 1 casilla ocupada por peon negro, 2 casilla ocupada por peon blanco y 3 casilla ocupada por el rey blanco

from calendar import c
from hashlib import new
import random
import ast


def estado_inicial(variante):
    if variante == 1:
        #Hnefatafl 
        tablero = ([0,0,0,1,1,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,2,0,0,0,0,1],[1,0,0,0,2,2,2,0,0,0,1],[1,1,0,2,2,3,2,2,0,1,1],[1,0,0,0,2,2,2,0,0,0,1],[1,0,0,0,0,2,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,1,1,1,1,1,0,0,0])
    if variante == 2:
        #Tablut
        tablero = ([0,0,0,1,1,1,0,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,0,2,0,0,0,0],[1,0,0,0,2,0,0,0,1],[1,1,2,2,3,2,2,1,1],[1,0,0,0,2,0,0,0,1],[0,0,0,0,2,0,0,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,1,1,1,0,0,0])
    if variante == 3:
        #Ard Ri
        tablero = ([0,0,1,1,1,0,0],[0,0,0,1,0,0,0],[1,0,2,2,2,0,1],[1,1,2,3,2,1,1],[1,0,2,2,2,0,1],[0,0,0,1,0,0,0],[0,0,1,1,1,0,0])
    if variante == 4:
        #Brandubh
        tablero = ([0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,2,0,0,0],[1,1,2,3,2,1,1],[0,0,0,2,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0])
    if variante == 5:
        #Tawlbwrdd
        tablero = ([0,0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,2,0,0,0,0,0],[1,1,0,0,2,2,2,0,0,1,1],[1,0,1,2,2,3,2,2,1,0,1],[1,1,0,0,2,2,2,0,0,1,1],[0,0,0,0,0,2,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,1,0,0,0,0],[0,0,0,0,1,1,1,0,0,0,0])
    if variante == 6:
        #Alea Evangelii
        tablero = ([0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,2,0,2,0,1,0,0,0,0,0,0],[1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1],[0,0,0,0,1,0,0,0,0,2,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,2,0,2,0,0,0,0,1,0,0,0],[0,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,0],[0,0,0,1,0,0,2,0,0,3,0,0,2,0,0,1,0,0,0],[0,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,0],[0,0,0,1,0,0,0,0,2,0,2,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,2,0,0,0,0,1,0,0,0,0],[1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1],[0,0,0,0,0,0,1,0,2,0,2,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0],[1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0])
    if variante == 7:
        #Prueba
        tablero = ([0,0,0,0,1,0,0],
                   [1,2,0,1,2,0,0],
                   [1,2,1,3,0,1,1],
                   [1,1,2,0,2,1,1],
                   [0,0,0,1,1,2,1],
                   [0,0,2,1,1,0,0],
                   [0,0,1,0,0,0,0])
    estado=(tablero,(1))
    return estado

#Creamos una funcion la cual convierte la coordenada i en las coordenadas que usamos visualmente, ya que la i del indice empieza en 0 pero seria la ultima coordenada del tablero
def cambio_coordenada(len,i):
    newI=len-1-i
    return newI

#Se comprueban los diferentes movimientos posibles de los peones dependiendo del jugador que le toque jugar, comprobando que no accedan a las casillas prohibidas( esquinas y centro )
def obtiene_movimiento_peon(tablero, jugador):
    movimientos = []
    numer_filas = len(tablero)
    #Recorre todas las filas en busca un 1
    movimientos = []
    movimiento=(0,0,0,0)
    for i in range(0,numer_filas):
        if(jugador in tablero[i]):
            for j in range(0,len(tablero[i])):
                if(tablero[i][j]==jugador):
                    #Se crea una variable nueva de I la cual transforma a coordenada de tablero, ya que la matriz empieza en 0 y en el tablero seria la coordenada ultima de la matriz
                    newI=numer_filas-1-i
                    izq=j-1
                    der=j+1
                    arr=i-1
                    abj=i+1                    
                    while(izq>=0):
                        if(tablero[i][izq]==0):
                            #Se comprueba que la casilla no sea la esquina superior ni inferior izquierda, ni el centro
                            if((izq,newI)!=(0,0) and (izq,newI)!=(0,numer_filas-1) and (izq,newI)!=((numer_filas-1)/2,(numer_filas-1)/2)):
                                movimiento=(j,newI,izq,newI)
                                movimientos.append(movimiento)
                            #se verifica que la nueva coordenada de la izquierda no se salgan del tablero y si es asi se prueba con una casilla mas a la izquierda
                            if(izq>0):
                                izq=izq-1
                            else:
                                break
                        else:
                            break
                    while(der<=len(tablero[i])-1):
                        if(tablero[i][der]==0):
                            #Se comprueba que la casilla no sea la esquina superior ni inferior derecha, ni el centro
                            if((der,newI)!=(numer_filas-1,numer_filas-1) and (der,newI)!=(numer_filas-1,0) and (der,newI)!=((numer_filas-1)/2,(numer_filas-1)/2)):
                                movimiento=(j,newI,der,newI)
                                movimientos.append(movimiento)          
                            #se verifica que la nueva coordenada de la derecha no se salga del tablero y si es asi se prueba con una casilla mas a la derecha
                            if(der<len(tablero[i])-1):
                                der=der+1
                            else:
                                break
                        else:
                            break
                    while(arr>=0):
                        if(tablero[arr][j]==0):
                            newArr = cambio_coordenada(numer_filas,arr)
                            #Se comprueba que la casilla no sea la esquina superior derecha ni izquierda, ni el centro
                            if((j,newArr)!=(0,numer_filas-1) and (j,newArr)!=(numer_filas-1,numer_filas-1) and (j,newArr)!=((numer_filas-1)/2,(numer_filas-1)/2)):
                                movimiento=(j,newI,j,newArr)
                                movimientos.append(movimiento)
                            #se verifica que la nueva coordenada de arriba no se salga del tablero y si es asi se prueba con una casilla mas a arriba
                            if(arr>0):
                                arr=arr-1
                            else:
                                break
                        else:
                            break
                    while(abj<=len(tablero)-1):
                        if(tablero[abj][j]==0):
                            newAbj=cambio_coordenada(numer_filas,abj)
                            #Se comprueba que la casilla no sea la esquina inferior derecha ni izquierda, ni el centro
                            if((j,newAbj)!=(0,0) and (j,newAbj)!=(numer_filas-1,0) and (j,newAbj)!=((numer_filas-1)/2,(numer_filas-1)/2)):
                                movimiento=(j,newI,j,newAbj)
                                movimientos.append(movimiento)
                            #se verifica que la nueva coordenada de abajo no se salga del tablero y si es asi se prueba con una casilla mas a abajo
                            if(abj<len(tablero)-1):
                                abj=abj+1
                            else:
                                break
                        else:
                            break
    #Eliminar de la lista de movimientos los cuales acaban en las esquinas y en el centro del tablero
    
    return movimientos

#Se comprueban los posibles movimientos del rey ya que este puede llegar a las esquinas y el centro cosa que los peones no, la función sera muy parecida solo quitabdo las comprobaciones
def obtiene_movimientos_rey(tablero):
    movimientos = []
    rey = 3
    numer_filas = len(tablero)
    #Recorre todas las filas en busca de un 2 o un 3 las cuales son las fichas del jugador blanco
    movimientos = []
    movimiento=(0,0,0,0)
    for i in range(0,len(tablero)):
        if(rey in tablero[i]):
            for j in range(0,len(tablero[i])):
                if(tablero[i][j]==rey):
                    #Se crea una variable nueva de I la cual transforma a coordenada de tablero, ya que la matriz empieza en 0 y en el tablero seria la coordenada ultima de la matriz
                    newI=cambio_coordenada(numer_filas,i)
                    izq=j-1
                    der=j+1
                    arr=i-1
                    abj=i+1                    
                    while(izq>=0):
                        if(tablero[i][izq]==0):
                            movimiento=(j,newI,izq,newI)
                            movimientos.append(movimiento)
                            #se verifica que la nueva coordenada de la izquierda no se salgan del tablero y si es asi se prueba con una casilla mas a la izquierda
                            if(izq>0):
                                izq=izq-1
                            else:
                                break
                        else:
                            break
                    while(der<=len(tablero[i])-1):
                        if(tablero[i][der]==0):
                            movimiento=(j,newI,der,newI)
                            movimientos.append(movimiento)          
                            #se verifica que la nueva coordenada de la derecha no se salga del tablero y si es asi se prueba con una casilla mas a la derecha
                            if(der<len(tablero[i])-1):
                                der=der+1
                            else:
                                break
                        else:
                            break
                    while(arr>=0):
                        if(tablero[arr][j]==0):
                            newArr=cambio_coordenada(numer_filas,arr)
                            movimiento=(j,newI,j,newArr)
                            movimientos.append(movimiento)
                            #se verifica que la nueva coordenada de arriba no se salga del tablero y si es asi se prueba con una casilla mas a arriba
                            if(arr>0):
                                arr=arr-1
                            else:
                                break
                        else:
                            break
                    while(abj<=len(tablero)-1):
                        if(tablero[abj][j]==0):
                            newAbj=cambio_coordenada(numer_filas,abj)
                            movimiento=(j,newI,j,newAbj)
                            movimientos.append(movimiento)
                            #se verifica que la nueva coordenada de abajo no se salga del tablero y si es asi se prueba con una casilla mas a abajo
                            if(abj<len(tablero)-1):
                                abj=abj+1
                            else:
                                break
                        else:
                            break
    return movimientos

#Creamos una funcion que nos devuelve una lista de movimientos posibles para cada jugador, ya que cada jugador tiene unas fichas diferentes
def obtiene_movimientos_negras(tablero):
    return obtiene_movimiento_peon(tablero,1)

def obtiene_movimientos_blancas(tablero):
    movimientos=obtiene_movimiento_peon(tablero,2)+obtiene_movimientos_rey(tablero)
    return movimientos

#Comprueba que jugador le toca jugar para comprobar sus movimientos
def obtiene_movimientos(estado):
    jugador = estado[1]
    tablero = estado[0]
    if(jugador==1):
        movimientos = obtiene_movimientos_negras(tablero)
    else:
        movimientos = obtiene_movimientos_blancas(tablero)
    return random.sample(movimientos, len(movimientos))
    
#Se comprueban si algun jugador esta en un estado final de victoria
def ganan_negras(estado, numero_de_movimientos):
    tablero = estado[0]
    resultado = True
    for i in range(0,len(tablero)):
        if(3 in tablero[i]):
            resultado=False
            break
    return resultado

def ganan_blancas(estado, numero_de_movimientos):
    tablero = estado[0]
    resultado = False
    #Comprobar que el valor de las casillas de las esquinas del tablero es 3
    if(tablero[0][0]==3 or tablero[0][len(tablero[0])-1]==3 or tablero[len(tablero)-1][0]==3 or tablero[len(tablero)-1][len(tablero[0])-1]==3):
        resultado=True
    return resultado

def es_estado_final(estado, numero_de_movimientos):
    if(numero_de_movimientos==0):
        return True
    else:
        negras_ganan = ganan_negras(estado, numero_de_movimientos)
        blancas_ganan = ganan_blancas(estado, numero_de_movimientos)
        return blancas_ganan or negras_ganan

def imprime_tablero(tablero):
    numer_filas=len(tablero)
    #Recorremos el tablero e imprimimos en consola el valor de cada casilla siendo 
    #0=vacio, 1=negras, 2=blancas, 3=rey
    for i in range(0,len(tablero)): 
        print("\n", cambio_coordenada(numer_filas,i), end=" ")
        if(cambio_coordenada(numer_filas,i)<10):
            print(" ", end="")
        for j in range(0,len(tablero[i])):
            if(tablero[i][j]==0):
                print("______", end=" ")
            elif(tablero[i][j]==1):
                print(" Negra", end=" ")
            elif(tablero[i][j]==2):
                print("Blanca", end=" ")
            elif(tablero[i][j]==3):
                print("  Rey ", end=" ")
    print("\n")
    for i in range(0,len(tablero[0])):
        if(i==0):
            print("      ",i, end="")
        elif(i>=10):
            print("    ", i, end="")
        else:
            print("     ", i, end= "")
    print("\n")


def imprime_estado(estado, numero_de_movimientos):
    tablero = estado[0]
    #Recorremos el tablero e imprimimos en consola el valor de cada casilla siendo 
    #0=vacio, 1=negras, 2=blancas, 3=rey
    imprime_tablero(tablero)
    jugador = estado[1]   
    #Se comprueba si el estado es final y se imprime el resultado dependiendo del jugador que haya jugado anteriormente
    final=es_estado_final(estado, numero_de_movimientos)
    if(final):
        if(jugador==1):
            print("Ganan blancas")
            return True
        else:
            print("Ganan negras")
            return True
    #Si el numero de movimientos es 0 la partida acaba en tablas
    #elif(nume_jugadas==0):
    #    print("Tablas")
    #    return True
    #Si no es estado final se imprime jugador y sus posibles movimientos
    else:
        if(jugador==1):
            print("Juegan negras")
        else:
            print("Juegan blancas")
        print("Posibles movimientos: ",numero_de_movimientos)

def aplica_movimiento(estado, movimiento):
    tablero = estado[0]
    numer_filas=len(tablero)
    jugador = estado[1]
    #Obtenemos el tipo de fichas del jugador que juega y las del rival
    if(jugador==1):
        fichas_jugador=(1,)
        fichas_rival=(2,3)
    else:
        fichas_jugador=(2,3)
        fichas_rival=(1,)
    newTablero = tablero
    #Obtenemos las coordenadas del movimiento, las actuales y a las finales, y convertimos la variable I que como ya hemos comentado antes esta al reves de los indices
    actualI=cambio_coordenada(numer_filas,movimiento[1])
    actualJ=movimiento[0]
    newI=cambio_coordenada(numer_filas,movimiento[3])
    newJ=movimiento[2]
    #Obtenemos el tipo de ficha que se mueve
    ficha = tablero[actualI][actualJ]
    #Movemos las fichas en el nuevo tablero
    newTablero[actualI][actualJ]=0
    newTablero[newI][newJ]=ficha
    #Luego se comprueba si en los lados de la pieza hay una ficha contraria para mirar si es comida a excepcion de si es el medio el cual se evalua diferente
    arr=newI-1
    abj=newI+1
    izq=newJ-1
    der=newJ+1
    vecinos_movimiento=((arr,newJ),(abj,newJ),(newI,izq),(newI,der))
    coord_centro=int((numer_filas-1)/2)
    centro=(coord_centro,coord_centro)
    centro_y_vecinos_centro=(centro,(coord_centro,coord_centro+1),(coord_centro,coord_centro-1),(coord_centro-1,coord_centro),(coord_centro+1,coord_centro))
    #Se comprueba en que tipo de movimiento estamos en cuanto a captura; la pieza capturada esta en el centro, esta en una vecina del centro o se encueentra en una posicion normal
    #Este caso es que la ficha a comer esta en el centro el cual debe ser rodeado por los 3 lados
    if(centro in vecinos_movimiento):
        if(tablero[coord_centro][coord_centro] in fichas_rival):
            if(newTablero[coord_centro][coord_centro+1] in fichas_jugador and newTablero[coord_centro][coord_centro-1] in fichas_jugador and newTablero[coord_centro-1][coord_centro] in fichas_jugador and newTablero[coord_centro+1][coord_centro] in fichas_jugador):
                newTablero[coord_centro][coord_centro]=0
                
    #Este caso es que la ficha a comer esta en una vecina del centro la cual debe ser rodeada por los 3 lados sin contar el centro
    if((coord_centro,coord_centro+1) in vecinos_movimiento):
        if(tablero[coord_centro][coord_centro+1] in fichas_rival):
            if(newTablero[coord_centro+1][coord_centro+1] in fichas_jugador and newTablero[coord_centro-1][coord_centro+1] in fichas_jugador and newTablero[coord_centro][coord_centro+2] in fichas_jugador):
                newTablero[coord_centro][coord_centro+1]=0
    if((coord_centro,coord_centro-1) in vecinos_movimiento):
        if(tablero[coord_centro][coord_centro-1] in fichas_rival):
            if(newTablero[coord_centro-1][coord_centro-1] in fichas_jugador and newTablero[coord_centro+1][coord_centro-1] in fichas_jugador and newTablero[coord_centro][coord_centro-2] in fichas_jugador):
                newTablero[coord_centro][coord_centro-1]=0
    if((coord_centro+1,coord_centro) in vecinos_movimiento):
        if(tablero[coord_centro+1][coord_centro] in fichas_rival):
            if(newTablero[coord_centro+2][coord_centro] in fichas_jugador and newTablero[coord_centro+1][coord_centro+1] in fichas_jugador and newTablero[coord_centro+1][coord_centro-1] in fichas_jugador):
                newTablero[coord_centro+1][coord_centro]=0
    if((coord_centro-1,coord_centro) in vecinos_movimiento):
        if(tablero[coord_centro-1][coord_centro] in fichas_rival):
            if(newTablero[coord_centro-2][coord_centro] in fichas_jugador and newTablero[coord_centro-1][coord_centro+1] in fichas_jugador and newTablero[coord_centro-1][coord_centro-1] in fichas_jugador):
                newTablero[coord_centro-1][coord_centro]=0
                
    #Este caso es el normal el cual aplica al encerrar una ficha entre dos tuyas, tambien se comprueba si la ficha esta conjunta a la esquina la cual actua como una ficha compañera
    if(arr>0):
        if(tablero[arr][newJ] in fichas_rival and ((arr,newJ) in centro_y_vecinos_centro)==False):
            if((arr-1==0) and (newJ==0 or newJ==numer_filas-1)):
                newTablero[arr][newJ]=0
            elif(tablero[arr-1][newJ] in fichas_jugador):
                newTablero[arr][newJ]=0
    if(abj<numer_filas-1):
        if(tablero[abj][newJ] in fichas_rival and ((abj,newJ) in centro_y_vecinos_centro)==False):
            if((abj+1==numer_filas-1) and (newJ==0 or newJ==numer_filas-1)):
                newTablero[abj][newJ]=0
            elif(tablero[abj+1][newJ] in fichas_jugador):
                newTablero[abj][newJ]=0
    if(izq>0):
        if(tablero[newI][izq] in fichas_rival and ((newI,izq) in centro_y_vecinos_centro)==False):
            if((izq-1==0) and (newI==0 or newI==numer_filas-1)):
                newTablero[newI][izq]=0
            elif(tablero[newI][izq-1] in fichas_jugador):
                newTablero[newI][izq]=0
    if(der<numer_filas-1):
        if(tablero[newI][der] in fichas_rival and ((newI,der) in centro_y_vecinos_centro)==False):
            if((der+1==numer_filas-1) and (newI==0 or newI==numer_filas-1)):
                newTablero[newI][der]=0
            elif(tablero[newI][der+1] in fichas_jugador):
                newTablero[newI][der]=0
                
    if(ficha==1):
        newEstado=(newTablero, 2)
    else:
        newEstado=(newTablero, 1)
    return newEstado
         
#Se pide un movimiento y se comprueba que sea un movimiento valido antes de aplicarlo
def movimiento_valido(estado, movimientos):
    movimiento = ast.literal_eval(input("Movimiento: "))
    if(movimiento in movimientos):
        return aplica_movimiento(estado, movimiento)
    else:
        print("Movimiento no valido, aplica un movimiento valido")
        return movimiento_valido(estado, movimientos)
    
#def busca_solucion(estado, tiempo):

def elige_variante():
    #Se pide al usuario que seleccione una variante de juego
    print("Seleccione una variante de juego:")
    #Se listan las variantes de juego disponibles
    print(" 1 - Hnefatafl \n 2 - Tablut \n 3 - Ard Ri \n 4 - Brandubh \n 5 - Tawlbwrdd \n 6 - Alea Evangelii")
    #Se lee el numero de variante seleccionada
    variante = int(input("Variante: "))
    #Si el caracter introducido no es un numero entre el 1 y el 6 se vuelve a pedir otra vez
    if(variante<1 or variante>7):
        print("Variante incorrecta")
        elige_variante()
    return variante

def elige_numero_turnos():
    numero_turnos = int(input("Numero de turnos a jugar antes de terminar en tablas: "))
    if(numero_turnos<1):
        print("Variante incorrecta")
        elige_numero_turnos()
    return numero_turnos

def interfaz_usuario():
    #Se pide al usuario que seleccione una variante de juego
    variante=elige_variante()
    #Se pide al usuario que seleccione un numero de turnos a jugar antes de terminar en tablas
    numero_turnos=elige_numero_turnos()
    #Se crea el estado inicial y una variable que indica el fin de la partida
    estado = estado_inicial(variante)
    fin = False
    while(fin!=True and numero_turnos>0):
        #Se obtienen los posibles movimientos y se imprime el estado actual
        movimientos = obtiene_movimientos(estado)
        num_movimientos = len(movimientos)
        fin = imprime_estado(estado, num_movimientos)
        #Se imprimen los posibles movimientos del jugador
        if(fin!=True):
            print(movimientos)
            #Se pide un movimiento y se verifica que sea valido, si lo es se aplica y se pasa al turno del nuevo jugador
            newEstado = movimiento_valido(estado, movimientos)
            estado = newEstado
            numero_turnos-=1
    if(numero_turnos==0):
        print("Tablas, se acabaron los turnos")
           
         
def main():
    interfaz_usuario()
        
if __name__ == "__main__":
    main()