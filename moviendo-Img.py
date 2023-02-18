import pygame #(1)
pygame.init()


screen = pygame.display.set_mode([720,720])
clock = pygame.time.Clock()
pygame.mouse.set_visible(0) #p/que no se vea el puntero. Si escribo 1, sí se muestra.


done = False

#-------------------------------------------------------------------cargo img
background = pygame.image.load("background.png").convert()
player = pygame.image.load("player.png").convert()
player.set_colorkey([0,0,0]) #--------------------------------------p/sacar el fondo de la ima de la nave pq se veía negro
                             #---------entre [] va el color q se quiere remover; en formato RGB.

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

#----------------------------------------------------------se obtienen las coord. del mouse p/poder mover la img
	mouse_pos = pygame.mouse.get_pos()
	x = mouse_pos[0]
	y = mouse_pos[1]


#----------------------------------------------------------coloco las img en la screen
	screen.blit(background, [0, 0])
	screen.blit(player, [x, y]) #las coord del mouse



#-------------------------------------------------------------------------------------------------------
	pygame.display.flip()
	clock.tick(60)
pygame.quit()