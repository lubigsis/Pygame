import pygame, sys, random
pygame.init()

#-------------------------------------------------defino colores
WHITE= (255,255,255)
RED = (255,0,0)
size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
coor_list = [] #p/guardar las coord.

#-----------------------------------------------dibujo 60 círculos 
for i in range(60):
		x = random.randint(0, 800)
		y = random.randint(0, 500)
		coor_list.append([x,y])

#-------------------------------------------------p/que la screen pueda cerrarse
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


#------------------------------------------------------background
	screen.fill(WHITE)

	for coord in coor_list:
		x = coord[0]
		y = coord[1]


		pygame.draw.circle(screen, RED, coord, 2)
#------------------------------------------------------------------animación p/ q los círculos bajen
		coord[1] += 1

#-----------------------------------------------------para q se sigan dibujando los círculos q' van bajando
		if coord[1] > 500:
			coord[1] = 0



#----------------------------------------------------actualizo Pygame y configuro el reloj
	pygame.display.flip()
	clock.tick(30)