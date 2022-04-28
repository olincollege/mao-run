import pygame

import world
import game
import character
import obstacle
import controller

def main():
    # Start pygame
    pygame.init()

    # Initialize a world instance
    cur_world = world.World()

    # Initializing display surface
    screen = pygame.display.set_mode((800,400))

    # Name window
    pygame.display.set_caption('Mao Run')

    # Initialize a player instance
    player = pygame.sprite.GroupSingle()
    player.add(character.Character())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # Formula: displace surface . blit (regular surface, position)
        screen.blit(cur_world.sky_surface,(0,0))
        screen.blit(cur_world.ground_surface,(0,300))
        screen.blit(cur_world.title_surface,(250,120))

        # screen.blit(cur_world.player_surface,cur_world.player_rect)
        player.draw(screen)

        # # Set object speed
        # cur_world.object_rect.x += 4
        # if cur_world.object_rect.left <= 0:
        #     cur_world.object_rect.right = 800
        # elif cur_world.object_rect.right >= 800:
        #     cur_world.object_rect.left = 0
        # screen.blit(cur_world.object_surface,cur_world.object_rect)

        pygame.display.update()
        # While loop should not run faster than 60fps
        # Maximum frame rate
        cur_world.clock.tick(60)