import pygame
import time
import sys

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

clock=pygame.time.Clock()


screen = pygame.init()



pygame.display.set_caption('snake game')
game_window = pygame.display.set_mode((700,500))

game_window.fill(red)
pygame.display.update()

snake_size=10
snake_list=[]

def snake(snake_size,snake_list):
	for i in snake_list:
		pygame.draw.rect(game_window,blue,[x[0],x[1],snake_size,snake_size])





def game_loop():



	x=350
	y=200
	y_change=0
	x_change=0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()


			if event.type==pygame.KEYDOWN:

				if event.key==pygame.K_LEFT:
					x_change=-snake_size
					y_change=0


				elif event.key==pygame.K_RIGHT:
					x_change=snake_size
					y_change=0


				elif event.key==pygame.K_UP:
					y_change=-snake_size
					x_change=0


				elif event.key==pygame.K_DOWN:
					y_change=snake_size
					x_change=0




			#pygame.draw.rect(game_window,blue,[x,y,snake_size,snake_size])
			#pygame.display.update()

		x=x+x_change
		y=y+y_change

		pygame.display.update()
		pygame.draw.rect(game_window,blue,[x,y,snake_size,snake_size])

		'''if x_change!=0:
			x=x+snake_size
			pygame.draw.rect(game_window,blue,[x,y,snake_size,snake_size])

		elif y_change!=0:
			y=y+snake_size
			pygame.draw.rect(game_window,blue,[x,y,snake_size,snake_size])
		'''

		pygame.display.update()
		clock.tick(25)
		game_window.fill(black)


game_loop()