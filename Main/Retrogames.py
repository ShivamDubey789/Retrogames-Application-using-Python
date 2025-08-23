import customtkinter ,os 
import subprocess
from PIL import Image 
import pygame 



pygame.init()
current_directory = os.path.dirname(__file__)

snakegame = os.path.join(current_directory,'snakegames.exe')
tetrisgame = os.path.join(current_directory,'tetris.exe')
ponggame = os.path.join(current_directory,'pong game.exe')
spaceinvadergame = os.path.join(current_directory,'sinvader.exe')
flappybirdgame = os.path.join(current_directory,"flappybird.exe")
dinorungame = os.path.join(current_directory,"dinorun.exe")

snake_process = None  # Global variable to keep track of the snake game process
pong_process = None
tetris_process = None
dinorun_process = None
spaceinvader_process = None
flappybird_process = None

def run_snake_game():
    global snake_process
    snakegame_script = snakegame
    root.withdraw() # Hide the main window
    snake_process = subprocess.Popen([snakegame_script],creationflags=subprocess.CREATE_NO_WINDOW, env=os.environ)
    snake_process.wait()  # Wait for the snake game process to finish
    root.deiconify()  # Show the main window again

def run_Pong_game():
    global pong_process
    pong_script = ponggame
    root.withdraw()  # Hide the main window
    pong_process = subprocess.Popen([pong_script],creationflags=subprocess.CREATE_NO_WINDOW, env=os.environ)
    pong_process.wait()  # Wait for the snake game process to finish
    root.deiconify()  # Show the main window again


def run_Tetris_game():
    global tetris_process
    tetris_script = tetrisgame
    root.withdraw()  # Hide the main window
    tetris_process = subprocess.Popen([tetris_script],creationflags=subprocess.CREATE_NO_WINDOW, env=os.environ)
    tetris_process.wait()  # Wait for the snake game process to finish
    root.deiconify()  # Show the main window again

def run_dinorun_game():
    global dinorun_process
    dinorun_script = dinorungame
    root.withdraw()  # Hide the main window
    dinorun_process = subprocess.Popen([dinorun_script],creationflags=subprocess.CREATE_NO_WINDOW, env=os.environ)
    dinorun_process.wait()  # Wait for the snake game process to finish
    root.deiconify()  # Show the main window again


def run_spaceinvader_game():
    global spaceinvader_process
    spaceinvader_script = spaceinvadergame
    root.withdraw()  # Hide the main window
    spaceinvader_process = subprocess.Popen([spaceinvader_script],creationflags=subprocess.CREATE_NO_WINDOW, env=os.environ)
    spaceinvader_process.wait()  # Wait for the snake game process to finish
    root.deiconify()  # Show the main window again

def run_flappybird_game():
    global flappybird_process
    flappybird_script = flappybirdgame
    root.withdraw()  # Hide the main window
    flappybird_process = subprocess.Popen([flappybird_script],creationflags=subprocess.CREATE_NO_WINDOW, env=os.environ)
    flappybird_process.wait()  # Wait for the snake game process to finish
    root.deiconify()  # Show the main window again
    

root = customtkinter.CTk()
root.title("The Retro Games")
root.geometry("800x600")
root.resizable(0,0)

icon_path = os.path.join(current_directory, "retrogame.ico")
root.iconbitmap(icon_path)



label = customtkinter.CTkLabel(master=root, text="THE RETRO GAMES",text_color="WHite",font=("arial",25,"bold"))
label.grid(row = 1, column=1 , padx=50 ,pady = 40)

frame = customtkinter.CTkFrame(master = root)
frame.grid(row = 2 , column=0 , padx=50 ,pady =10 )

frame1 = customtkinter.CTkFrame(master = root )
frame1.grid(row = 2 , column=1 , padx=0 ,pady =10 )

frame2 = customtkinter.CTkFrame(master = root , border_width= 0)
frame2.grid(row = 2 , column=2 , padx=0 ,pady =10 )

frame3 = customtkinter.CTkFrame(master = root , border_width= 0)
frame3.grid(row = 3 , column=0 , padx=0 ,pady =10 )

frame4 = customtkinter.CTkFrame(master = root , border_width= 0)
frame4.grid(row = 3 , column=1 , padx=0 ,pady =10 )

frame5 = customtkinter.CTkFrame(master = root , border_width= 0)
frame5.grid(row = 3 , column=2 , padx=0 ,pady =10 )

snake_image_path = os.path.join(current_directory,'snakelogo.jpg')
pong_image_path = os.path.join(current_directory,'pongcover.jpg')
tetris_image_path = os.path.join(current_directory,'tetris cover.jpg')
dinorun_image_path = os.path.join(current_directory,'dino run cover.jpg')
sinvader_image_path = os.path.join(current_directory,'spaceinvaders.jpg')
flappybird_image_path = os.path.join(current_directory,'flappy bird cover.jpg')

snake_image = customtkinter.CTkImage(Image.open(snake_image_path),size = (150,200) )
pong_image = customtkinter.CTkImage(Image.open(pong_image_path),size = (150,200))
tetris_image = customtkinter.CTkImage(Image.open(tetris_image_path),size = (150,200))
dinorun_image = customtkinter.CTkImage(Image.open(dinorun_image_path),size = (150,200))
sinvader_image = customtkinter.CTkImage(Image.open(sinvader_image_path),size = (150,200))
flappybird_image = customtkinter.CTkImage(Image.open(flappybird_image_path),size = (150,200))


snake_button = customtkinter.CTkButton(frame,text="", command=run_snake_game, height= 200 ,width= 100 ,image = snake_image ,anchor ="center",fg_color ="purple" ,hover_color ="dark blue",corner_radius = 0) 
snake_button.grid()

Ponggame_button = customtkinter.CTkButton(frame1, text="", command=run_Pong_game, height = 200 ,width=100,image = pong_image,fg_color = "purple",hover_color ="dark blue",corner_radius= 0 )
Ponggame_button.grid()

quiz_button = customtkinter.CTkButton(frame2, text="", command=run_Tetris_game,image = tetris_image ,height = 200 ,width=100,corner_radius= 0,fg_color = "purple",hover_color ="dark blue" )
quiz_button.grid()

empty1_button = customtkinter.CTkButton(frame3, text="", command=run_dinorun_game,image = dinorun_image , height = 200 ,width=100,corner_radius= 0,fg_color = "purple",hover_color ="dark blue" )
empty1_button.grid()

empty2_button = customtkinter.CTkButton(frame4, text="", command=run_spaceinvader_game,image = sinvader_image , height = 200 ,width=100,corner_radius= 0,fg_color = "purple",hover_color ="dark blue" )
empty2_button.grid()

empty3_button = customtkinter.CTkButton(frame5, text="", command=run_flappybird_game,image = flappybird_image , height = 200 ,width=100,corner_radius= 0,fg_color = "purple",hover_color ="dark blue" )
empty3_button.grid()


root.mainloop()
