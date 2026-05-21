import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import random
from logger import log_event

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw (self, screen):
         pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)
    
    def update (self, delta_time):
        self.position += self.velocity * delta_time

    def split (self):
        pygame.sprite.Sprite.kill(self)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            new_vector = random.uniform(20, 50)
            Asteroid_oneV = pygame.math.Vector2.rotate(self.velocity, new_vector)
            Asteroid_twoV = pygame.math.Vector2.rotate(self.velocity, -new_vector)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            newAS1 = Asteroid(self.position.x, self.position.y, new_radius)
            newAS1.velocity = Asteroid_oneV * 1.2
            newAS2 = Asteroid(self.position.x, self.position.y, new_radius)
            newAS2.velocity = Asteroid_twoV * 1.2




    
