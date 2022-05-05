import pygame
import sys
from random import choice
from obstacle import Obstacle

class Game:

    POSSIBLE_OBSTACLES = ["spades", "diamonds", "hearts", "clubs"]
    score = 0

    def __init__(self, obstacle_actions):
        self._round_over_called = False
        self._game_over_called = False
        self._obstacle_actions = obstacle_actions
    
    @property
    def round_over_called(self):
        return self._round_over_called

    @property
    def game_over_called(self):
        return self._game_over_called

    @property
    def obstacle_actions(self):
        return self._obstacle_actions
    
    def round_over(self):
        """"
        Demonstrate that the round is over.
        """
        self._round_over_called = True
    
    def game_over(self):
        """"
        Demonstrate that the game is over.
        """
        self._game_over_called = True

    def exit_window(self, event):
        """
        Allow the user to turn off the game windown when clicking the
        'X' button.

        Args:
            event: 
        """
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    def press_any_arrow_key(self, event):
        """
        Check if the player is pressing one of the arrow keys.
        Args:
            event: 

        Returns
            A boolean statement representing whether the correct key is pressed.
        """
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP 
                or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or
                event.key == pygame.K_RIGHT):
            return True
        return False

    def check_continue(self, control, obstacle):
        """
        Check whether the game should continue.

        If the user presses the correct key, the game continues.
        If not, round_over is called and the game restarts.

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
            self.exit_window(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game_over()
            self.exit_window(event)
            # determine whether the user pressed the correct key
            pressed_correct_key = control.interpret_input(event, obstacle.action)

            # if a key is pressed and the key is the correct key, return a new
            # obstacle instance
            if event.type == pygame.KEYDOWN:
                if pressed_correct_key:
                    self.score += 1
                    # print(self.score)
                    print(obstacle.sprite)
                    return Obstacle(choice(self.POSSIBLE_OBSTACLES), self.obstacle_actions)
                else:
                    self.round_over()
        
        # If the obstacle collides with the player, end the game
        if control.check_collision(obstacle):
            self.round_over()
        
        # Return the obstacle instance entered as an argument if no keys were pressed
        return obstacle
