# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import * # Import everything from constants.py
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.get_init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0 

    while True: # Starts game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # Stops game loop if game window is closed
        
        for obj in updateable: # Updates objects position
            obj.update(dt)

        for ast in asteroids:
            if player.collides(ast):
                #print("Game over!")
                sys.exit("Game over!")
        
        screen.fill("black") # Fills game window with solid black colour

        for obj in drawable: # Draws objects on screen
            obj.draw(screen)

        pygame.display.flip() # Refreshes screen
        dt = clock.tick(60)/1000 # This limits the framerate
        

if __name__ == "__main__":
    main()
