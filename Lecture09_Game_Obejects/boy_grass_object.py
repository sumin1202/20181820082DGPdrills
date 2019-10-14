from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image=load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 800), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball_small:
    def __init__(self):
        self.x, self.y = random.randint(50, 800), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        r1_y = random.randint(7, 15)
        self.y -= r1_y


    def draw(self):
        if(self.y<65):
            self.image.draw(self.x, 65)
        else:
            self.image.draw(self.x, self.y)

class Ball_big:
    def __init__(self):
        self.x, self.y = random.randint(50, 700), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        r2_y = random.randint(10, 25)
        self.y -= r2_y



    def draw(self):
        if (self.y < 70):
            self.image.draw(self.x, 70)
        else:
            self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

team = [Boy() for i in range(11)]
ns = random.randint(7, 12)
ball_s = [Ball_small() for i in range(ns)]
ball_b = [Ball_big() for i in range(20-ns)]
grass = Grass()

running = True
# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()
    for bs in ball_s:
        bs.update()
    for bs in ball_b:
        bs.update()

    clear_canvas()

    grass.draw()
    for boy in team:
        boy.draw()
    for bs in ball_s:
        bs.draw()
    for bs in ball_b:
        bs.draw()
    update_canvas()

    delay(0.04)

# finalization code
close_canvas()