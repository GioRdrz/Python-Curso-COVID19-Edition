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
    