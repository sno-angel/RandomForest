import pygame
from sys import exit
import os
import Player
import Objects
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

scale = 6
windowWidth = scale*160
windowHeight = scale*90

maxFPS = 30

gameState = 1

font = pygame.font.Font('assets/pixeldroidConsoleRegular.ttf', 50)

screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Random Forest')
#pygame.display.set_icon('') TODO: this
clock = pygame.time.Clock()

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player.PlayerObj())

world_group = pygame.sprite.Group()
world_group.add(Objects.Object(50,50))

bg_surf = pygame.Surface((windowWidth,windowHeight))
bg_surf.fill((26,67,20))

gameRunning = True #Window running
gameActive = True #Gameplay active

while(gameRunning):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            gameRunning = False


    if(gameActive):

        screen.blit(bg_surf, (0,0))

        player.update()
        player.draw(screen)

        playerPosX=player.getPosX()
        playerPosY=player.getPosY()
        
        for obj in world_group:
            obj.set_screen_pos(playerPosX,playerPosY)
        world_group.draw(screen)


        

    pygame.display.update()
    clock.tick(maxFPS) #TODO - Go back and seperate frame rendering from game processing

            
pygame.quit()