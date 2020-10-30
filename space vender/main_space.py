import pygame
import math
import random


#initlizing the game
pygame.init()
#cordinates
lose = 0
playerX = 300
playerY = 600
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemyimg = []
player_change = 0
bulletY = 600
bulletX = 0
bulletY_change = 5
bullet_state = "ready"
flag = []
score = 0
running = True
num_of_enemy = 6
textX= 10
textY= 10

#enemy appering code
for i in range(num_of_enemy):
    enemyimg.append(pygame.image.load("enemy3.png"))
    enemyX.append(random.randint(0, 700))
    enemyY.append(random.randint(0, 300))
    enemyX_change.append(1)
    enemyY_change.append(50)
    flag.append(0)
#images load
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Scape INvander game")
playerimage = pygame.image.load("player3.png")

icon = pygame.image.load("icon.png")
background = pygame.image.load("background1.jpg")
bullet = pygame.image.load("bullet1.png")
line = pygame.image.load("line1.png")
pygame.display.set_icon(icon)
#font
font = pygame.font.Font('sectar.otf' , 32)
#define player movement
def player(x,y):
    screen.blit( playerimage, (x,y))

#define shooting function
def shoot(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x,y))

#defin collision function to check bullet touch enemy of not
def iscollision(EX,EY,BX,BY):
    distance = math.sqrt(math.pow(EX-BX,2)+math.pow(EY-BY,2))

    if distance < 20:
        return True
    else :
        return False
#def score font
def show_score(x,y):
    score_value = font.render("score :" + str(score) , True , (255,225,225) )
    screen.blit(score_value,(x,y))
def game_over(x,y):
    over = font.render("game over " , True , (255,225,225) )
    screen.blit(over ,(x,y))
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False


        if event.type == pygame.KEYDOWN :

         # SHOOTING CODE
             if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX + 10
                    shoot(bulletX,bulletY)


        # player movement
             if event.key == pygame.K_LEFT:
                 player_change = -1
             if event.key == pygame.K_RIGHT:
                player_change = 1
        if event.type == pygame.KEYUP :

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0


    playerX += player_change

    if playerX < 0:
        playerX=0
    if playerX >= 640:
        playerX = 640
#ENEMY MOVEMENT
    for i in range(num_of_enemy):
        if flag[i] == 0:
            enemyX[i] += enemyX_change[i]
            if enemyX[i] == 700:
                enemyY[i] += enemyY_change[i]
                flag[i] = 1
        if flag[i] == 1:
            enemyX[i] -= enemyX_change[i]
            if enemyX[i]== 0:
               enemyY[i] += enemyY_change[i]
               flag[i] = 0

#IMAGE PRINTING
    screen.blit(background ,(0,0))
    player(playerX, playerY)
    # shooting image
    if bullet_state is "fire":
        shoot(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY < 0 :
            bulletY = 600
            bullet_state = "ready"
# collision
    for i in range(num_of_enemy):
        collision = iscollision(enemyX[i], enemyY[i], playerX, bulletY)
        if collision == True:
            score += 1
            print(score)

            enemyX[i] = -2000
            enemyY[i] = -3000
        if enemyY[i] >= 530:
            game_over(200,200)
            lose=1
            break
    if lose == 1:
        break

    if score == 6:
        print ("player won the game")
        break
    for i in range(num_of_enemy):
        screen.blit(enemyimg[i], (enemyX[i],enemyY[i]))
    show_score(textX,textY)
    screen.blit(line,(0,600))
    pygame.display.update()