import pygame #acceder al comando de pygame

pygame.init()

ANCHO  = 800
ALTO = 600
color_rojo=(255,0,0)
color_negro=(0,0,0)
color_azul = (0,255,0)
color_blanco = (130,130,130)
ancho_juga = 15
alto_juga = 90

consola = pygame.display.set_mode((ANCHO,ALTO)) #consola que proyecta el juego
reloj = pygame.time.Clock()

juga1_x = 50
juga1_y = 300 - (alto_juga/2)
juga1_vel = 0

juga2_x = 750 - ancho_juga
juga2_y = 300 - (alto_juga/2)
juga2_vel = 0

pel_x = 400
pel_y = 300
pel_x_vel = 3
pel_y_vel = 3

game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		if event.type == pygame.KEYDOWN:
			# Jugador 1
			if event.key == pygame.K_w:
				juga1_vel = -3
			if event.key == pygame.K_s:
				juga1_vel = 3
			# Jugador 2
			if event.key == pygame.K_UP:
				juga2_vel = -3
			if event.key == pygame.K_DOWN:
				juga2_vel= 3

		if event.type == pygame.KEYUP:
			# Jugador 1
			if event.key == pygame.K_w:
				juga1_vel = 0
			if event.key == pygame.K_s:
				juga1_vel = 0
			# Jugador 2
			if event.key == pygame.K_UP:
				juga2_vel = 0
			if event.key == pygame.K_DOWN:
				juga2_vel = 0

	if pel_y > 590 or pel_y < 10:
		pel_y_vel *= -1
	if pel_x > 800:
		pel_x = 400
		pel_y = 300
		# Si sale de la pantalla, invierte direccion
		pel_x_vel *= -1
		pel_y_vel *= -1

	# Revisa si la pelota sale del lado izquierdo
	if pel_x < 0:
		pel_x = 400
		pel_y = 300
		# Si sale de la pantalla, invierte direccion
		pel_x_vel *= -1
		pel_y_vel *= -1

	juga1_y += juga1_vel
	juga2_y += juga2_vel
    # Movimiento pelota
	pel_x += pel_x_vel
	pel_y += pel_y_vel

	consola.fill(color_negro)

	juga1 = pygame.draw.rect(consola, color_azul, (juga1_x,juga1_y,ancho_juga, alto_juga )) #dibujo paleta izquierda
	juga2 = pygame.draw.rect(consola, color_azul, (juga2_x,juga1_y,ancho_juga, alto_juga )) #dibujo paleta izquierda
	pel = pygame.draw.circle(consola, color_rojo, (pel_x, pel_y), 10)

	if pel.colliderect(juga1) or pel.colliderect(juga2):
		pel_x_vel *= -1

	pygame.display.flip()
	reloj.tick(60)

pygame.quit()