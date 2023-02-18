#hacerlo también con p5.JS
#ver el orden de las distintas partes del programita

import pygame, sys
pygame.init()


# ------------------------------------------------Definir colores
BLACK = (0,0,0)
WHITE= (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
size = (800, 500)
#--------------------------------------------------Crear ventana
screen = pygame.display.set_mode(size)

#-------------------------------------------------Para controlar FPS
clock = pygame.time.Clock()


#--------------------------------------------------defino variables (son las coord. del cuadrado, posición inicial)
cord_x = 400
cord_y = 200
#---------------------------------------------- defino Velocidad a la que se movera el cuadrado
speed_x = 3
speed_y = 3


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

#-----------------------------------------------------------------------LÓGICA
	if (cord_x > 720 or cord_x < 0):
		speed_x *= -1 #para que el valor se haga negativo y rebote
	if (cord_y > 420 or cord_y < 0):
		speed_y *= -1

#------------------------------------------------------------------------(animación)
	cord_x += speed_x
	cord_y += speed_y

#-----------------------------------------------------------------------background
	screen.fill(WHITE)
	

	#-----------------------------------------------------------------------Zona de dibujo

	pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80))




	#------------------------------------------------------------------------Zona de dibujo


	#-----------------------------------------------------------------------------Actualizar pantalla
	pygame.display.flip()
	clock.tick(60) #FPS