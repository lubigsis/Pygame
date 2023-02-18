# Se obtienen las coordenadas del ratón para desplazar el cuadrado.

import pygame, sys
pygame.init()

BLACK = (0,0,0)
WHITE= (255,255,255)
RED = (255,0,0)
size = (800, 500)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.mouse.set_visible(0) #p/que no se vea el puntero. Si escribo 1, sí se muestra.

#-----------------------------------------------------------------------------------

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


	mouse_pos = pygame.mouse.get_pos()   #p/obtener coord.
	x = mouse_pos[0]  #almaceno valor X 
	y = mouse_pos[1]  #almaceno valor Y


	screen.fill(WHITE)
	pygame.draw.rect(screen, RED, (x, y, 100, 100))


	pygame.display.flip()
	clock.tick(60)