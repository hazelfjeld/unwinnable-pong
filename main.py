import pygame
import random
pygame.init()
ball_list=[-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()
#COLORS
BLACK=(0,0,0)
WHITE=(255,255,255)

#Ball
ball=pygame.Rect(50,50,20,20)
ball_speed=5
ball_speed_y=5
#Platforms
player_wall = pygame.Rect(0,0,10,150)
opponent_wall = pygame.Rect(590,0,10,40)
running=True
while running:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            running=False
    #Player movement
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_wall.y >=10:
        player_wall.y-=10
    if keys[pygame.K_DOWN] and player_wall.y <= 450:
        player_wall.y+=10
    #Opponent movement
    opponent_wall.y=ball.y


    #ball physics
    if ball.colliderect(player_wall):
        ball_speed_y=random.choice(ball_list)
        ball_speed = 9-abs(ball_speed_y)
        
    if ball.colliderect(opponent_wall):
        ball_speed_y=random.choice(ball_list)
        ball_speed = -9+abs(ball_speed_y)
    
    if ball.x<=0:
        ball.x=player_wall.x
        ball.y=player_wall.y+100
    
    if ball.y<=0:
        ball_speed_y= abs(ball_speed_y)
    if ball.y>=600:
        ball_speed_y= -1*abs(ball_speed_y)
    ball.x+=ball_speed
    ball.y+=ball_speed_y
    #Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen,BLACK,player_wall)
    pygame.draw.rect(screen,BLACK,opponent_wall)
    pygame.draw.rect(screen,BLACK,ball)
    pygame.display.update()
    clock.tick(60)
