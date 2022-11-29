import pygame

pygame.init()
class Obstacle1():
    def __init__(self, size, position, fall = False):
        self.size = size
        self.position = position
        self.fall = fall

    def drop(self, speed):
        self.position[1] += speed

    def draw(self, surface):
        pygame.draw.circle(surface,(0,0,0), self.position, self.size)
done = False
clock = pygame.time.Clock()
