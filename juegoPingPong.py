#poner un límite a las paletas prque salen de la screen

import pygame
pygame.init()

#--------------------------------------------Colores
black = (0, 0, 0)
white = (255, 255, 255)
screen_size = (800, 600)
player_width = 15
player_height = 90

#----------------------------------------------------screen
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

#-------------------------------------------Coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0 #la velocidad es 0 pq acá si depende de si yo presiono o no una tecla.

#----------------------------------------------Coordenadas y velocidad del jugador 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

# ----------------------------------------------------Coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3  #se le asignan directm. valores pq su movimiento no depende de si se presiona una tecla o no
pelota_speed_y = 3

game_over = False #---variable q permite salir del bucle ppal.

#----------------------------------------------------------------------------------------------------BUCLE ppal-LÓGICA
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		if event.type == pygame.KEYDOWN:
			# -------------------------------Jugador 1
			if event.key == pygame.K_w: #tecla W mueve hacia arriba
				player1_y_speed = -3
			if event.key == pygame.K_s: #tecla S mueve hacia abajo
				player1_y_speed = 3
			# -------------------------------Jugador 2
			if event.key == pygame.K_UP: #tecla flecha hacia arriba
				player2_y_speed = -3
			if event.key == pygame.K_DOWN: #tecla flecha hacia abajo
				player2_y_speed = 3
#--------------------------------------------------------------------------cuando se suelta la tecla q no haga nada:

		if event.type == pygame.KEYUP:
			# -------------------------------Jugador 1
			if event.key == pygame.K_w:
				player1_y_speed = 0
			if event.key == pygame.K_s:
				player1_y_speed = 0
			# ---------------------------------Jugador 2
			if event.key == pygame.K_UP:
				player2_y_speed = 0
			if event.key == pygame.K_DOWN:
				player2_y_speed = 0



#-----------------------------------------------(2)Empiezo a hacer chequeo de pelota luego de darle movimiento
	if pelota_y > 590 or pelota_y < 10:
		pelota_speed_y *= -1    #p/q rebote

	#----------------------------------------------------(3)Revisa si la pelota sale del lado derecho
	if pelota_x > 800:
		pelota_x = 400
		pelota_y = 300

	#-------------------------------------------------------(4) Si sale de la pantalla, invierte direccion
		pelota_speed_x *= -1
		pelota_speed_y *= -1

	#---------------------------------------------------------(5) Revisa si la pelota sale del lado izquierdo
	if pelota_x < 0:
		pelota_x = 400
		pelota_y = 300
	#----------------------------------------------------------(6) Si sale de la pantalla, invierte direccion
		pelota_speed_x *= -1
		pelota_speed_y *= -1


	#---------------------------------------------- Modifica las coordenadas para dar mov. a los jugadores/ pelota
	player1_y_coor += player1_y_speed #movimiento de paletas
	player2_y_coor += player2_y_speed

	#-------------------------------------------------------(1) Movimiento pelota(1° hago esto luego chequeo q no se salga de la screen)
	pelota_x += pelota_speed_x
	pelota_y += pelota_speed_y


	screen.fill(black)

	#---------------------------------------------------------------------------Zona de dibujo

	jugador1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_width, player_height))
	jugador2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_width, player_height))
	pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)


	#---------------------------------------------------------------------------------------(7) Colisiones
	if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
		pelota_speed_x *= -1  #q cuando choque cambie de dirección


#--------------------------------------------------------------------------------------------------------------
	pygame.display.flip()
	clock.tick(60)
pygame.quit()