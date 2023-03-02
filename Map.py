import pygame

White=(255,255,255)
class Map(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image=pygame.Surface((width,height))
        self.image=pygame.image.load("Image/grenade.png")
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


    def collisions(self):
        hits=pygame.sprite.spritecolle
