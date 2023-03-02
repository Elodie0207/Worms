import pygame
class Grenade:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.color = (255, 255, 255)
        self.radius = 5
        self.timer = 0
        self.explosion_radius = 50
        self.explosion_color = (255, 255, 255)

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            self.y += self.speed

    def draw(self, surface):
        if self.timer > 0:
            pygame.draw.circle(surface, self.explosion_color, (self.x, self.y), self.explosion_radius)
        else:
            pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def explode(self):
        self.timer = 30
