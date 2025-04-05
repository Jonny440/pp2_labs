import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

#Setting up variables
fps = 60
framePerSec = pygame.time.Clock()

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

screenWidth = 840
screenHeight = 650
speed = 5
score = 0
coins = 0

font = pygame.font.SysFont("times new roman", 60)
fontSmall = pygame.font.SysFont("times new roman", 20)
gameOver = font.render("Game Over", True, black)

background = pygame.image.load("road.png")

displaySurf = pygame.display.set_mode((840,650))
displaySurf.fill(white)
pygame.display.set_caption("Game")

#Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screenWidth-40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.top > 650):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screenWidth - 40), 0)

#Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressedKeys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressedKeys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screenWidth:
            if pressedKeys[K_RIGHT]:
                self.rect.move_ip(5, 0)

#Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screenWidth - 40), 0)
        
    def move(self):
        global coins
        self.rect.move_ip(0, speed)
        if (self.rect.top > 650):
            self.rect.top = 0
            self.rect.center = (random.randint(40, screenWidth - 40), 0)

#Creting objects of the game
player1 = Player()
enemy1 = Enemy()
enemy2 = Enemy()
coin1 = Coin()
coin2 = Coin()

#collecting objects into sprite groups
enemiesGroup = pygame.sprite.Group()
enemiesGroup.add(enemy1)
enemiesGroup.add(enemy2)

coinsGroup = pygame.sprite.Group()
coinsGroup.add(coin1)
coinsGroup.add(coin2)

allSprites = pygame.sprite.Group()
allSprites.add(player1)
allSprites.add(enemy1)
allSprites.add(enemy2)
allSprites.add(coin1)
allSprites.add(coin2)

# custom user event, handles speed inscreasment
incSpeed = pygame.USEREVENT + 1
pygame.time.set_timer(incSpeed, 1000)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == incSpeed:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaySurf.blit(background, (0,0))

    # Display score and coins
    scoreText = fontSmall.render(f"Score: {score}", True, black)
    displaySurf.blit(scoreText, (10,10))

    coinText = fontSmall.render(f"Coins: {coins}", True, black)
    displaySurf.blit(coinText, (screenWidth - 100, 10))  # Right top corner

    # Moves and redraws sprites
    for entity in allSprites:
        displaySurf.blit(entity.image, entity.rect)
        entity.move()

    # Collision check between player and enemy
    if pygame.sprite.spritecollideany(player1, enemiesGroup):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        displaySurf.fill(red)
        displaySurf.blit(gameOver, (30,250))

        pygame.display.update()
        for entity in allSprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    #check collsions between player and coiny
    if pygame.sprite.spritecollideany(player1, coinsGroup):
        coins += 1  #increase the coin count
        for coin in coinsGroup:
            coin.rect.top = 0
            coin.rect.center = (random.randint(40, screenWidth - 40), 0)  #move the coin back to top

    pygame.display.update()
    framePerSec.tick(fps)
