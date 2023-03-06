import pygame
import math

class Roquette(pygame.sprite.Sprite):
    def __init__(self, pos, angle, power):
        super().__init__()
        self.image = pygame.image.load("Image/missile.png").convert_alpha()
        self.roquette=pygame.image.load("Image/Roquette.png").convert_alpha()
        self.place= self.roquette.get_rect()
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)
        self.gravity = pygame.Vector2(0, 0.98)
        self.wind = pygame.Vector2(0.2, 0)
        self.angle = angle
        self.power = power
        self.timer = 120

        self.flag = False
        self.charging = False
        self.thrown = False
        self.usable = True
    
    
    
    def drawRoquette(self,screen):
        imageRotate = pygame.transform.rotate(self.roquette, self.angle)
        rectRotate = imageRotate.get_rect(center=self.place.center)
        screen.blit(imageRotate, rectRotate)
    def update(self):
        self.vel += self.acc + self.gravity + self.wind
        self.pos += self.vel
        self.rect.center = self.pos
        self.timer -= 1
        if self.timer == 0:
            self.exploser()

    def placement(self, player_pos):
        self.pos = pygame.Vector2(player_pos)
        self.rect.center = self.pos
    def lanceur(self, player_pos):
        self.pos = pygame.Vector2(player_pos)
        self.place.center = self.pos
    def collision(self, objects):
        collisions = pygame.sprite.spritecollide(self, objects, False)
        if collisions:
            self.exploser()

    def exploser(self):
        explosion_radius = 50
        '''for obj in objects:
            distance = self.pos.distance_to(obj.pos)
            if distance < explosion_radius:
                obj.health -= (explosion_radius - distance) * 2'''
        print("boom")
        self.thrown = False
        self.usable = True


    def draw(self, screen):
        imageRotate = pygame.transform.rotate(self.image, self.angle)
        rectRotate = imageRotate.get_rect(center=self.rect.center)
        screen.blit(imageRotate, rectRotate)

    def lancer(self, is_facing_left):
        angle_radians = math.radians(self.angle)
        if is_facing_left:
            direction = -1
        else:
           direction = 1
        #equation
        self.vel.x = math.cos(angle_radians) * self.power * direction
        self.vel.y = -math.sin(angle_radians) * self.power
        self.acc = pygame.Vector2(0, 0.5)

    def trajectoire(self, screen, is_facing_left):
        angle_radians = math.radians(self.angle)
        if is_facing_left:
            direction = -1
        else:
            direction = 1
        #equation
        vel_x = math.cos(angle_radians) * self.power
        vel_y = -math.sin(angle_radians) * self.power
        v0 = pygame.Vector2(self.pos)
        points = [v0]
        #mise en place de l'equation de la trajectoire
        for i in range(1, 100):
            x = v0.x + vel_x * i * 0.1 * direction
            y = v0.y + vel_y * i * 0.1 + 0.5 * self.gravity.y * (i * 0.1) ** 2
            if y > screen.get_height():
                break
            points.append(pygame.Vector2(x, y))
        pygame.draw.lines(screen, 255, False, points, 2)

    def adjust_angle(self, direction):
        if direction == "up":
            self.angle += 5
        elif direction == "down":
            self.angle -= 5
        if self.angle > 90:
            self.angle = 90
        elif self.angle < 0:
            self.angle = 0
