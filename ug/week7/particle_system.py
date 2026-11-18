from py5canvas import *
import numpy as np

class Particle:
    def __init__(self, lifetime=3.0):
        self.lifetime = lifetime
        self.life = self.lifetime
        self.reset()

    def reset(self):
        self.pos = np.array(mouse_pos)
        self.vel = np.zeros(2)
        angle = -PI/2 + np.random.uniform(-1, 1)*0.2
        self.acc = np.array([np.cos(angle), np.sin(angle)])*400*np.random.uniform(0.5, 1.0)
        self.life = self.lifetime
    
    def update(self, dt, force=np.zeros(2)):
        self.acc += force
        self.acc += Vector(0, 9.8) # Gravity
        self.vel += self.acc*dt 
        self.pos += self.vel*dt
        self.life -= dt
        if self.life <= 0:
            self.reset()

    def draw(self):
        fill(255, 255*(self.life/self.lifetime))
        circle(self.pos, 2)

particles = []

def setup():
    create_canvas(600, 600)
    no_stroke()
    frame_rate(60)
    noise_detail(1)


def draw():
    background(0, 10)

    # Create particles until we reach a maximum capacity of the list
    if len(particles) < 1000:
        particles.append(Particle())
    # Update and draw the particles
    for p in particles:
        # angle = remap(noise(p.pos*13.1233-[2, 3]), 0.0, 1.0, -np.pi*2, np.pi*2)
        # force = direction(angle)*20
        p.update(1.0/60) #, force)
        p.draw()

run()

