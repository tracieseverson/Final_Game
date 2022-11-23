import pygame
import sys

pygame.init()

background_tile = pygame.image.load("images/water_tile.png")
water_rect = background_tile.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((10*tile_size,10*tile_size))
screen.fill((0,0,0))
screen_rect = screen.get_rect()
rows = screen_rect.height // tile_size
cols = screen_rect.width // tile_size
#drwaing my ocean onthe screen
for x in range(int(rows)):
    for y in range(int(cols)):
        screen.blit(background_tile, (x*water_rect.height, y*water_rect.width))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()