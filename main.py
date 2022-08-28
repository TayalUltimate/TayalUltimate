import math

import pygame
import random
from pygame import mixer

# Initialize the game
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((1500, 800))

# Title and Icon
pygame.display.set_caption("Space Invaders - By TayalUltimate")
pygame.display.set_icon(pygame.image.load('images/icon.png'))

# Variables
running = True
playerIMAGE = pygame.image.load('images/spaceship.png')
playerX = 718
playerY = 650
playerXCHANGE = 0
playerYCHANGE = 0
backgroundnum = 1
angle = 0
laser = False
laserX = playerX
laserY = playerY
laserXCHANGE = 0
laserYCHANGE = 0
playerHP = 10000
font = pygame.font.Font('font.ttf', 48)
wavefont = pygame.font.Font('font.ttf', 256)
statfont = pygame.font.Font('freesansbold.ttf', 16)
hpcolor = (0, 255, 0)
borderDMG = 1
playerhealpower = 0.01
noheal = False
dedcolor = (255, 255, 255)
slider = pygame.image.load('images/laser/slider.png')
sliderval = 0
sliderchange = 1
borderDMGeffect = 0
lasercolor = (255, 255, 255)
laserIMG = pygame.image.load('images/laser/miss.png')
laserangle = angle
WEAKenemyIMG = []
WEAKenemyX = []
WEAKenemyY = []
WEAKenemyXCHANGE = []
WEAKenemyYCHANGE = []
WEAKenemyHP = []
WEAKenemyALIVE = []
STRONGenemyIMG = []
STRONGenemyX = []
STRONGenemyY = []
STRONGenemyXCHANGE = []
STRONGenemyYCHANGE = []
STRONGenemyHP = []
STRONGenemyALIVE = []
CRITICALenemyIMG = []
CRITICALenemyX = []
CRITICALenemyY = []
CRITICALenemyXCHANGE = []
CRITICALenemyYCHANGE = []
CRITICALenemyHP = []
CRITICALenemyALIVE = []
CREEPERenemyIMG = []
CREEPERenemyX = []
CREEPERenemyY = []
CREEPERenemyXCHANGE = []
CREEPERenemyYCHANGE = []
CREEPERenemyHP = []
CREEPERenemyALIVE = []
CREEPERenemyANGLE = []
CREEPERenemyIMGrotate = []
CREEPERenemyHPcolor = []
wave = 0
NEWwave = True
a = wave
playerDMG = 1
totalenemyHP = 1
maxenemyHP = 235
distance = 10000000000
newwaveeffect = 0
playerDistance = 10000000000
gameover = False
newwavefont = 0
blast = pygame.image.load('images/blast.png')
blastX = -100
blastY = -100
score = 0
maxplayerHP = 1000
creeperenemyhpcoloradd = 5
damagepowerupIMG = pygame.image.load('images/sword.png')
damagepowerupANGLE = 0
damagepowerup = False
damagepowerupX = -100
damagepowerupY = -100

if wave < 10:
    mixer.music.load('background.wav')
    mixer.music.play(-1)
elif wave >= 10 and wave < 20:
    mixer.music.load('background2.wav')
    mixer.music.play(-1)
else:
    mixer.music.load('background3.wav')
    mixer.music.play(-1)

# Game Loop
while running:

    if not gameover:
        # Variable Naming
        background = pygame.image.load(f'images/background/background ({backgroundnum}).gif')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pressed()[0]:
                if laser:
                    pass
                if not laser:
                    laser = True
                    lasersound = mixer.Sound('sounds/laser.wav')
                    lasersound.play()
                    if sliderval <= 300 or sliderval >= 700:
                        playerDMG = 1
                        lasercolor = (0, 255, 0)
                        laserIMG = pygame.image.load('images/laser/miss.png')
                    elif sliderval <= 450 or sliderval >= 550:
                        playerDMG = 2
                        lasercolor = (255, 255, 0)
                        laserIMG = pygame.image.load('images/laser/weak.png')
                    elif sliderval <= 495 or sliderval >= 505:
                        playerDMG = 5
                        lasercolor = (255, 0, 0)
                        laserIMG = pygame.image.load('images/laser/strong.png')
                    else:
                        playerDMG = 10
                        lasercolor = (255, 0, 255)
                        laserIMG = pygame.image.load('images/laser/critical.png')

                    if angle == 0:
                        laserXCHANGE = 0
                        laserYCHANGE = -20
                    if angle == 90:
                        laserXCHANGE = -20
                        laserYCHANGE = 0
                    if angle == 180:
                        laserXCHANGE = 0
                        laserYCHANGE = 20
                    if angle == 270:
                        laserXCHANGE = 20
                        laserYCHANGE = 0

                    laserangle = angle
                    laserY = playerY
                    laserX = playerX

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    playerYCHANGE = -5
                    angle = 0
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    playerYCHANGE = 5
                    angle = 180
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    playerXCHANGE = -5
                    angle = 90
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    playerXCHANGE = 5
                    angle = 270
                if event.key == pygame.K_SPACE:
                    if laser:
                        pass
                    if not laser:
                        laser = True
                        lasersound = mixer.Sound('sounds/laser.wav')
                        lasersound.play()
                        if sliderval <= 300 or sliderval >= 700:
                            playerDMG = 1
                            lasercolor = (0, 255, 0)
                            laserIMG = pygame.image.load('images/laser/miss.png')
                        elif sliderval <= 450 or sliderval >= 550:
                            playerDMG = 2
                            lasercolor = (255, 255, 0)
                            laserIMG = pygame.image.load('images/laser/weak.png')
                        elif sliderval <= 495 or sliderval >= 505:
                            playerDMG = 5
                            lasercolor = (255, 0, 0)
                            laserIMG = pygame.image.load('images/laser/strong.png')
                        else:
                            playerDMG = 10
                            lasercolor = (255, 0, 255)
                            laserIMG = pygame.image.load('images/laser/critical.png')

                        if angle == 0:
                            laserXCHANGE = 0
                            laserYCHANGE = -20
                        if angle == 90:
                            laserXCHANGE = -20
                            laserYCHANGE = 0
                        if angle == 180:
                            laserXCHANGE = 0
                            laserYCHANGE = 20
                        if angle == 270:
                            laserXCHANGE = 20
                            laserYCHANGE = 0

                        laserangle = angle
                        laserY = playerY
                        laserX = playerX

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    playerYCHANGE = 0
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    playerYCHANGE = 0
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    playerXCHANGE = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    playerXCHANGE = 0

        if playerX >= 1436:
            playerX = 1400
            playerHP = playerHP - borderDMG
            borderDMG += 0.5
            borderDMGeffect = 10
            while borderDMGeffect != 0:
                screen.fill((255, 255, 255))
                pygame.display.update()
                borderDMGeffect = borderDMGeffect - 1

        if playerY >= 736:
            playerY = 700
            playerHP = playerHP - borderDMG
            borderDMG += 0.5
            borderDMGeffect = 10
            while borderDMGeffect != 0:
                screen.fill((255, 255, 255))
                pygame.display.update()
                borderDMGeffect = borderDMGeffect - 1

        if playerX <= 0:
            playerX = 36
            playerHP = playerHP - borderDMG
            borderDMG += 0.5
            borderDMGeffect = 10
            while borderDMGeffect != 0:
                screen.fill((255, 255, 255))
                pygame.display.update()
                borderDMGeffect = borderDMGeffect - 1

        if playerY <= 0:
            playerY = 36
            playerHP = playerHP - borderDMG
            borderDMG += 0.5
            borderDMGeffect = 10
            while borderDMGeffect != 0:
                screen.fill((255, 255, 255))
                pygame.display.update()
                borderDMGeffect = borderDMGeffect - 1

        maxplayerHP = 0
        maxplayerHP = 1000 + ((wave - 1) * 10)

        if playerHP >= 1000:
            hpcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            playerhealpower = 0.005
            noheal = False
        if playerHP < 1000:
            hpcolor = (255, 0, 255)
            playerhealpower = 0.01
            noheal = False
        if playerHP <= 950:
            hpcolor = (0, 255, 0)
            playerhealpower = 0.02
            noheal = False
        if playerHP <= 550:
            hpcolor = (255, 255, 0)
            playerhealpower = 0.1
            noheal = False
        if playerHP <= 250:
            hpcolor = (255, 0, 0)
            playerhealpower = 0.2
            noheal = False
        if playerHP <= 75:
            hpcolor = (128, 64, 0)
            playerhealpower = 1
            noheal = False
        if playerHP <= 0:
            gameover = True
            hpcolor = (0, 0, 255)
            noheal = True
            playerhealpower = 0
            playerHP = 0
            dedcolor = (0, 0, 255)
            dedsound = mixer.Sound('sounds/explosion.wav')
            dedsound.play()
            dedsound = mixer.Sound('sounds/explosion.wav')
            dedsound.play()
            dedsound = mixer.Sound('sounds/explosion.wav')
            dedsound.play()
            mixer.music.load('gameover.wav')
            mixer.music.play(-1)

        if not noheal:
            playerHP += playerhealpower + (wave * 0.001)
            if sliderval == 500:
                playerHP += 10
        if playerHP > maxplayerHP:
            playerHP = maxplayerHP

        if borderDMG < 1:
            borderDMG = 1

        if sliderval <= 0:
            sliderchange = 2
        elif sliderval >= 1000:
            sliderchange = -2

        sliderval += sliderchange

        if totalenemyHP == 0 or NEWwave:
            score = score + wave * 100
            score = score + (score * wave * 0.05)
            newwaveeffect = 2500
            wave = wave + 1
            NEWwave = False
            WEAKenemyIMG = []
            WEAKenemyX = []
            WEAKenemyY = []
            WEAKenemyXCHANGE = []
            WEAKenemyYCHANGE = []
            WEAKenemyHP = []
            WEAKenemyALIVE = []
            STRONGenemyIMG = []
            STRONGenemyX = []
            STRONGenemyY = []
            STRONGenemyXCHANGE = []
            STRONGenemyYCHANGE = []
            STRONGenemyHP = []
            STRONGenemyALIVE = []
            CRITICALenemyIMG = []
            CRITICALenemyX = []
            CRITICALenemyY = []
            CRITICALenemyXCHANGE = []
            CRITICALenemyYCHANGE = []
            CRITICALenemyHP = []
            CRITICALenemyALIVE = []
            CREEPERenemyIMG = []
            CREEPERenemyX = []
            CREEPERenemyY = []
            CREEPERenemyXCHANGE = []
            CREEPERenemyYCHANGE = []
            CREEPERenemyHP = []
            CREEPERenemyALIVE = []
            CREEPERenemyANGLE = []
            CREEPERenemyIMGrotate = []
            CREEPERenemyHPcolor = []
            playerXCHANGE = 0
            playerYCHANGE = 0
            newwavefont = pygame.font.Font('font.ttf', 256)
            newwavetext = newwavefont.render("Wave " + str(wave), True, True)
            levelupsound = mixer.Sound('sounds/levelup.wav')
            levelupsound.play()
            while newwaveeffect != 0:
                screen.fill((0, 255, 0))
                screen.blit(newwavetext, (400, 250))
                screen.blit(font.render("Click to skip!", True, True), (607, 500))
                pygame.display.update()
                newwaveeffect = newwaveeffect - 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if pygame.mouse.get_pressed()[0]:
                        newwaveeffect = 0
            a = wave
            b = wave // 2
            c = wave // 5
            d = wave // 10
            while a != 0:
                WEAKenemyIMG.append(pygame.image.load('images/enemy/weak.png'))
                WEAKenemyX.append(random.randint(0, 1478))
                WEAKenemyY.append(random.randint(0, 100))
                WEAKenemyY.append(0)
                WEAKenemyXCHANGE.append(1)
                WEAKenemyYCHANGE.append(1)
                WEAKenemyHP.append(10)
                WEAKenemyALIVE.append(True)
                a = a - 1
            while b != 0:
                STRONGenemyIMG.append(pygame.image.load('images/enemy/strong.png'))
                STRONGenemyX.append(random.randint(0, 1478))
                STRONGenemyY.append(random.randint(0, 100))
                STRONGenemyY.append(0)
                STRONGenemyXCHANGE.append(2)
                STRONGenemyYCHANGE.append(2)
                STRONGenemyHP.append(25)
                STRONGenemyALIVE.append(True)
                b = b - 1
            while c != 0:
                CRITICALenemyIMG.append(pygame.image.load('images/enemy/critical.png'))
                CRITICALenemyX.append(random.randint(0, 1478))
                CRITICALenemyY.append(random.randint(0, 100))
                CRITICALenemyY.append(0)
                CRITICALenemyXCHANGE.append(3)
                CRITICALenemyYCHANGE.append(3)
                CRITICALenemyHP.append(50)
                CRITICALenemyALIVE.append(True)
                c = c - 1
            while d != 0:
                CREEPERenemyIMG.append(pygame.image.load('images/enemy/creeper.png'))
                CREEPERenemyX.append(random.randint(0, 1478))
                CREEPERenemyY.append(random.randint(0, 100))
                CREEPERenemyY.append(0)
                CREEPERenemyXCHANGE.append(0.5)
                CREEPERenemyYCHANGE.append(0.5)
                CREEPERenemyHP.append(150)
                CREEPERenemyALIVE.append(True)
                CREEPERenemyANGLE.append(0)
                CREEPERenemyIMGrotate.append(None)
                CREEPERenemyHPcolor.append(125)
                d = d - 1
            if wave == 1:
                mixer.music.load('background.wav')
                mixer.music.play(-1)
            if wave == 10:
                mixer.music.load('background2.wav')
                mixer.music.play(-1)
            if wave == 20:
                mixer.music.load('background3.wav')
                mixer.music.play(-1)

        maxenemyHP = ((wave * 10) + (wave // 2 * 25) + (wave // 5 * 50)) + (wave // 10 * 150)

        x = wave - 1
        while x != -1:
            if WEAKenemyALIVE[x]:
                WEAKenemyX[x] = WEAKenemyX[x] + WEAKenemyXCHANGE[x]
                WEAKenemyY[x] = WEAKenemyY[x] + WEAKenemyYCHANGE[x]
                if WEAKenemyX[x] <= 0:
                    WEAKenemyXCHANGE[x] = 1
                    WEAKenemyHP[x] = WEAKenemyHP[x] - 0.1
                elif WEAKenemyX[x] >= 1436:
                    WEAKenemyXCHANGE[x] = -1
                    WEAKenemyHP[x] = WEAKenemyHP[x] - 0.1
                elif WEAKenemyY[x] <= 0:
                    WEAKenemyYCHANGE[x] = 1
                    WEAKenemyHP[x] = WEAKenemyHP[x] - 0.1
                elif WEAKenemyY[x] >= 760:
                    WEAKenemyYCHANGE[x] = -1
                    WEAKenemyHP[x] = WEAKenemyHP[x] - 0.1
                distance = math.sqrt(math.pow(WEAKenemyX[x] - laserX, 2) + math.pow(WEAKenemyY[x] - laserY, 2))
                if distance < 54:
                    WEAKenemyHP[x] = WEAKenemyHP[x] - playerDMG
                    laserX = -100
                    laserY = -100
                    laser = False
                if WEAKenemyHP[x] <= 0:
                    WEAKenemyHP[x] = 0
                    WEAKenemyALIVE[x] = False
                    blastX = WEAKenemyX[x]
                    blastY = WEAKenemyY[x]
                    WEAKenemyX[x] = -100
                    WEAKenemyY[x] = -100
                    dedeffect = 250
                    dedsound = mixer.Sound('sounds/explosion.wav')
                    dedsound.play()
                    score = score + (100 * wave)
                    while dedeffect != 0:
                        screen.fill((255, 255, 0))
                        screen.blit(blast, (blastX, blastY))
                        pygame.display.update()
                        dedeffect = dedeffect - 1
                    break
                playerDistance = math.sqrt(math.pow(WEAKenemyX[x] - playerX, 2) + math.pow(WEAKenemyY[x] - playerY, 2))
                if playerDistance < 54:
                    screen.fill((255, 0, 0))
                    pygame.display.update()
                    playerHP = playerHP - 1
                    WEAKenemyHP[x] = WEAKenemyHP[x] - 1
            x = x - 1

        x = (wave // 2) - 1
        while x != -1:
            if STRONGenemyALIVE[x]:
                STRONGenemyX[x] = STRONGenemyX[x] + STRONGenemyXCHANGE[x]
                STRONGenemyY[x] = STRONGenemyY[x] + STRONGenemyYCHANGE[x]
                if STRONGenemyX[x] <= 0:
                    STRONGenemyXCHANGE[x] = 2
                    STRONGenemyHP[x] = STRONGenemyHP[x] - 0.1
                elif STRONGenemyX[x] >= 1436:
                    STRONGenemyXCHANGE[x] = -2
                    STRONGenemyHP[x] = STRONGenemyHP[x] - 0.1
                elif STRONGenemyY[x] <= 0:
                    STRONGenemyYCHANGE[x] = 2
                    STRONGenemyHP[x] = STRONGenemyHP[x] - 0.1
                elif STRONGenemyY[x] >= 760:
                    STRONGenemyYCHANGE[x] = -2
                    STRONGenemyHP[x] = STRONGenemyHP[x] - 0.1
                distance = math.sqrt(math.pow(STRONGenemyX[x] - laserX, 2) + math.pow(STRONGenemyY[x] - laserY, 2))
                if distance < 54:
                    STRONGenemyHP[x] = STRONGenemyHP[x] - playerDMG
                    laserX = -100
                    laserY = -100
                    laser = False
                if STRONGenemyHP[x] <= 0:
                    STRONGenemyHP[x] = 0
                    STRONGenemyALIVE[x] = False
                    blastX = STRONGenemyX[x]
                    blastY = STRONGenemyY[x]
                    STRONGenemyX[x] = -100
                    STRONGenemyY[x] = -100
                    dedeffect = 100
                    dedsound = mixer.Sound('sounds/explosion.wav')
                    dedsound.play()
                    score = score + (350 * wave)
                    while dedeffect != 0:
                        screen.fill((255, 255, 0))
                        screen.blit(blast, (blastX, blastY))
                        pygame.display.update()
                        dedeffect = dedeffect - 1
                    break
                playerDistance = math.sqrt(math.pow(STRONGenemyX[x] - playerX, 2) + math.pow(STRONGenemyY[x] - playerY, 2))
                if playerDistance < 54:
                    screen.fill((255, 0, 0))
                    pygame.display.update()
                    playerHP = playerHP - 5
                    STRONGenemyHP[x] = STRONGenemyHP[x] - 1
            x = x - 1

        x = (wave // 5) - 1
        while x != -1:
            if CRITICALenemyALIVE[x]:
                CRITICALenemyX[x] = CRITICALenemyX[x] + CRITICALenemyXCHANGE[x]
                CRITICALenemyY[x] = CRITICALenemyY[x] + CRITICALenemyYCHANGE[x]
                if CRITICALenemyX[x] <= 0:
                    CRITICALenemyXCHANGE[x] = 3
                    CRITICALenemyHP[x] = CRITICALenemyHP[x] - 0.1
                elif CRITICALenemyX[x] >= 1436:
                    CRITICALenemyXCHANGE[x] = -3
                    CRITICALenemyHP[x] = CRITICALenemyHP[x] - 0.1
                elif CRITICALenemyY[x] <= 0:
                    CRITICALenemyYCHANGE[x] = 3
                    CRITICALenemyHP[x] = CRITICALenemyHP[x] - 0.1
                elif CRITICALenemyY[x] >= 760:
                    CRITICALenemyYCHANGE[x] = -3
                    CRITICALenemyHP[x] = CRITICALenemyHP[x] - 0.1
                distance = math.sqrt(math.pow(CRITICALenemyX[x] - laserX, 2) + math.pow(CRITICALenemyY[x] - laserY, 2))
                if distance < 54:
                    CRITICALenemyHP[x] = CRITICALenemyHP[x] - playerDMG
                    laserX = -100
                    laserY = -100
                    laser = False
                if CRITICALenemyHP[x] <= 0:
                    CRITICALenemyHP[x] = 0
                    CRITICALenemyALIVE[x] = False
                    blastX = CRITICALenemyX[x]
                    blastY = CRITICALenemyY[x]
                    CRITICALenemyX[x] = -100
                    CRITICALenemyY[x] = -100
                    dedeffect = 100
                    dedsound = mixer.Sound('sounds/explosion.wav')
                    dedsound.play()
                    score = score + (1000 * wave)
                    while dedeffect != 0:
                        screen.fill((255, 255, 0))
                        screen.blit(blast, (blastX, blastY))
                        pygame.display.update()
                        dedeffect = dedeffect - 1
                    break
                playerDistance = math.sqrt(math.pow(CRITICALenemyX[x] - playerX, 2) + math.pow(CRITICALenemyY[x] - playerY, 2))
                if playerDistance < 54:
                    screen.fill((255, 0, 0))
                    pygame.display.update()
                    playerHP = playerHP - 10
                    CRITICALenemyHP[x] = CRITICALenemyHP[x] - 1
            x = x - 1

        x = (wave // 10) - 1
        while x != -1:
            if CREEPERenemyALIVE[x]:
                CREEPERenemyX[x] = CREEPERenemyX[x] + CREEPERenemyXCHANGE[x]
                CREEPERenemyY[x] = CREEPERenemyY[x] + CREEPERenemyYCHANGE[x]
                CREEPERenemyHP[x] = CREEPERenemyHP[x] + 0.02
                if CREEPERenemyHPcolor[x] == 125:
                    creeperenemyhpcoloradd = 5
                if CREEPERenemyHPcolor[x] == 255:
                    creeperenemyhpcoloradd = -5
                CREEPERenemyHPcolor[x] = CREEPERenemyHPcolor[x] + creeperenemyhpcoloradd
                if CREEPERenemyHP[x] > 150:
                    CREEPERenemyHP[x] = 150
                if CREEPERenemyX[x] <= 0:
                    CREEPERenemyXCHANGE[x] = 0.5
                    CREEPERenemyHP[x] = CREEPERenemyHP[x] - 0.1
                elif CREEPERenemyX[x] >= 1436:
                    CREEPERenemyXCHANGE[x] = -0.5
                    CREEPERenemyHP[x] = CREEPERenemyHP[x] - 0.1
                elif CREEPERenemyY[x] <= 0:
                    CREEPERenemyYCHANGE[x] = 0.5
                    CREEPERenemyHP[x] = CREEPERenemyHP[x] - 0.1
                elif CREEPERenemyY[x] >= 760:
                    CREEPERenemyYCHANGE[x] = -0.5
                    CREEPERenemyHP[x] = CREEPERenemyHP[x] - 0.1
                distance = math.sqrt(math.pow(CREEPERenemyX[x] - 40 - laserX, 2) + math.pow(CREEPERenemyY[x] - 40 - laserY, 2))
                if distance < 120:
                    CREEPERenemyHP[x] = CREEPERenemyHP[x] - playerDMG
                    laserX = -100
                    laserY = -100
                    laser = False
                if CREEPERenemyHP[x] <= 0:
                    CREEPERenemyHP[x] = 0
                    CREEPERenemyALIVE[x] = False
                    blastX = CREEPERenemyX[x]
                    blastY = CREEPERenemyY[x]
                    CREEPERenemyX[x] = -100
                    CREEPERenemyY[x] = -100
                    dedeffect = 100
                    dedsound = mixer.Sound('sounds/explosion.wav')
                    dedsound.play()
                    score = score + (20000 * wave)
                    while dedeffect != 0:
                        screen.fill((255, 255, 0))
                        screen.blit(blast, (blastX, blastY))
                        pygame.display.update()
                        dedeffect = dedeffect - 1
                    break
                playerDistance = math.sqrt(
                    math.pow(CREEPERenemyX[x] - 40 - playerX, 2) + math.pow(CREEPERenemyY[x] - 40 - playerY, 2))
                if playerDistance < 120:
                    screen.fill((255, 0, 0))
                    pygame.display.update()
                    playerHP = playerHP - 10
                    CREEPERenemyHP[x] = CREEPERenemyHP[x] - 1
                CREEPERenemyANGLE[x] = CREEPERenemyANGLE[x] + 0.2
            x = x - 1

        totalenemyHP = 0
        x = wave - 1
        while x != -1:
            totalenemyHP = totalenemyHP + WEAKenemyHP[x]
            x = x - 1
        x = (wave // 2) - 1
        while x != -1:
            totalenemyHP = totalenemyHP + STRONGenemyHP[x]
            x = x - 1
        x = (wave // 5) - 1
        while x != -1:
            totalenemyHP = totalenemyHP + CRITICALenemyHP[x]
            x = x - 1
        x = (wave // 10) - 1
        while x != -1:
            totalenemyHP = totalenemyHP + CREEPERenemyHP[x]
            x = x - 1

        if not damagepowerup:
            if random.randint(0, 20) == 1:
                damagepowerup = True
                damagepowerupX = random.randint(0, 1400)
                damagepowerupY = random.randint(0, 700)
                damagepowerupANGLE = random.randint(0, 359)
                mixer.Sound('sounds/powerupspawn.wav').play()
                mixer.Sound('sounds/powerupspawn.wav').play()
                mixer.Sound('sounds/powerupspawn.wav').play()
                mixer.Sound('sounds/powerupspawn.wav').play()
                mixer.Sound('sounds/powerupspawn.wav').play()


        DISPLAYscore = int(score)
        DISPLAYscoreTRUE = True
        modvalue = 0
        if score / 1000000 > 1 and DISPLAYscoreTRUE:
            modvalue = score % 1000000
            if modvalue < 100000:
                modvalue = ""
            else:
                modvalue = "." + str(int(modvalue))[0]
            DISPLAYscore = str(int(score / 1000000)) + modvalue + "M"
            DISPLAYscoreTRUE = False
        if score / 1000 > 1 and DISPLAYscoreTRUE:
            modvalue = score % 1000
            if modvalue < 100:
                modvalue = ""
            else:
                modvalue = "." + str(int(modvalue))[0]
            DISPLAYscore = str(int(score / 1000)) + modvalue + "K"
            DISPLAYscoreTRUE = False

        # Draw
        hptext = font.render("Health: " + str(int(playerHP)), True, hpcolor)
        enemyhptext = font.render("Total Enemy Health: " + str(int(totalenemyHP)), True, (0, 255, 0))
        screen.fill((0, 0, 0))
        backgroundnum = backgroundnum + 1
        if backgroundnum == 17:
            backgroundnum = 1
        background = pygame.transform.scale(background, (1500, 800))
        screen.blit(background, (0, 0))
        screen.blit(wavefont.render(str(wave), True, (255, 225, 255)), (700, 275))
        playerX = playerX + playerXCHANGE
        playerY = playerY + playerYCHANGE
        if laser:
            laserX += laserXCHANGE
            laserY += laserYCHANGE
            screen.blit(pygame.transform.rotate(laserIMG, laserangle), (laserX, laserY))
            if laserX <= -100 or laserX >= 1600:
                laser = False
            if laserY <= -100 or laserY >= 900:
                laser = False
        screen.blit(pygame.transform.rotate(playerIMAGE, angle), (playerX, playerY))

        if damagepowerup:
            damagepowerupANGLE = damagepowerupANGLE + 0.4
            screen.blit(pygame.transform.rotate(damagepowerupIMG, damagepowerupANGLE), (damagepowerupX, damagepowerupY))



        x = wave - 1
        while x != -1:
            if WEAKenemyALIVE[x]:
                screen.blit(WEAKenemyIMG[x], (WEAKenemyX[x], WEAKenemyY[x]))
                pygame.draw.rect(screen, (0, 255, 0), (WEAKenemyX[x], WEAKenemyY[x], WEAKenemyHP[x] * 6.5, 10))
            x = x - 1

        x = (wave // 2) - 1
        while x != -1:
            if STRONGenemyALIVE[x]:
                screen.blit(STRONGenemyIMG[x], (STRONGenemyX[x], STRONGenemyY[x]))
                pygame.draw.rect(screen, (0, 255, 0), (STRONGenemyX[x], STRONGenemyY[x], STRONGenemyHP[x] * 2.5, 10))
            x = x - 1

        x = (wave // 5) - 1
        while x != -1:
            if CRITICALenemyALIVE[x]:
                screen.blit(CRITICALenemyIMG[x], (CRITICALenemyX[x], CRITICALenemyY[x]))
                pygame.draw.rect(screen, (0, 255, 0), (CRITICALenemyX[x], CRITICALenemyY[x], CRITICALenemyHP[x] * 1.35, 10))
            x = x - 1

        x = (wave // 10) - 1
        while x != -1:
            if CREEPERenemyALIVE[x]:
                pygame.draw.rect(screen, (0, 0, CREEPERenemyHPcolor[x]), (CREEPERenemyX[x] - 70, CREEPERenemyY[x] - 80, CREEPERenemyHP[x] * 0.85, 10))
                CREEPERenemyIMGrotate[x] = pygame.transform.rotate(CREEPERenemyIMG[x], CREEPERenemyANGLE[x])
                screen.blit(CREEPERenemyIMGrotate[x], (CREEPERenemyX[x] - int(CREEPERenemyIMGrotate[x].get_width()/ 2), CREEPERenemyY[x] - int(CREEPERenemyIMGrotate[x].get_height() / 2)))
            x = x - 1


        pygame.draw.rect(screen, dedcolor, (250, 725, 1000, 7))
        pygame.draw.rect(screen, hpcolor, (250, 725, playerHP / maxplayerHP * 1000, 7))
        screen.blit(hptext, (250, 680))
        pygame.draw.rect(screen, (255, 255, 255), (250, 50, 1000, 7))
        pygame.draw.rect(screen, (0, 255, 0), (250, 50, (totalenemyHP / maxenemyHP) * 1000, 7))
        screen.blit(enemyhptext, (250, 55))

        score = score + wave * 0.1

        scoretext = font.render("Score: " + str(DISPLAYscore), True, (255, 255, 255))
        screen.blit(scoretext, (250, 100))


        pygame.draw.rect(screen, (0, 255, 0), (250, 750, 300, 25))
        pygame.draw.rect(screen, (255, 255, 0), (550, 750, 150, 25))
        pygame.draw.rect(screen, (255, 0, 0), (700, 750, 45, 25))
        pygame.draw.rect(screen, (255, 0, 255), (745, 750, 10, 25))
        pygame.draw.rect(screen, (255, 0, 0), (755, 750, 45, 25))
        pygame.draw.rect(screen, (255, 255, 0), (800, 750, 150, 25))
        pygame.draw.rect(screen, (0, 255, 0), (950, 750, 300, 25))

        screen.blit(slider, (220 + sliderval, 732))



        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 1500, 7))
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 7, 800))
        pygame.draw.rect(screen, (255, 0, 0), (1493, 0, 7, 800))
        pygame.draw.rect(screen, (255, 0, 0), (0, 793, 1500, 7))

        screen.blit(statfont.render("Made By TayalUltimate", True, (255, 255, 255)), (7, 7))

        # Update {DO NOT ERASE}
        pygame.display.update()

    if gameover:

        screen.fill((255, 0, 0))
        gameovertext = newwavefont.render("Game Over", True, True)
        retrytext = font.render("Press Mouse Key to Retry", True, True)
        screen.blit(gameovertext, (215, 250))
        screen.blit(font.render("Your Score: " + str(int(score)), True, (255, 255, 255)), (215, 220))
        screen.blit(retrytext, (500, 700))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pressed()[0]:
                gameover = False
                running = True
                playerIMAGE = pygame.image.load('images/spaceship.png')
                playerX = 718
                playerY = 650
                playerXCHANGE = 0
                playerYCHANGE = 0
                backgroundnum = 1
                angle = 0
                laser = False
                laserX = playerX
                laserY = playerY
                laserXCHANGE = 0
                laserYCHANGE = 0
                playerHP = 1000
                font = pygame.font.Font('font.ttf', 48)
                wavefont = pygame.font.Font('font.ttf', 256)
                statfont = pygame.font.Font('freesansbold.ttf', 16)
                hpcolor = (0, 255, 0)
                borderDMG = 1
                playerhealpower = 0.01
                noheal = False
                dedcolor = (255, 255, 255)
                slider = pygame.image.load('images/laser/slider.png')
                sliderval = 0
                sliderchange = 1
                borderDMGeffect = 0
                lasercolor = (255, 255, 255)
                laserIMG = pygame.image.load('images/laser/miss.png')
                laserangle = angle
                WEAKenemyIMG = []
                WEAKenemyX = []
                WEAKenemyY = []
                WEAKenemyXCHANGE = []
                WEAKenemyYCHANGE = []
                WEAKenemyHP = []
                WEAKenemyALIVE = []
                STRONGenemyIMG = []
                STRONGenemyX = []
                STRONGenemyY = []
                STRONGenemyXCHANGE = []
                STRONGenemyYCHANGE = []
                STRONGenemyHP = []
                STRONGenemyALIVE = []
                CRITICALenemyIMG = []
                CRITICALenemyX = []
                CRITICALenemyY = []
                CRITICALenemyXCHANGE = []
                CRITICALenemyYCHANGE = []
                CRITICALenemyHP = []
                CRITICALenemyALIVE = []
                CREEPERenemyIMG = []
                CREEPERenemyX = []
                CREEPERenemyY = []
                CREEPERenemyXCHANGE = []
                CREEPERenemyYCHANGE = []
                CREEPERenemyHP = []
                CREEPERenemyALIVE = []
                CREEPERenemyANGLE = []
                CREEPERenemyIMGrotate = []
                CREEPERenemyHPcolor = []
                wave = 0
                NEWwave = True
                a = wave
                playerDMG = 1
                totalenemyHP = 1
                maxenemyHP = 235
                distance = 10000000000
                newwaveeffect = 0
                playerDistance = 10000000000
                gameover = False
                newwavefont = 0
                blast = pygame.image.load('images/blast.png')
                blastX = -100
                blastY = -100
                score = 0
                maxplayerHP = 1000
                damagepowerupIMG = pygame.image.load('images/sword.png')
                damagepowerupANGLE = 0
                damagepowerup = False
                damagepowerupX = -100
                damagepowerupY = -100

