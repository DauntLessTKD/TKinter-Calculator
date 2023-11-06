<h1 align="center" id="title">TKinter-Calculator</h1>

<p id="description">Create a simple calculator using a library of graphical interfaces in python</p>

<h2>Project Screenshots:</h2>

<img src="https://drive.google.com/uc?export=download&id=1Edv5ZaFFNyje9SW0uQSRIks6snelpAbR" alt="project-screenshot" width="400" height="400">

<h2>🛠️ Installation Steps:</h2>

<p>1. Install tkinter</p>

```
pip install tk
```

<h2>💻 Built with</h2>

Technologies used in the project:

* Tkinter
* Python

```
<h2>Description</h2>
```

```
In this code: 

Import Statements: The tkinter library is imported to create the graphical user interface. 

Tkinter Window Creation: A Tk() object is created representing the main window of the application. The window's title is set to "Calculator". 

Entry Field: An entry field (e\_text) is created to display input and output. It's placed at the top of the window. 

Button Functions: 
click\_button(value): This function is called when a digit or operator button is clicked. It inserts the clicked value into the entry field. 
delete(): This function clears the entry field. operations(): This function evaluates the mathematical expression entered in the entry field and displays the result. If a division by zero occurs it displays "infinite" for a few seconds and then clears the entry field. 

Buttons: Buttons for digits 1 to 9 operations and special characters like parentheses period and equals sign are created. Each button is associated with a click\_button() function using the command parameter. 

Grid Layout: The buttons are placed in the window using the grid() method defining their positions in rows and columns. 

Main Loop: The window.mainloop() function starts the Tkinter main event loop allowing the application to respond to user interactions.
```
