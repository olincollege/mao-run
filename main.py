import sys
import pygame

from world import MaoRun
import game
import character
import obstacle
import controller

if __name__ == '__main__':
    pygame.init()

    # Initialize world
    CUR_WORLD = MaoRun()
    # Initialize player

    # Initialize obstacles

    # Initialize controller

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        CUR_WORLD.display()