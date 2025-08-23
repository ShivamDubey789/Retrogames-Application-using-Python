import pygame,sys,random , os

current_directory = os.path.dirname(__file__)

def reset_ball():
    global ball_speed_x , ball_speed_y 
    ball.x = screen_width/2 - 10
    ball.y = random.randint(10,100)
    ball_speed_x *= random.choice([-1,1])
    ball_speed_y *= random.choice([-1,1])

def point_won(winner):
    global player2_points,player1_points
    if winner == "Player 2":
        player2_points += 1 
    
    if winner == "player 1":
        player1_points += 1

    reset_ball()

def animate_ball():
    global ball_speed_x , ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y



    if ball.bottom >= screen_height or ball.top <= 0:
       ball_speed_y *= -1
       
    
    if ball.right >= screen_width:
        point_won("Player 2")
        pongmiss_sound.play()
        
    if  ball.left <=0:
        point_won("player 1")
        pongmiss_sound.play()

    if ball.colliderect(player) or ball.colliderect(player_2):
        ball_speed_x *= -1

        paddlecollision_sound.play()

def animate_player():
    player.y += player_speed
    

    if player.top <= 0:
        player.top = 0

    if player.bottom >= screen_height:
        player.bottom = screen_height


    

def animate_player2():
    player_2.y += player2_speed

    if player_2.top <= 0:
        player_2.top = 0

    if player_2.bottom >= screen_height:
        player_2.bottom = screen_height



pygame.init()

bgmusic = os.path.join(current_directory,'bgpong.mp3')

pygame.mixer.music.load(bgmusic)  
pygame.mixer.music.set_volume(5)  
pygame.mixer.music.play(-1)



screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Defend the ball")

bgimage_path = os.path.join(current_directory,'pongbg.jpg')

background_image = pygame.image.load(bgimage_path)
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))


paddle_path = os.path.join(current_directory,'PADHIT.mp3')
paddlecollision_sound = pygame.mixer.Sound(paddle_path)

pongmiss_path = os.path.join(current_directory,'pongmiss.mp3')
pongmiss_sound = pygame.mixer.Sound(pongmiss_path)

icon_path = os.path.join(current_directory,'pong icon.png')
icon = pygame.image.load(icon_path)  
pygame.display.set_icon(icon)



clock = pygame.time.Clock()

ball_path = os.path.join(current_directory,'ball.png')
ball_image = pygame.image.load(ball_path)  # Load image of the ball
ball_image = pygame.transform.scale(ball_image, (45, 45))  # Scale the image to match the size of the ball

ball = pygame.Rect(0, 0, 45, 45)
ball.center = (screen_width / 2, screen_height / 2)

player_2 = pygame.Rect(0,0,20,100)
player_2.centery = screen_height/2

player = pygame.Rect(0,0,20,100)
player.midright = (screen_width,screen_height/2)

ball_speed_x = 9
ball_speed_y = 9
player_speed = 0
player2_speed = 0 

player1_points , player2_points = 0,0

score_font = pygame.font.Font(None , 60)

while True:
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -6
            if event.key == pygame.K_DOWN:
                player_speed = 6
            if event.key == pygame.K_w:
                player2_speed = -6
            if event.key == pygame.K_s:
                player2_speed = 6

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player_speed = 0
            if event.key in (pygame.K_w, pygame.K_s):
                player2_speed = 0

    # Change the position of the game objects
    animate_ball()
    animate_player()
    animate_player2()


    # Check if a player has won the game
    if player2_points  >=10:
        winner_message = score_font.render("Player A has won the game!", True, "white")
        screen.blit(winner_message, (screen_width // 2 - 200, screen_height // 2))
        pygame.display.update()
        pygame.mixer.music.stop()
        pygame.time.delay(4000)  # Pause for 3 seconds to display the message
        
        pygame.quit()
        sys.exit()

    elif player1_points >= 10:
        winner_message = score_font.render("Player B has won the game!", True, "white")
        screen.blit(winner_message, (screen_width // 2 - 200, screen_height // 2))
        pygame.display.update()
        pygame.mixer.music.stop()
        pygame.time.delay(4000)  # Pause for 3 seconds to display the message
            
        pygame.quit()
        sys.exit()

    

    # Draw the game objects
    screen.fill("black")
    screen.blit(background_image, (0, 0))
    player2_score_surface = score_font.render(str(f"Player A:{player2_points}"), True, "white")
    player1_score_surface = score_font.render(str(f"Player B:{player1_points}"), True, "white")
    screen.blit(player2_score_surface, (200, 40))
    screen.blit(player1_score_surface, (850, 40))
    pygame.draw.aaline(screen, 'white', (screen_width/2, 0), (screen_width/2, screen_height))
    pygame.draw.aaline(screen, 'white', (0, 100), (screen_width, 100))
    screen.blit(ball_image, ball)
    pygame.draw.rect(screen, "white", player_2)
    pygame.draw.rect(screen, "white", player)
    
    # Update the display
    pygame.display.update()
    clock.tick(60)
