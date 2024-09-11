import time,os


from food import *
from turtle import *
from snake import *
from scoreboard import *
import pygame



pygame.init()
current_directory = os.path.dirname(__file__)

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("OliveDrab3")
screen.title("my snake game")
screen.tracer(0)


border = Turtle()
border.penup()
border.color("white")
border.goto(-290, -290)
border.pendown()
border.pensize(10)
for _ in range(4):
    border.forward(580)
    border.left(90)
border.hideturtle()

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

collision_sound_1 = os.path.join(current_directory,'food.mp3')
crash_sound_1 =  os.path.join(current_directory,'crash.mp3')
bgmusic = os.path.join(current_directory,'background.mp3')

collision_sound = pygame.mixer.Sound(collision_sound_1)
crash_sound = pygame.mixer.Sound(crash_sound_1)
pygame.mixer.music.load(bgmusic)
pygame.mixer.music.play(-1)


game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.075)
    snake.move()

    #detect collison with food
    if snake.head.distance(food) < 15:
        collision_sound.play()
        food.refresh() 
        snake.extend()
        scoreboard.increase_score()
       
    #detect collison with wall
    if snake.head.xcor() > 290 or snake.head.xcor()< -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        crash_sound.play()
        game_is_on = False
        scoreboard.reset()
        scoreboard.game_over()
        pygame.mixer.music.pause()
    

    #detect collision with  tail
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 10:
             crash_sound.play()
             game_is_on = False
             scoreboard.reset()
             scoreboard.game_over()
             pygame.mixer.music.pause()
    
    
screen.exitonclick( )
 
 