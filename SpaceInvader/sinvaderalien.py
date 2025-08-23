import pygame , random , os
current_directory = os.path.dirname(__file__)

mystery_path = os.path.join(current_directory,'mystery.png')


class Alien(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        super().__init__()
        self.type = type
        path = os.path.join(current_directory,rf"alien_{type}.png")
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft = (x,y))
    
    def update(self,direction):
        self.rect.x += direction

class mysteryship(pygame.sprite.Sprite):
   
    def __init__(self,screen_width,offset):
        super().__init__()
        self.screen_width = screen_width
        self.offset = offset
        self.image = pygame.image.load(mystery_path)
        x = random.choice([self.offset/2,self.screen_width + self.offset - self.image.get_width()])

        if x == offset/2:
            self.speed = 3 
        else:
            self.speed = -3
        self.rect = self.image.get_rect(topleft = (x,90))

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen_width + self.offset/2:
            self.kill()
        elif self.rect.left < self.offset/2:
            self.kill()
        
