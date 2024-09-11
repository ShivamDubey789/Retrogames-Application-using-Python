import pygame,sys,os
import random

pygame.init()
current_directory = os.path.dirname(__file__)


ICON_PATH = os.path.join(current_directory,'dinorun icon.png')
icon = pygame.image.load(ICON_PATH)  
pygame.display.set_icon(icon)
pygame.display.set_caption("Dino Run")



SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


DINORUN_PATH1 = os.path.join(current_directory,'DinoRun1.png')
DINORUN_PATH2 = os.path.join(current_directory,'DinoRun2.png')

RUNNING = [pygame.image.load(DINORUN_PATH1),
           pygame.image.load(DINORUN_PATH2)
           ]

JUMPING_PATH = os.path.join(current_directory,'DinoJump.png')
JUMPING = pygame.image.load(JUMPING_PATH)


DUCKING_PATH1 = os.path.join(current_directory,'DinoDuck1.png')
DUCKING_PATH2 = os.path.join(current_directory,'DinoDuck2.png')
DUCKING = [pygame.image.load(DUCKING_PATH1),
           pygame.image.load(DUCKING_PATH2)]

SMALL_CACTUS_PATH1 = os.path.join(current_directory,'SmallCactus1.png')
SMALL_CACTUS_PATH2 = os.path.join(current_directory,'SmallCactus2.png')
SMALL_CACTUS_PATH3 = os.path.join(current_directory,'SmallCactus3.png')
SMALL_CACTUS = [pygame.image.load(SMALL_CACTUS_PATH1),
                pygame.image.load(SMALL_CACTUS_PATH1),
                pygame.image.load(SMALL_CACTUS_PATH1)]

LARGE_CACTUS_PATH1 = os.path.join(current_directory,'LargeCactus1.png')
LARGE_CACTUS_PATH2 = os.path.join(current_directory,'LargeCactus2.png')
LARGE_CACTUS_PATH3 = os.path.join(current_directory,'LargeCactus3.png')
LARGE_CACTUS = [pygame.image.load(LARGE_CACTUS_PATH1),
                pygame.image.load(LARGE_CACTUS_PATH2),
                pygame.image.load(LARGE_CACTUS_PATH3)]

BIRD_PATH1 = os.path.join(current_directory,'Bird1 copy.png')
BIRD_PATH2 = os.path.join(current_directory,'Bird2 copy.png')
BIRD = [pygame.image.load(BIRD_PATH1),
        pygame.image.load(BIRD_PATH2)]

CLOUD_PATH = os.path.join(current_directory,'Cloud.png')
CLOUD = pygame.image.load(CLOUD_PATH)

BG_PATH = os.path.join(current_directory,'Track.png')
BG = pygame.image.load(BG_PATH)

DIE_SOUND_PATH = os.path.join(current_directory,'dinodie.mp3')
diesound = pygame.mixer.Sound(DIE_SOUND_PATH)

pointsound_path = os.path.join(current_directory,'rename.mp3')
pointsound = pygame.mixer.Sound(pointsound_path)

jumpsound_path = os.path.join(current_directory,'jump.mp3')
jumpsound = pygame.mixer.Sound(jumpsound_path)

class dinosaur:
    xpos = 80
    ypos = 310
    ypos_duck = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.xpos
        self.dino_rect.y = self.ypos

    def update(self,userinput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

       
        if self.step_index >= 10:
            self.step_index = 0

        if userinput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userinput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not(self.dino_jump or userinput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True 
            self.dino_jump = False

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.xpos
        self.dino_rect.y = self.ypos
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.xpos
        self.dino_rect.y = self.ypos_duck
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel <- self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
            jumpsound.play()

    def draw(self,SCREEN):
        SCREEN.blit(self.image,(self.dino_rect.x,self.dino_rect.y))

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800,1000)
        self.y = random.randint(50,100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x <- self.width:
            self.x = SCREEN_WIDTH + random.randint(2500,3000)
            self.y = random.randint(50,100)
    
    def draw(self,SCREEN):
        SCREEN.blit(self.image,(self.x,self.y))

class obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type 
        self.rect = self.image[self.type].get_rect() 
        self.rect.x = SCREEN_WIDTH
    
    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type],self.rect)

class SmallCactus(obstacle):
    def __init__(self,image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus(obstacle):
    def __init__(self,image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(obstacle):
    def __init__(self,image):
        self.type = 0
        super().__init__(image,self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self,SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5],self.rect)
        self.index += 1 

def main():
    global game_speed,xposbg,yposbg,points,obstacles
    run = True
    clock = pygame.time.Clock()
    player = dinosaur()
    cloud = Cloud()
    game_speed = 16
    xposbg = 0 
    yposbg = 380
    points = 0
    font = pygame.font.Font(None ,20)
    obstacles = []
    death_count = 0

    def score():
        global points,game_speed
        points += 1 
        if points % 200 == 0:
            game_speed += 5
            pointsound.play()

        text = font.render("SCORE:"+str(points),True,(0,0,0))
        textRect = text.get_rect()
        textRect.center = (1000,40)
        SCREEN.blit(text,textRect)

    def background():
        global xposbg,yposbg
        image_width = BG.get_width()
        SCREEN.blit(BG,(xposbg,yposbg))
        SCREEN.blit(BG,(image_width + xposbg,yposbg))
        if xposbg <= -image_width:
            SCREEN.blit(BG,(image_width + xposbg,yposbg))
            xposbg = 0
        xposbg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255,255,255))
        userinput = pygame.key.get_pressed()

        background()

        player.draw(SCREEN)
        player.update(userinput)

        if len(obstacles) == 0:
            if random.randint(0,2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0,2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0,2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()       
            if player.dino_rect.colliderect(obstacle.rect):
                diesound.play()
                pygame.time.delay(2000)
                death_count += 1 
                
                menu(death_count)
            
        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()



def menu(death_count):
    global points 
    run = True 
    while run:
        SCREEN.fill((255,255,255))
        font = pygame.font.Font("freesansbold.ttf",30)

        if death_count == 0:
            text = font.render("Press any key to Start\nUse Arrow Key to jump and duck ",True,(0,0,0))
        elif death_count > 0:
            text = font.render("Press any Key to restart",True,(0,0,0))
            score = font.render("your Score:"+ str(points),True,(0,0,0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH//2 , SCREEN_HEIGHT //2 + 50)
            SCREEN.blit(score,scoreRect)
        
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
        SCREEN.blit(text,textRect)
        SCREEN.blit(RUNNING[0],(SCREEN_WIDTH//2 - 20,SCREEN_HEIGHT //2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)