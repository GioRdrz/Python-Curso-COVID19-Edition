# - X O
# 0 1 2

tablero = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def JuegoTerminado(matriz):

    m = matriz
    ganador = '-'
    if m[0][0] == 1 and m[0][1] == 1 and m[0][2] == 1:
        ganador = "X"
    elif m[1][0] == 1 and m[1][1] == 1 and m[1][2] == 1:
        ganador = "X"
    elif m[2][0] == 1 and m[2][1] == 1 and m[2][2] == 1:
        ganador = "X"
    elif m[0][0] == 1 and m[1][0] == 1 and m[2][0] == 1:
        ganador = "X"
    elif m[0][1] == 1 and m[1][1] == 1 and m[2][1] == 1:
        ganador = "X"
    elif m[0][2] == 1 and m[1][2] == 1 and m[2][2] == 1:
        ganador = "X"
    elif m[0][0] == 1 and m[1][1] == 1 and m[2][2] == 1:
        ganador = "X"
    elif m[0][2] == 1 and m[1][1] == 1 and m[2][0] == 1:
        ganador = "X"
    elif m[0][0] == 2 and m[0][1] == 2 and m[0][2] == 2:
        ganador = "O"
    elif m[1][0] == 2 and m[1][1] == 2 and m[1][2] == 2:
        ganador = "O"
    elif m[2][0] == 2 and m[2][1] == 2 and m[2][2] == 2:
        ganador = "O"
    elif m[0][0] == 2 and m[1][0] == 2 and m[2][0] == 2:
        ganador = "O"
    elif m[0][1] == 2 and m[1][1] == 2 and m[2][1] == 2:
        ganador = "O"
    elif m[0][2] == 2 and m[1][2] == 2 and m[2][2] == 2:
        ganador = "O"
    elif m[0][0] == 2 and m[1][1] == 2 and m[2][2] == 2:
        ganador = "O"
    elif m[0][2] == 2 and m[1][1] == 2 and m[2][0] == 2:
        ganador = "O"

    return ganador

def Num2Letter(num):
    if num == 0:
        return " "
    if num == 1:
        return "X"
    if num == 2:
        return "O"

def MuestraTablero(matriz):
    m = matriz
    tableroStr = """
      1   2   3
     ___________
    |   |   |   |
 1  | {} | {} | {} |
    |___|___|___|
    |   |   |   |
 2  | {} | {} | {} |
    |___|___|___|
    |   |   |   |
 3  | {} | {} | {} |
    |___|___|___|
    """.format(
        Num2Letter(m[0][0]),
        Num2Letter(m[0][1]),
        Num2Letter(m[0][2]),
        Num2Letter(m[1][0]),
        Num2Letter(m[1][1]),
        Num2Letter(m[1][2]),
        Num2Letter(m[2][0]),
        Num2Letter(m[2][1]),
        Num2Letter(m[2][2])
    )
    print(tableroStr)

print(" === JUEGO DEL GATO | TIC TAC TOE === ")

while True:

    MuestraTablero(tablero)
    print("TURNO DE 'X'")
    while True:
        p_i = int(input("Ingresa la fila: "))-1
        p_j = int(input("Ingresa la columna: "))-1
        if tablero[p_i][p_j] == 0:
            tablero[p_i][p_j] = 1
            break
        else:
            print("Ingresa posiciones vacias.")
    posibleGanador = JuegoTerminado(tablero)
    if posibleGanador != '-':
        print("El juego ha terminado. {} es el ganador!!!".format(posibleGanador))
        break
    MuestraTablero(tablero)
    print("TURNO DE 'O'")
    while True:
        p_i = int(input("Ingresa la fila: "))-1
        p_j = int(input("Ingresa la columna: "))-1
        if tablero[p_i][p_j] == 0:
            tablero[p_i][p_j] = 2
            break
        else:
            print("Ingresa posiciones vacias.")
    posibleGanador = JuegoTerminado(tablero)
    if posibleGanador != '-':
        print("El juego ha terminado. {} es el ganador!!!".format(posibleGanador))
        break