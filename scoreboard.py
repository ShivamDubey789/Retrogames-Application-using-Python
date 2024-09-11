from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",15,"bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}   HIGHSCORE: {self.high_score}",align ="center",font=FONT)




    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align =ALIGNMENT,font=FONT)


    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
     
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score() 
        self.score = 0
        self.update_scoreboard()

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))
    

        