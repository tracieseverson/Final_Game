import pygame
import sys
from ship_1 import Ship1
from test_obstacle import Ship2
import random
from obstacle_1 import Obstacle1

pygame.init()
clock = pygame.time.Clock()

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
position_x = random.randint(0,600)

#obstacle
clock = pygame.time.Clock()
speed = 1
obs_list = []

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
    screen.blit(obstacle.image,(position_x,position_y))
    y_position = 0
    x_position= random.randint(0,600)
    speed = 1
    y_position += speed
    #can you make these obstacles sprites like in our alien invasion game?
    obs = Obstacle1(2,[x_position, y_position])
    obs_list.append(obs)
    for course in obs_list:
        course.draw(screen)
        course.drop(speed)
    collision = pygame.sprite.collide_rect(player1, obs)
    if collision:
        player1.health -= 1
    clock.tick(60)
    pygame.display.flip()
