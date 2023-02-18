
import pygame #(1)
pygame.init()


screen = pygame.display.set_mode([750,744]) #Este es el tamaño de la img que tengo (2)
clock = pygame.time.Clock()#(3)


done = False #variable q me permite salir del bucle ppal.(4)

background = pygame.image.load("perris.jpg").convert() #(7) Cargo la img y hay q almacenarla en una variable.


while not done:#(5)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.blit(background, [0, 0]) #(8) Muestro la img almacenada


#---------------------------------------------------------------------------------------------------------
	pygame.display.flip() #(6)
	clock.tick(60)
pygame.quit()