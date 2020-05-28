#Import a library of functions called 'pygame'
import pygame

#Initialize the game engine
pygame.init()

#Define some colors
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Set the height and width of the screen
size = (1200, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Juego de la Vida")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

#Grid de cuadrados
ancho_cuadro = 15
max_i = size[0] // ancho_cuadro
max_j = size[1] // ancho_cuadro
cuadros = [[0 for j in range(max_j)] for i in range(max_i)]
cuadros_next_gen = [[0 for j in range(max_j)] for i in range(max_i)]

#Dibujar cuadrado
def dibujaCuadro(screen,i,j,cuadros):
    if cuadros[i][j] == 0:
        #Aqui si el cuadro no esta activo
        pygame.draw.rect(screen, (0,0,0), [ancho_cuadro*i, ancho_cuadro*j, ancho_cuadro, ancho_cuadro], 0)
        pygame.draw.rect(screen, (64,64,64), [ancho_cuadro*i, ancho_cuadro*j, ancho_cuadro, ancho_cuadro], 1)
    elif cuadros[i][j] == 1:
        #Aqui si el cuadro esta activo
        pygame.draw.rect(screen, (255,255,255), [ancho_cuadro*i, ancho_cuadro*j, ancho_cuadro, ancho_cuadro], 0)

#Checar si mouse sobre cuadro
def mouseSobreCuadro(x,y,valor):
    global cuadros
    for i in range(len(cuadros)):
        for j in range(len(cuadros[0])):
            #Aqui validamos si el mouse esta posicionado dentro de algun cuadro
            if x >= i*ancho_cuadro and x < (i+1)*ancho_cuadro and y >= j*ancho_cuadro and y < (j+1)*ancho_cuadro:
                cuadros[i][j] = valor

#Codigo para regresar los cuadros a cero
def resetearCuadros():
    global cuadros
    for i in range(len(cuadros)):
        for j in range(len(cuadros[0])):
            cuadros[i][j] = 0

#Funcion auxiliar para contar los vecinos de una celula
def cuentaVecinos(i,j,cuadros):
    vecinos = 0
    m = len(cuadros)
    n = len(cuadros[0])
    #Posicion superior izquierda
    if i-1 >= 0 and j-1 >= 0 and cuadros[i-1][j-1] == 1:
        vecinos += 1
    #Posicion superior central
    if i   >= 0 and j-1 >= 0 and cuadros[i  ][j-1] == 1:
        vecinos += 1
    #Posicion superior derecha
    if i+1 <  m and j-1 >= 0 and cuadros[i+1][j-1] == 1:
        vecinos += 1
    #Posicion central izquierda
    if i-1 >= 0 and j   >= 0 and cuadros[i-1][j  ] == 1:
        vecinos += 1
    #Posicion central derecha
    if i+1 <  m and j   >= 0 and cuadros[i+1][j  ] == 1:
        vecinos += 1
    #Posicion inferior izquierda
    if i-1 >= 0 and j+1 <  n and cuadros[i-1][j+1] == 1:
        vecinos += 1
    #Posicion inferior central
    if i   >= 0 and j+1 <  n and cuadros[i  ][j+1] == 1:
        vecinos += 1
    #Posicion inferior derecha
    if i+1 <  m and j+1 <  n and cuadros[i+1][j+1] == 1:
        vecinos += 1
    return vecinos

#Funcion que implementa las reglas del juego para cambiar de generacion
def siguienteGeneracion():
    global cuadros
    global cuadros_next_gen
    #Hacemos una copia de cuadros a cuadros_next_gen
    for i in range(len(cuadros)):
        for j in range(len(cuadros[0])):
            cuadros_next_gen[i][j] = cuadros[i][j]
    #Implementamos las reglas del juego aquí
    for i in range(len(cuadros)):
        for j in range(len(cuadros[0])):
            numVecinos = cuentaVecinos(i,j,cuadros)
            if cuadros[i][j] == 1:
                if numVecinos == 2 or numVecinos == 3:
                    cuadros_next_gen[i][j] = 1
                else:
                    cuadros_next_gen[i][j] = 0
            if cuadros[i][j] == 0 and numVecinos == 3:
                cuadros_next_gen[i][j] = 1
    #Pasamos de cuadros_next_gen a cuadros
    for i in range(len(cuadros)):
        for j in range(len(cuadros[0])):
            cuadros[i][j] = cuadros_next_gen[i][j]

#Variable para saber si el juego esta corriendo
tiempo = False

#Variable para ajustar los FPS
fps = 0

#Loop as long as done == False
while not done:
    #Manejo de eventos
    for event in pygame.event.get():    # User did something
        if event.type == pygame.QUIT:   # If user clicked close
            done = True                 # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                resetearCuadros()
            if event.key == pygame.K_SPACE:
                tiempo = not tiempo
            if event.key == pygame.K_LEFT:
                if fps > 0:
                    fps -= 5
            if event.key == pygame.K_RIGHT:
                if fps < 30:
                    fps += 5

    #All drawing code happens after the for loop and but
    #inside the main while not done loop.

    #Clear the screen and set the screen background
    screen.fill(WHITE)

    #Manejo de los botones del mouse
    if pygame.mouse.get_pressed()[0]:
        x,y = pygame.mouse.get_pos()
        mouseSobreCuadro(x,y,1)
    if pygame.mouse.get_pressed()[2]:
        x,y = pygame.mouse.get_pos()
        mouseSobreCuadro(x,y,0)

    #Dibujar cada cuadro por separado
    for i in range(max_i):
        for j in range(max_j):
            # Draw a rectangle
            dibujaCuadro(screen,i,j,cuadros)

    #Actualizamos a la nueva generación
    if tiempo:
        siguienteGeneracion()

    #Go ahead and update the screen with what we've drawn.
    #This MUST happen after all the other drawing commands.
    pygame.display.flip()

    #This limits the while loop to a max of 60 times per second.
    #Leave this out and we will use all CPU we can.
    clock.tick(fps)

#Be IDLE friendly
pygame.quit()