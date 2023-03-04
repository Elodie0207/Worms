import pygame
import math

class Grenade(pygame.sprite.Sprite):
    def __init__(self, pos, angle, power):
        super().__init__()
        self.image = pygame.image.load("Image/grenade.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)
        self.gravity = pygame.Vector2(0, 0.98)
        self.angle = angle
        self.power = power
        self.timer = 120

        self.flag = False
        self.charging = False
        self.thrown = False
        self.usable = True

    def update(self):
        self.vel += self.acc + self.gravity
        self.pos += self.vel
        self.rect.center = self.pos
        self.timer -= 1
        if self.timer == 0:
            self.explode()

    def place_at_player(self, player_pos):
        self.pos = pygame.Vector2(player_pos)
        self.rect.center = self.pos

    def check_collision(self, objects):
        collisions = pygame.sprite.spritecollide(self, objects, False)
        if collisions:
            self.explode()

    def explode(self):
        explosion_radius = 50
        '''for obj in objects:
            distance = self.pos.distance_to(obj.pos)
            if distance < explosion_radius:
                obj.health -= (explosion_radius - distance) * 2'''
        print("boom")
        self.thrown = False
        self.usable = True
        self.kill()

    def render(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, rotated_rect)

    def throw(self, is_facing_left):
        angle_radians = math.radians(self.angle)
        direction = -1 if is_facing_left else 1
        self.vel.x = math.cos(angle_radians) * self.power * direction
        self.vel.y = -math.sin(angle_radians) * self.power
        self.acc = pygame.Vector2(0, 0.5)

    def draw_trajectory(self, screen, is_facing_left):
        angle_radians = math.radians(self.angle)
        direction = -1 if is_facing_left else 1
        vel_x = math.cos(angle_radians) * self.power
        vel_y = -math.sin(angle_radians) * self.power
        start_pos = pygame.Vector2(self.pos)
        points = [start_pos]
        for i in range(1, 100):
            x = start_pos.x + vel_x * i * 0.1 * direction
            y = start_pos.y + vel_y * i * 0.1 + 0.5 * self.gravity.y * (i * 0.1) ** 2
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
