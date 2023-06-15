"""
Bu proje bir pin pon oyunu düşünülerek tasarlanmıştır. 1. oyuncu aşağı ve yukarı yön tuşlarını kullanırken
2. oyuncu 'w' ve 's' tuşlarını kullanabilir. Oyun, oyunculardan birinin 10 puan alması ile biter.
"""

import pygame


pygame.init()
gameWindow = pygame.display.set_mode((650,450)) # Pencere büyüklüğü

# Oyunda kullanılacak renklerin tanımlanması
black = (0,0,0)
white = (255,255,255)
cyan = (3,252,207)

ballx = 100
bally = 100
paddle1x = 50
paddle1y = 150
paddle2x = 590
paddle2y = 150
xvelocity = 10
yvelocity = 10

# Başlangıç puanları
p1score = 0
p2score = 0

font = pygame.font.Font("freesansbold.ttf", 32)

scorestr = str(p1score) + " : " + str(p2score)

text = font.render(scorestr, True, cyan, white)

textrect = text.get_rect()
textrect.center = (325,50)

# Top hareketinin tanımlanması
while True:
    pygame.event.clear()
    gameWindow.fill(black)
    gameWindow.blit(text, textrect)
    
    ball = pygame.Rect((ballx, bally, 10, 10))
    pygame.draw.circle(gameWindow, cyan, (ballx, bally), 5)
    paddle1 = pygame.Rect((paddle1x, paddle1y, 10, 150))
    
    paddle2 = pygame.Rect((paddle2x, paddle2y, 10, 150))
    pygame.draw.rect(gameWindow, white, paddle1)
    pygame.draw.rect(gameWindow, white, paddle2)
    ballx = ballx + xvelocity
    bally = bally + yvelocity
    if(bally <= 0 or bally > 430):
        yvelocity *= -1
        
    if(ballx <= 0):
        ballx = 325
        bally = 200
        xvelocity *= -1
        yvelocity *= -1
        p2score = p2score + 1
        if(p2score == 10):
            break
        
    if(ballx >= 630):
        ballx = 325
        bally = 200
        xvelocity *= -1
        yvelocity *= -1
        p1score = p1score + 1
        if(p1score == 10):
            break
        
    if(pygame.Rect.colliderect(ball, paddle1)):
        ballx = paddle1x + 20
        xvelocity *= -1
        
    if(pygame.Rect.colliderect(ball, paddle2)):
        ballx = paddle2x - 20
        xvelocity *= -1
        
    keys = pygame.key.get_pressed()
    
    if(keys[pygame.K_w] and paddle1y >= 0): # w tuşu
        paddle1y = paddle1y - 10
         
    if(keys[pygame.K_s] and paddle1y <= 300): # s tuşu
        paddle1y = paddle1y + 10
           
    if(keys[pygame.K_UP] and paddle2y >= 0): # yukarı yön tuşu
        paddle2y = paddle2y - 10
         
    if(keys[pygame.K_DOWN] and paddle2y <= 300): # aşağı yön tuşu
        paddle2y = paddle2y + 10
          
    
    scorestr = str(p1score) + " : " + str(p2score)
    text = font.render(scorestr, True, cyan, black)
    textrect = text.get_rect()
    textrect.center = (325,50)
    pygame.time.delay(40)
    pygame.display.update()
    
