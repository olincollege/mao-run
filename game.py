import pygame
import sys
from random import choice
from obstacle import Obstacle
from world import MaoRun

class Game:

    actions = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_DOWN]
    possible_obstacles = ["spades", "diamonds", "hearts", "clubs"]

    def __init__(self):
        self._obstacle_actions = {
            "spades": choice(self.actions),
            "diamonds": choice(self.actions),
            "hearts": choice(self.actions),
            "clubs": choice(self.actions),
        }
    
    @property
    def obstacle_actions(self):
        return self._obstacle_actions
    
    def game_over(self):
        """"
        Demonstrate that the game is over.

        Update the screen to demonstrate the game is over.
        """
        print("game over")
        pygame.quit()
        sys.exit()
        # create a method in world that will display game over when called

    def check_continue(self, control, obstacle):
        """
        Check whether the game should continue.

        If the user presses the correct key, the game continues.
        If not, game_over is called and the game restarts.

        Args:
            control: An ObstacleController instance for the current game.
            obstacle: An obstacle instance that is the current obstacle
                on the screen.
        
        Returns:
            An obstacle instance that is the same as the argument if the game
            is not over and the key is pressed, or is a new random obstacle if
            the correct key was pressed.
        """
        for event in pygame.event.get():
            # if the user tries to exit the window, end the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # determine whether the user pressed the correct key
            pressed_correct_key = control.interpret_input(event, obstacle.action)

            # if a key is pressed and the key is the correct key, return a new
            # obstacle instance
            if event.type == pygame.KEYDOWN and pressed_correct_key:
                print(obstacle.sprite)
                return Obstacle(choice(self.possible_obstacles), self.obstacle_actions)
        
        # if the obstacle collides with the player, end the game
        if control.check_collision(obstacle):
            self.game_over()
        
        # return the obstacle instance entered as an argument if no keys were pressed
        return obstacle

