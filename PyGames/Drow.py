import pygame, time, sys

# inithials of pygame
pygame.init()
print('Status:\nStart First Game')
# main root
win = pygame.display.set_mode((800, 600))

# set title of root
pygame.display.set_caption("First Game")

time.sleep(2)

# color = (R, G, B)
red =(255, 0, 0)
green =(0, 255, 0)
blue =(0, 0, 255)
white =(255, 255, 255)
black =(0, 0, 0)
yellow = (255, 255, 0)

# fill main root
win.fill(white)
print('Change Color to White')

time.sleep(2)

print('Plase Waite! Drowing...')
time.sleep(2)
# drow
# mostatil      koja, rang, mogheiat,   andaze ,   zekhamat
pygame.draw.rect(win, red, ((400, 300), (100, 50)), 15)
# dayere          koja, rang, mogheiat, ghotr,  zekhamat
pygame.draw.circle(win, green, (300, 250), 20, 0)
# beizi             koja, rang, mogheiat, ghotr,  zekhamat
pygame.draw.ellipse(win, blue, (500, 450, 100, 50), 0)
# motevazi alazla    koja, rang,   ras1       ras2,      ras3,       ras4,    zekhamat
pygame.draw.polygon(win, yellow, ((100, 50), (200, 50), (175, 100), (75, 100)), 0)
# kaman        koja, rang,  mogheiat ,  shoa,  start, end , zekhamat # 1 radian = 57^
pygame.draw.arc(win, green, (600, 100, 50, 50), 1, 3, 1)
# khat          koja, rang, start,       end , zekhamat
pygame.draw.line(win, red, (100, 100), (150, 200), 1)
# a khat          koja, rang,  start,     end , zekhamat
pygame.draw.aaline(win, red, (50, 100), (150, 150), 1)
pygame.draw.aaline(win, red, (100, 150), (200, 260), 1)
pygame.draw.aaline(win, red, (100, 160), (200, 270), 1)
# chand khati     koja, rang,baste?, start,     point1    ,  point2
pygame.draw.lines(win, blue, True, ((300, 300), (270, 310), (350, 350)))
print('Drow is Complet')

# main loop
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            print('End First Game')
            sys.exit()
    # update win
    pygame.display.update()
