import pygame
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Object(pygame.sprite.Sprite):
    def __init__(self, wX, wY):
        super().__init__()
        self.worldX=wX
        self.worldY=wY
        self.set_screen_pos(self.worldX,self.worldY)
        self.image = pygame.image.load('assets/sprites/object/object.png').convert_alpha()
        self.imgSize = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.imgSize[0]*3),int(self.imgSize[1]*3)))
        self.rect = self.image.get_rect(center = (self.worldX*6,self.worldY*6))

        

    def set_world_pos(self,wX,wY):
        self.worldX=wX
        self.worldY=wY

    def set_screen_pos(self,xOffset,yOffset):
        self.screenX=(self.worldX+xOffset)*6
        self.screenY=(self.worldY+yOffset)*6