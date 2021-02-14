import pygame
import time
import sys

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)



screen = pygame.init()



pygame.display.set_caption('snake game')
game_window = pygame.display.set_mode((700,500))

game_window.fill(red)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()


