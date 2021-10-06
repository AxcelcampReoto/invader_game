import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,600))
screen.fill((0,0,0))
pygame.display.set_caption("インベーダー？ゲーム？")

player = pygame.image.load("player.png")
playerX = 100
playerY = 200
running = True

while running:
    screen.fill((0,0,0))
    screen.blit(player, (playerX, playerY))

    押されたキーを調べる
    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_LEFT]:
        playerX -= 0.5
    if key_pressed[K_RIGHT]:
        playerX += 0.5
    if key_pressed[K_UP]:
        playerY -= 0.5
    if key_pressed[K_DOWN]:
        playerY += 0.5

    for event in pygame.event.get():
        if event.type == QUIT:
            running =False
        # if event.type == KEYDOWN:
        #     if event.key == K_RIGHT:
        #         playerX += 50
        #         screen.fill((255,0,0))
        #     if event.key == K_LEFT:
        #         playerX -= 50
        #         screen.fill((0,255,0))
        #     if event.key == K_UP:
        #         playerY -= 50
        #
        #         screen.fill((0,0,255,))
        #     if event.key == K_DOWN:
        #         playerY += 50
        #         screen.fill((255,255 , 255,))



    pygame.display.update()





