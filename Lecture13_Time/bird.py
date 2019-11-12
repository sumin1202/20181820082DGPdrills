from pico2d import *
import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 60.0   # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 250
        self.image = load_image('bird_animation.png')
        self.size_x, self.size_y = 182, 167
        self.dir = 1
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        if self.dir == 1:
            self.x += RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == 0:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time

        if self.x < 0:
            self.dir = 1
        if self.x > 1600:
            self.dir = 0

        pass

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame % 5) * self.size_x, int(self.frame / 5) * self.size_y+self.size_y,
                                           self.size_x, self.size_y, math.radians(0), '', self.x, self.y,
                                           self.size_x, self.size_y)
        elif self.dir == 0:
            self.image.clip_composite_draw(int(self.frame % 5) * self.size_x, int(self.frame / 5) * self.size_y+self.size_y,
                                           self.size_x, self.size_y, math.radians(180), 'v', self.x, self.y,
                                           self.size_x, self.size_y)

    def handle_event(self, event):
        pass
