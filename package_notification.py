import sys, pygame, time
import math
pygame.init()



import csv
with open('data.csv', 'r') as f:
    readdata = csv.reader(f, delimiter=',')
    
    twelvedigit = []
    threedigit = []
    interval = []
    color = []
    ycord = []
    for row in readdata:
        twelvedigit_v = row[0]
        threedigit_v = row[1]
        interval_v = row[2]
        color_v = row[3]
        ycord_v = row[4]

        twelvedigit.append(twelvedigit_v)
        threedigit.append(threedigit_v)
        interval.append(interval_v)
        color.append(color_v)
        ycord.append(ycord_v)


screen = pygame.display.set_mode([2000, 1000])
black = (0,0,0)
screen.fill(black)

player = pygame.image.load('yellow_tri.png').convert_alpha()
player2 = pygame.image.load('blue_tri.png').convert_alpha()
player3 = pygame.image.load('green_triangle.png').convert_alpha()
player4 = pygame.image.load('red_tri.png').convert_alpha()
player5 = pygame.image.load('yellow_rect.png').convert_alpha()
player6 = pygame.image.load('blue_rect.png').convert_alpha()
player7 = pygame.image.load('red_rect.png').convert_alpha()
background = pygame.image.load('black_rect.png')

player_r = dict()
x_all = dict()
appear = dict()

for i in range(0,11,1):
    if float(color[i]) == 1:
        player_r[i] = pygame.transform.rotate(player, 0)
    if float(color[i]) == 2:
        player_r[i] = pygame.transform.rotate(player2, 0)
    if float(color[i]) == 3:
        player_r[i] = pygame.transform.rotate(player3, 0)
    if float(color[i]) == 4:
        player_r[i] = pygame.transform.rotate(player4, 0)
    if float(color[i]) == 5:
        player_r[i] = pygame.transform.rotate(player5, 0)
    if float(color[i]) == 6:
        player_r[i] = pygame.transform.rotate(player6, 0)
    if float(color[i]) == 7:
        player_r[i] = pygame.transform.rotate(player7, 0)
    x_all[i] = 100*float(interval[i])
    appear[i] = 0 - x_all[i]



running = 1
FPS = 240
clock = pygame.time.Clock()

x = 0
screen.fill((black))


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    while x < 10000:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    x = 100001
        dt = clock.tick(FPS)
        x += 3
        screen.fill((black))
        for i in range (0,11,1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    x = 10001
            if appear[i] > 0:
                screen.blit(player_r[i],(x - float(x_all[i]), float(ycord[i])))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        x = 10001
            appear[i] = x - float(x_all[i])
        pygame.display.update()

pygame.display.quit()
pygame.quit()


        
    

    
