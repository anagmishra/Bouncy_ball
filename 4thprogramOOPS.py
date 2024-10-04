import pgzrun
from random import randint

#Constants
TITLE="Bouncy Ball"
HEIGHT=500
WIDTH=500
BALL_RADIUS=35
GRAVITY=2000

CLR=(randint(0, 255), randint(0, 255), randint(0, 255))


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 200
        self.vy = 0
        self.uy = 0
        self.radius = BALL_RADIUS

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius,CLR)

    def update(self, dt):
        #Applying the constant acceleration formulae
        self.uy = self.vy
        self.vy += GRAVITY*dt
        self.y += (self.uy + self.vy)*0.5*dt

        #Detecting and handling the bounce
        if self.y>HEIGHT-self.radius:
            self.y = HEIGHT-self.radius
            self.vy = -self.vy*0.9 #Inelastic collision

        # X component does not have acceleration but it has constant velocity
        self.x += self.vx*dt
        if self.x>WIDTH - self.radius or self.x<self.radius:
            self.vx = -self.vx

bouncy_ball= Ball(25, 25)

def draw():
    screen.clear()
    bouncy_ball.draw()

def update(dt):
    bouncy_ball.update(dt)

def on_key_down(key):
    if key == keys.SPACE:
        bouncy_ball.vy = -500

pgzrun.go()