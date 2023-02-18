#Las 2 líneas de código siguiente, van siempre en pygame
import pygame, sys
pygame.init() 

#Defino colores
BLACK = (0,0,0)
WHITE= (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

#Creo tamaño de mi ventana gráfica en una tupla:
size = (800, 500)

#Creo ventana:
screen = pygame.display.set_mode(size)

#Creo un bucle ppal. Todos los juegos por defecto corren dentro de un bucle enorme que se repite.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #color de fondo:
    screen.fill(WHITE)
    #-------------------------------------ZONA DE DIBUJO---------------------------------------------------------------#

    for x in range(100, 700, 100):
	        pygame.draw.rect(screen, BLACK, (x, 230, 50, 50))

    #-------------------------------------ZONA DE DIBUJO---------------------------------------------------------------#

    #Actualizar pantalla:
    pygame.display.flip()
