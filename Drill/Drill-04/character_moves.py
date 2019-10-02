from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')
character2 = load_image('animation_sheet.png')

isDone = True

x = 0
frame = 0
while True:
    clear_canvas()
    grass.draw(400, 30)
    if isDone:
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame+1) % 8
        x += 5
        if x >= 800:
            isDone = False
    else:
        character2.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        if x <= 0:
            isDone = True
    delay(0.05)
    get_events()

close_canvas()