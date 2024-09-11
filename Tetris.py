import pygame , sys , os
from tetrisgame import Game
from tetriscolors import Colors


pygame.init()
current_directory = os.path.dirname(__file__)

icon_path = os.path.join(current_directory,'tetris icon.png')


icon = pygame.image.load(icon_path)  
pygame.display.set_icon(icon)

title_font = pygame.font.Font(None,40)
press_font = pygame.font.Font(None,20)
score_surface = title_font.render("Score",True,Colors.white)
game_over_surface = title_font.render("GAME OVER",True,Colors.white)
presskey_surface = press_font.render("Press any key to reset game",True,Colors.white)
score_rect = pygame.Rect(400,55,170,60)


screen = pygame.display.set_mode((600,630))
pygame.display.set_caption("Tetris Game")

clock = pygame.time.Clock()


game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0,1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()


    score_value_surface = title_font.render(str(game.score),True,Colors.white)
    screen.fill(Colors.black)
    screen.blit(score_surface,(450,25,50,50))

    if game.game_over == True:
        screen.blit(game_over_surface,(400,450,50,50))
        screen.blit(presskey_surface,(400,500,50,50))
        pygame.mixer.music.stop()

       



    pygame.draw.rect(screen,Colors.light_blue,score_rect)
    screen.blit(score_value_surface,score_value_surface.get_rect(centerx = score_rect.centerx,centery = score_rect.centery) )
    game.draw(screen)
    


    pygame.display.update()
    clock.tick(60)