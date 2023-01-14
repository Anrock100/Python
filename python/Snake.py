from tkinter import *
import random

Game_width = 500
Game_height = 500
Speed = 140
Space_size = 20
Body_parts = 3
Snake_color = "white"
Food_color = "red"
Background_color = "black"


class Snake:
    def __init__(self) -> None:
        self.body_size = Body_parts
        self.coordinates = []
        self.squares = []

        for i in range(0, Body_parts):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_oval(x, y, x + Space_size, y + Space_size, fill=Snake_color, tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self) -> None:
        x = random.randint(0, (Game_width/Space_size)-1) * Space_size
        y = random.randint(0, (Game_height/Space_size)-1) * Space_size

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + Space_size, y + Space_size, fill=Food_color, tag="food")


def next_turn(snake, food):
    
    x , y = snake.coordinates[0]

    if direction == "up":
        y -= Space_size

    elif direction == "down":
        y += Space_size

    elif direction == "left":
        x -= Space_size

    elif direction == "right":
        x += Space_size

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_oval(x, y, x + Space_size, y + Space_size, fill=Snake_color) #snake head
    
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()

    else:

        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()

    else:
        window.after(Speed, next_turn, snake, food)


def change_direction(new_direction):
    
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collision(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= Game_width:
        return True
    
    elif y < 0 or x >= Game_height:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False
    

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("consolas", 70), text="Game Over", fill="red", tag="gameover")


window = Tk()
window.title("Sunway Snake Game")

#window.resizable(False, False) #to fix the screen size
score = 0
direction = "down"

label = Label(window, text = "Score:{}".format(score), font=("consolas", 40))
label.pack()

canvas = Canvas(window, bg=Background_color, height= Game_height, width= Game_width)
canvas.pack()

window.update()

window_width= window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

#window.geometry(f"{window_width} * {window_height} + {x} + {y}") # should not be float

window.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y)) # to centralize the opening screen


#controls

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('a', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('d', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('w', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('s', lambda event: change_direction('down'))


snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()