# Our game’s vision

Mao Run is a 2D platformer game with only 1 rule: _We don’t talk about the rules._ The player has to figure out what to do with whatever visual cues provided to them on screen. Our goal is to be as infuriating as possible while keeping a certain level of enjoyment and dopamine for players to fixate on continuing.

In a way, despite its non-educative appearance and inherent silliness, Mao Run embodies the ultimate life lesson: _“You live and you learn.”_ Sometimes, what you need to do is to “just 
go for it”. As long as you have a chance to correct yourself, the possibility for trial and error (and eventual improvement) is endless. We hope you have good luck in diving headfirst into whatever the task that made you hesitant is. Meanwhile, ***enjoy our game!***

# Preview
_Technically, you shouldn’t view this section to enjoy the full game experience._
- - - 
Below is the demonstration video for Mao Run.
[![Demonstration Video](https://i.ibb.co/CHDvSPq/mao-run-start-screen.png)](https://youtu.be/HAZj4FIPxYA "Mao Run")
### Image of Mao Run Game
After the game has begun, obstacles, such as the club below, appear and the player must figure out what to do to continue playing the game.
![In-game Screen](https://i.ibb.co/kgF1TvS/mao-run-image.jpg)
- - - 
## FEATURES
### BEAUTIFUL PIXEL INTERFACE
* Simulates a nostalgic atmosphere that brings you back to the age of arcade games. Mao Run (2022) aims to achieve the simple visuals presented in games like Space Invaders (1978) and Pac-Man (1980), which provide a compelling game environment that draws you in without the addition of convoluted computer graphics.

### RANDOM KEY ASSIGNMENT
* Keeping our game captivating at its core is the random key assignment function. Written using Python’s [random](https://docs.python.org/3/library/random.html) library. The function would assign each of the 4 different user inputs: `pygame.K_UP` `pygame.K_DOWN` `pygame.K_LEFT` `pygame.K_RIGHT` to each obstacle for every new instance of the game. To proceed with the game, the player is expected to fail the first few times to figure out which key corresponds to which obstacle,

### RANDOM SPEED CHANGES
* **NEW FEATURE** When players start to understand the game’s implied logic and assignments, some complain that the game begins to feel slow and rather _boring_. As a team, we value our consumers’ interests and concerns. Case in point, in response to the aforementioned feedback, we promptly deliver a new feature: **RANDOM SPEED CHANGES**.
As you, the player, get to a certain level of proficiency in maneuvering the game, **RANDOM SPEED CHANGES** will be called into action, keeping you on your toes by randomly speeding up the impending obstacles.

# Try it yourself!

## Installation instructions for [Mao Run](https://github.com/olincollege/mao-run)
1. Clone the repository.<br>
    `git clone https://github.com/olincollege/mao-run.git`
2. Navigate to the local repository using your terminal.<br>
    ex: `cd mao-run`
3. Install the dependencies listed below if they are not already installed.

## Dependencies
This project relies upon the following dependency:
* Pygame
    * To install, run the following line in terminal <br>`pip install pygame`

## Play the game 
* After navigating to the local repository in the terminal, run the following line to start the game:
`python3 main.py`
* To start the game, press one of the arrow keys to move past the introduction screens.
* Since the rules of the game are purposefully unknown, simply press an arrow key and hope for the best.
* If you want to exit the game, press the `esc` key.

# About Us
### [Lili Baker](https://github.com/lilibaker)
*Back End Software Developer*
<img src="https://i.ibb.co/NYgGQ34/lili-baker.png" alt="lili-baker" width="20%" height="20%" border-right="2%" style="float:left">
* "I would rather be reading right now, but here we are 😓"
* Patiently generated and delivered all test functions
* Diligently fill up every needed spot in the code
<br><br>
### [Cherry Pham](https://github.com/cherryyypham)
*Back End Software Developer*
<img src="https://i.ibb.co/1Lb2fpz/cherry-pham.png" alt="cherry-pham" width="20%" height="20%" border-right="2%" style="float:left">
* "Can you do it again 🥺👉👈"
* Adaptively employ all Pygame implementations
* Meticulously ensure the project's quality
<br><br>
### [Vaani Bhatnagar](https://github.com/vaanibhatnagar)
*UI/UX Designer*
<img src="https://i.ibb.co/zRdXtLX/vaani-bhatnagar.png" alt="vaani-bhatnagar" width="20%" height="20%" border-right="2%" style="float:left">
* "I'm so hungry 😩🍗🍞🧀"
* Skillfully produce adorable sprite designs and eye-catching color scheme
* Effectively incorporated critiques into design process
<br><br>
# References
Mao Run is inspired by the underlying concepts of the card game [Mao](https://www.wikihow.com/Play-Mao), in which all players except the gamemaster do not know the rules of the game. The particpants learn the unspoken rules whilst playing the game, which is similar to how Mao Run (2022) works.