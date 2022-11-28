import pygame

class Ship1:
    def __init__(self):
        self.image = pygame.image.load("images/player_1.png")
        self.rect = self.image.get_rect()
        #movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on teh movement flag"""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x.
        self.rect.x = self.x
  
    def draw(self, surface):
        surface.blit(self.image, self.rect)