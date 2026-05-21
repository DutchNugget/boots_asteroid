import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0.0



    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers= (updatable)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    
    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)
        

        updatable.update(delta_time)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            pass

        pygame.display.flip()
        delta_time = clock.tick(60) / 1000.0
        
        
  
if __name__ == "__main__":
    main()  