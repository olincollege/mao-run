import pygame
pygame.init()

# Initializing display surface
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Mao Run')

# Necessary to control frame rate for consistency across
# different devices
clock = pygame.time.Clock()

# Title
title_font = pygame.font.Font(None, 100)
title_surface = title_font.render('Mao Run', False, 'Brown')

# Test regular surface
sky_surface = pygame.Surface((800,300))
sky_surface.fill('Blue')

ground_surface = pygame.Surface((800,100))
ground_surface.fill('Green')

object_surface = pygame.Surface((50,50))
object_surface.fill('Red')
object_rect = object_surface.get_rect(midbottom = (300,300))

player_surface = pygame.Surface((50,50))
player_surface.fill('Black')
player_rect = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Formula: displace surface . blit (regular surface, position)
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(title_surface,(250,120))
    screen.blit(player_surface,player_rect)
    # Set object speed
    object_rect.x += 4
    if object_rect.left <= 0:
        object_rect.right = 800
    elif object_rect.right >= 800:
        object_rect.left = 0
    screen.blit(object_surface,object_rect)

    if player_rect.colliderect(object_rect):
        print('Collision')

    pygame.display.update()
    # While loop should not run faster than 60fps
    # Maximum frame rate
    clock.tick(60)

    # Adding image: .convert_alpha()