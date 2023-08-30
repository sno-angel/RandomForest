import pygame
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class PlayerObj(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        rightIdleImage = pygame.image.load('assets/sprites/player/right_idle.png').convert_alpha()
        self.image = rightIdleImage
        self.imgSize = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.imgSize[0]*3),int(self.imgSize[1]*3)))
        self.rect = self.image.get_rect(center = (6*80,6*45))

        self.wPosX = 0
        self.wPosY = 0

        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False

    def getPosX(self):
        return self.wPosX
    def getPosY(self):
        return self.wPosY

    def player_input(self):
        keys = pygame.key.get_pressed()
        self.movingUp = keys[pygame.K_UP]
        self.movingDown = keys[pygame.K_DOWN]
        self.movingLeft = keys[pygame.K_LEFT]
        self.movingRight = keys[pygame.K_RIGHT]

        if(self.movingUp):
            self.wPosY-=1
        if(self.movingDown):
            self.wPosY+=1
        if(self.movingLeft):
            self.wPosX-=1
        if(self.movingRight):
            self.wPosX+=1

    #def anim_state():

    def update(self):
        self.player_input()
        #self.anim_state()