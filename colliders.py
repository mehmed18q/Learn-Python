import pygame
pygame.init()


window = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Basic Game")
walkRight = [pygame.image.load('sprites/R1.png'), 
             pygame.image.load('sprites/R2.png'), 
             pygame.image.load('sprites/R3.png'), 
             pygame.image.load('sprites/R4.png'), 
             pygame.image.load('sprites/R5.png'), 
             pygame.image.load('sprites/R6.png'), 
             pygame.image.load('sprites/R7.png'), 
             pygame.image.load('sprites/R8.png'), 
             pygame.image.load('sprites/R9.png')]

walkLeft = [pygame.image.load('sprites/L1.png'), 
            pygame.image.load('sprites/L2.png'), 
            pygame.image.load('sprites/L3.png'), 
            pygame.image.load('sprites/L4.png'), 
            pygame.image.load('sprites/L5.png'), 
            pygame.image.load('sprites/L6.png'), 
            pygame.image.load('sprites/L7.png'), 
            pygame.image.load('sprites/L8.png'), 
            pygame.image.load('sprites/L9.png')]
bg = pygame.image.load('sprites/bg.jpg')
char = pygame.image.load('sprites/standing.png')
clock = pygame.time.Clock()
screenWidth = 600

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 7
        self.isJumping = False
        self.jumpCount = 10 
        self.left = False
        self.right = False
        self.walkC = 0
        self.isStanding = True
        self.collider_player = (self.x + 20, self.y, 28, 60)

    def draw(self, window):
        if self.walkC + 1 >=27: 
            self.walkC = 0
        
        if not(self.isStanding):
            if self.left: 
                window.blit(walkLeft[self.walkC // 3], (self.x,self.y))
                self.walkC += 1
            elif self.right: 
                window.blit(walkRight[self.walkC // 3], (self.x,self.y))
                self.walkC += 1
        else: 
            if self.right: 
                window.blit(walkRight[0], (self.x, self.y))
            else:
                window.blit(walkLeft[0], (self.x, self.y))
        self.collider_player = (self.x + 20, self.y, 28, 60)
        pygame.draw.rect(window, (255, 0, 0), self.collider_player, 2)
class enemy(object):
    walkRight = [pygame.image.load('sprites/R1E.png'), 
                pygame.image.load('sprites/R2E.png'), 
                pygame.image.load('sprites/R3E.png'), 
                pygame.image.load('sprites/R4E.png'), 
                pygame.image.load('sprites/R5E.png'), 
                pygame.image.load('sprites/R6E.png'), 
                pygame.image.load('sprites/R7E.png'), 
                pygame.image.load('sprites/R8E.png'), 
                pygame.image.load('sprites/R9E.png'), 
                pygame.image.load('sprites/R10E.png'), 
                pygame.image.load('sprites/R11E.png')]

    walkLeft = [pygame.image.load('sprites/L1E.png'), 
                pygame.image.load('sprites/L2E.png'), 
                pygame.image.load('sprites/L3E.png'), 
                pygame.image.load('sprites/L4E.png'), 
                pygame.image.load('sprites/L5E.png'), 
                pygame.image.load('sprites/L6E.png'), 
                pygame.image.load('sprites/L7E.png'), 
                pygame.image.load('sprites/L8E.png'), 
                pygame.image.load('sprites/L9E.png'),
                pygame.image.load('sprites/L10E.png'), 
                pygame.image.load('sprites/L11E.png')]
    def __init__(self, x, y, width, height, endPoint):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.endpoint = endPoint
        self.walkC = 0
        self.speed  = 4
        self.mainPath = [self.x, self.endpoint]
        self.collier_enemy = (self.x + 20, self.y, 28, 60)
    def draw(self, window):
        self.move_enemy()

        if self.walkC + 1 >=33:
            self.walkC = 0
        if self.speed > 0: 
            window.blit(self.walkRight[self.walkC // 3], (self.x, self.y))
            self.walkC += 1
        else: 
            window.blit(self.walkLeft[self.walkC // 3], (self.x, self.y))
            self.walkC += 1
        self.collier_enemy = (self.x + 20, self.y, 28, 60)
        pygame.draw.rect(window, (255, 0, 0), self.collier_enemy, 2)
    def move_enemy(self):
        if self.speed > 0: 
            if self.x + self.speed < self.mainPath[1]:
                self.x += self.speed
            else: 
                self.speed = self.speed * -1
                self.walkC = 0
        else: 
            if self.x - self.speed > self.mainPath[0]:
                self.x += self.speed
            else: 
                self.speed = self.speed * -1
                self.walkC = 0
    def get_hit(self):
        print("Hit")
class P_Bullet(object):
    def __init__(self, x, y, r, color, side):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.side = side
        self.velocity = 8*side
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x,self.y), self.r)



def redrawGameWindow():
    window.blit(bg, (0,0))
    main_character.draw(window)
    enemy_character.draw(window)
    for bullet in bullet_list: 
        bullet.draw(window)
    pygame.display.update()

main_character = player(200, 400, 64, 64)
enemy_character = enemy(200, 400, 64, 64, 430)
runG = True
bullet_count = 0
bullet_list = []
while runG: 
    clock.tick(25)
    if bullet_count > 0: 
        bullet_count += 1
    if bullet_count > 3: 
        bullet_count = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            runG = False
    for bullet in bullet_list: 
        if bullet.y -  bullet.r < enemy_character.collier_enemy[1] + enemy_character.collier_enemy[3] and bullet.y + bullet.r > enemy_character.collier_enemy[1]:
            if bullet.x + bullet.r > enemy_character.collier_enemy[0] and bullet.x - bullet.r < enemy_character.collier_enemy[0] + enemy_character.collier_enemy[2]:
                bullet_list.pop(bullet_list.index(bullet))
                enemy_character.get_hit()

        if bullet.x < 500 and bullet.x > 0: 
            bullet.x += bullet.velocity
        else: 
            bullet_list.pop(bullet_list.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if main_character.left: 
            side = -1
        else: 
            side = 1
        if len(bullet_list) < 6 and bullet_count == 0:
            bullet_list.append(P_Bullet(round(main_character.x + main_character.width // 2), round(main_character.y + main_character.height // 2), 6, (2,0,0), side))
        bullet_count = 1

    if keys[pygame.K_d] and main_character.x < screenWidth - main_character.width - main_character.velocity:
        main_character.x += main_character.velocity
        main_character.right = True
        main_character.left = False
        main_character.isStanding = False
    elif keys[pygame.K_a] and main_character.x > main_character.velocity:
        main_character.x -= main_character.velocity
        main_character.right = False  
        main_character.left = True
        main_character.isStanding = False
    else: 
        main_character.isStanding = True
        main_character.walkC = 0
    if not(main_character.isJumping):
        if keys[pygame.K_w]:
            main_character.isJumping = True
            main_character.left = False
            main_character.right = False
            main_character.walkC = 0
    else: 
        if main_character.jumpCount >= -10: 
            neg = 1
            if main_character.jumpCount < 0: 
                neg = -1
            main_character.y -= (main_character.jumpCount**2) * 0.5 * neg
            main_character.jumpCount -=1
        else: 
            main_character.isJumping = False
            main_character.jumpCount = 10  
    redrawGameWindow()

pygame.quit()