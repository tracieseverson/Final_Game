import pygame

class Ship2:
    def __init__(self):
        self.image = pygame.image.load("images/player_2.png")
        self.rect = self.image.get_rect()

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

    def draw(self, surface):
        surface.blit(self.image, self.rect)

