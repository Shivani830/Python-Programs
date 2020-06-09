"""
File: brickbreaker.py
----------------
YOUR DESCRIPTION HERE
"""

import tkinter
import time
import random

# How big is the playing area?
CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 800     # Height of drawing canvas in pixels

# Constants for the bricks
N_ROWS = 8              # How many rows of bricks are there?
N_COLS = 10             # How many columns of bricks are there?
SPACING = 5             # How much space is there between each brick?
BRICK_START_Y = 50      # The y coordinate of the top-most brick
BRICK_HEIGHT = 20       # How many pixels high is each brick
BRICK_WIDTH = (CANVAS_WIDTH - (N_COLS+1) * SPACING ) / N_COLS

# Constants for the ball and paddle
BALL_SIZE = 40
PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 80


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Brick Breaker')
    create_bricks(canvas)
    ball = add_ball(canvas)
    paddle = canvas.create_rectangle(0, CANVAS_HEIGHT-130, PADDLE_WIDTH, CANVAS_HEIGHT - 110, fill="black")
    change_x = 8
    change_y = 8
    chances_consumed = 0
    bricks_remaining = N_COLS*N_ROWS
    while chances_consumed <= 3 and bricks_remaining > 0:
        mouse_x = canvas.winfo_pointerx()
        canvas.moveto(paddle, mouse_x, CANVAS_HEIGHT - 130)
        canvas.move(ball, change_x, change_y)
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            change_x *= -1
        elif hit_paddle(canvas, paddle):
            change_y *= -1
        elif hit_brick(canvas, ball):
            colliding_list = find_colliding_list(canvas, ball)
            for shape in colliding_list:
                if shape == ball:
                    pass
                else: 
                    canvas.delete(shape)
                    bricks_remaining -= 1
            change_y *= -1
        elif hit_top_wall(canvas, ball):
            change_y *= -1
        elif hit_bottom_wall(canvas, ball):
            chances_consumed += 1
            change_y *= -1

        canvas.update()
        time.sleep(1/50)

    if chances_consumed > 3:
        canvas.create_text(CANVAS_WIDTH/2 - 180, CANVAS_HEIGHT/2 - 100, text="GAME OVER!!!", anchor='w', font='Courier 40', fill='red')
    else:
        canvas.create_text(CANVAS_WIDTH/2 - 180, CANVAS_HEIGHT/2 - 100, text="YOU WON !!", anchor='w', font='Courier 40', fill='red')
    canvas.update()
    time.sleep(1/50)
    canvas.mainloop()


def create_bricks(canvas):
    x1_start = 6
    x2_start = 6 + BRICK_WIDTH
    y1 = BRICK_START_Y
    y2 = BRICK_START_Y + BRICK_HEIGHT
    x1 = x1_start
    x2 = x2_start
    for row in range(N_ROWS):
        for col in range(N_COLS):
            if row == 0 or row == 1:
                color = 'red'
            if row == 2 or row == 3:
                color = 'orange'
            if row == 4 or row == 5:
                color = 'yellow'
            if row == 6 or row == 7:
                color = 'cyan'
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            x1 = x2 + SPACING
            x2 = x1 + BRICK_WIDTH
        y1 = y2 + SPACING
        y2 = y1 + BRICK_HEIGHT
        x1 = x1_start
        x2 = x2_start


def add_ball(canvas):
    x1 = CANVAS_WIDTH / 2 - BALL_SIZE / 2
    y1 = CANVAS_HEIGHT / 2 - BALL_SIZE / 2
    x2 = CANVAS_WIDTH / 2 + BALL_SIZE / 2
    y2 = CANVAS_HEIGHT / 2 + BALL_SIZE / 2
    ball = canvas.create_oval(x1, y1, x2, y2, fill='black', outline='black')
    return ball


def get_left_x(canvas, shape):
    return canvas.coords(shape)[0]


def get_top_y(canvas, shape):
    return canvas.coords(shape)[1]


def get_right_x(canvas, shape):
    return canvas.coords(shape)[2]


def get_bottom_y(canvas, shape):
    return canvas.coords(shape)[3]


def hit_left_wall(canvas, ball):
    return get_left_x(canvas, ball) <= 0


def hit_right_wall(canvas, ball):
    return get_right_x(canvas, ball) >= CANVAS_WIDTH


def hit_bottom_wall(canvas, ball):
    return get_bottom_y(canvas, ball) >= CANVAS_HEIGHT


def hit_top_wall(canvas, ball):
    return get_top_y(canvas, ball) <= 0


def hit_paddle(canvas, paddle):
    paddle_coords = canvas.coords(paddle)
    x1 = paddle_coords[0]
    y1 = paddle_coords[1]
    x2 = paddle_coords[2]
    y2 = paddle_coords[3]
    result = canvas.find_overlapping(x1, y1, x2, y2)
    return len(result) > 1


def hit_brick(canvas, ball):
    colliding_list = find_colliding_list(canvas, ball)
    return len(colliding_list) > 1


def find_colliding_list(canvas, ball):
    ball_coords = canvas.coords(ball)
    x1 = ball_coords[0]
    y1 = ball_coords[1]
    x2 = ball_coords[2]
    y2 = ball_coords[3]
    return canvas.find_overlapping(x1, y1, x2, y2)


def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()
