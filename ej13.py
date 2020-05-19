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
size = (600, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Cuadritos del Gio")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

#Grid de cuadrados
max_i = 54
max_j = 36
cuadros = [[0 for j in range(max_j)] for i in range(max_i)]

#Dibujar cuadrado
def dibujaCuadro(screen,i,j,cuadros):
    if cuadros[i][j] == 0:
        #Aqui si el cuadro no esta activo
        pygame.draw.rect(screen, (0,0,0), [11*i+1, 11*j+1, 10, 10], 0)
    elif cuadros[i][j] == 1:
        #Aqui si el cuadro esta activo
        pygame.draw.rect(screen, (255,255,255), [11*i+1, 11*j+1, 10, 10], 0)

#Checar si mouse sobre cuadro
def mouseSobreCuadro(x,y):
    global cuadros
    for i in range(len(cuadros)):
        for j in range(len(cuadros[0])):
            #Aqui validamos si el mouse esta posicionado dentro de algun cuadro
            if x >= i*11 and x < (i+1)*11 and y >= j*11 and y < (j+1)*11:
                cuadros[i][j] = 1

#Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    #All drawing code happens after the for loop and but
    #inside the main while not done loop.

    #Clear the screen and set the screen background
    screen.fill(WHITE)

    if pygame.mouse.get_pressed()[0]:
        x,y = pygame.mouse.get_pos()
        mouseSobreCuadro(x,y)

    for i in range(max_i):
        for j in range(max_j):
            # Draw a rectangle
            dibujaCuadro(screen,i,j,cuadros)

    #Go ahead and update the screen with what we've drawn.
    #This MUST happen after all the other drawing commands.
    pygame.display.flip()

    #This limits the while loop to a max of 60 times per second.
    #Leave this out and we will use all CPU we can.
    clock.tick(15)

#Be IDLE friendly
pygame.quit()