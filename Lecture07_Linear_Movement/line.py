from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    # fill here
    global running
    global x, y
    global remx, remy
    global px, py
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT -1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            remx, remy = event.x - 25, KPU_HEIGHT - 1 - event.y + 25

    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image("KPU_GROUND.png")
mouse = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
x = KPU_WIDTH // 2
y = KPU_HEIGHT // 2
px = KPU_WIDTH // 2
py = KPU_HEIGHT // 2
frame = 0
dir = 3
remx = px
remy = py
hide_cursor()

while running:
    cx=(remx-px)/30
    cy=(remy-py)/30
    px+=cx
    py+=cy

    if remx-px < 0:
        dir = 0
    elif remx-px > 0:
        dir = 1
    elif remx-px == 0:
        dir = 3

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.draw(x, y)
    character.clip_draw(frame * 100, 100*dir, 100, 100, px, py)
    update_canvas()
    frame = (frame + 1) & 8
    delay(0.01)
    handle_events()

close_canvas()