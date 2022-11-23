import pygame

class Ship1:
    def __init__(self):
        self.image = pygame.image.load("images/player_1.png")

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.moving_left = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.moving_left = True

