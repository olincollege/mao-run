# mao-run
A game in which the rules are unknown.

## Dependencies
* pygame

## Notes
good key pressed example: https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-tutorial-movement/

## The big idea or goal of the project

---

(Write things and stuff here)


## Unique features of your project

---
#### Mechanics
![Brailldle Mechanics Breakdown](https://i.ibb.co/qxzfz3b/mechanics-breakdown.png)

_Sketch of Brailldle mechanics_
##### The braille display is composited of 5 components:
1. Pen push buttons: we figured that the pen push buttons are perfect as braille dots.
2. Cell base (acrylic)
3. Servo motor: each corresponds to a braille dot.
4. Wooden rod
5. Cam

In their resting position, the braille dots (pen push buttons) lay under the cell base. As each servo receives a signal to turn 180º, it would turn the wooden rod connected to the cam. The cam would push the braille dot right on top of it past a hole in the cell base. Each letter would take 5 seconds to refresh.

#### Braille Cell
The **braille cell** consists of a **body** with all the mechanics and a **case** to store the body.

![Braille Cell Body](https://i.ibb.co/tH85Rzw/braille-cell-body.png)

_CAD model for the body of the braille cell_

![Braille Case](https://i.ibb.co/9c2kYvK/braille-case.png)

_CAD model for the case of the braille cell_

#### Electrical and Programming
![Circuit Diagram](https://i.ibb.co/TMjH0zx/circuit.jpg)

_Circuit diagram for the servos_

Through a camera, we can acquire the image of text. Using _Pytesseract_, we extract the text from the image and run our _Arduino_ file, which converts the text to braille and regulates servos to raise dots on our braille cell.

#### Pseudocode
![Pseudocode](https://i.ibb.co/Pc09qkQ/Screenshot-17.png)

## Try it yourself!


---

### Installation instructions
- Grainy camera
- Servos loop does not terminate (Arduino//servo error)
- Interface error (Camera not showing//Tkinter)

### Download links for your project
- Early idea forming and realistic planning
- Using a camera to read text
- Teamwork, delegation

### A link to your project’s GitHub page
- Pytesseract
- Tkinter
- Arduino configuration

## About Us

---
(Things)
