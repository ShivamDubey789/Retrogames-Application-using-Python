import pygame, random , os
from pygame.locals import *

pygame.init()

current_directory = os.path.dirname(__file__)

icon_path = os.path.join(current_directory,'flappybird icon.png')

icon = pygame.image.load(icon_path)  
pygame.display.set_icon(icon)


flap_path = os.path.join(current_directory,'flap.mp3')
flap = pygame.mixer.Sound(flap_path)

hit_path = os.path.join(current_directory,'hit.mp3')
hit = pygame.mixer.Sound(hit_path)
hitplay = False


clock = pygame.time.Clock()


screen_width = 864
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Flappy Bird")

font = pygame.font.SysFont("Bauhaus 93",60)

white = (255,255,255)

ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False


bg_path = os.path.join(current_directory,'bg.png')
bg = pygame.image.load(bg_path)

ground_path = os.path.join(current_directory,'ground.png')
ground = pygame.image.load(ground_path)




def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))


class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0

        for num in range(1,4):
            bird_path = os.path.join(current_directory,rf'bird{num}.png')
            img =  pygame.image.load(bird_path)
            self.images.append(img)
        self.image = self.images[self.index ]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.clicked = False

    def update(self):
        
        if flying == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 680:
                self.rect.y += int(self.vel)

        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
                flap.play()

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                  
            
            flap_cooldown = 5
            self.counter += 1
        

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]

            self.image = pygame.transform.rotate(self.images[self.index],self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index],-90)

class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        pipe_path = os.path.join(current_directory,'pipe.png')
        self.image = pygame.image.load(pipe_path)
        self.rect = self.image.get_rect()
        
        if position == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x, y - int(pipe_gap /2 )]
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap /2 )]
    
    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 200:
            self.kill
            

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100,int(screen_height / 2))
 
bird_group.add(flappy)




run = True 
def reset_game():
    global bird_group, pipe_group, flappy, flying, game_over, ground_scroll, score, pass_pipe, last_pipe,hitplay
    bird_group = pygame.sprite.Group()
    pipe_group = pygame.sprite.Group()
    flappy = Bird(100, int(screen_height / 2))
    bird_group.add(flappy)
    flying = False
    game_over = False
    ground_scroll = 0
    pass_pipe = False
    last_pipe = pygame.time.get_ticks() - pipe_frequency
    hitplay = False

reset_text = font.render("Press any key to reset game", True, white)

while run:
    clock.tick(60)

    screen.blit(bg,(0,0))

    if not flying and not game_over:
        start_text = font.render("Press Right Click to Start", True, white)
        screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, screen_height // 3))


    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)
    


    screen.blit(ground,(ground_scroll,680))

    if len(pipe_group) > 0:
        
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
			and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
			and pass_pipe == False:
            pass_pipe = True
       
        bird_center_x = bird_group.sprites()[0].rect.centerx

        pipe_center_x = pipe_group.sprites()[0].rect.centerx

        if bird_center_x >= pipe_center_x and not pass_pipe:
                 score += 1
                 pass_pipe = True
               
                    
    draw_text(str(score),font,white,int(screen_width /2),20)


    
    if pygame.sprite.groupcollide(bird_group,pipe_group,False,False) or flappy.rect.top < 0 and flappy.rect.bottom < 0:
        game_over = True
        if not hitplay:
            hit.play()
            hitplay = True
        

    if flappy.rect.bottom >= 680:
        game_over = True
        flying = False
        if not hitplay:
            hit.play()
            hitplay = True


    if flying == True and game_over == False:
     
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
                pass_pipe = False
                pipe_height = random.randint(-100,100)
                btm_pipe = Pipe(screen_width, int(screen_height / 2 ) + pipe_height, -1)
                top_pipe = Pipe(screen_width, int(screen_height / 2 ) + pipe_height, 1)
                pipe_group.add(btm_pipe)
                pipe_group.add(top_pipe)
                last_pipe = time_now

        pipe_group.update()

        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN and game_over:
            reset_game()
            score = 0
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
    
    if game_over:
        screen.blit(reset_text, (screen_width // 2 - reset_text.get_width() // 2, screen_height // 2))

   
    pygame.display.update()


pygame.quit