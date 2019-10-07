from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    # fill here
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT -1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image("KPU_GROUND.png")
mouse = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y = 800 // 2
frame = 0
dir = 0
randx, randy = random.randrange(10, KPU_WIDTH), random.randrange(10, KPU_HEIGHT)

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.clip_draw(frame * 100, 0, 100, 100, x, y)
    character.clip_draw(frame * 100, 0, 100, 100, randx, randy)
    update_canvas()
    handle_events()
    frame = (frame + 1) & 8
    x += dir * 5
    delay(0.01)

close_canvas()