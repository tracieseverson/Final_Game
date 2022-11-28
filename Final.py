import pygame
import sys
from ship_1 import Ship1
from ship_2 import Ship2

pygame.init()

background_tile = pygame.image.load("images/water_tile.png")
water_rect = background_tile.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((10*tile_size,10*tile_size))
screen.fill((0,0,0))
screen_rect = screen.get_rect()
rows = screen_rect.height // tile_size
cols = screen_rect.width // tile_size

#drawing my ocean onthe screen
def update():
    for x in range(int(rows)):
        for y in range(int(cols)):
            screen.blit(background_tile, (x*water_rect.height, y*water_rect.width))

#bring in player 1
player1 = Ship1()

pygame.display.flip()
#points for the first ship origin
x=50
y=520

#first obstacle
obstacle = Ship2()
position_y = 0


while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=3
    elif keys[pygame.K_RIGHT]:
        x+=3
    position_y += 1
    update()
    player1_rect = player1.rect
    #player1.draw(screen)
    screen.blit(player1.image, (x,y))
    screen.blit(obstacle.image,(0,position_y))
    pygame.display.flip()
