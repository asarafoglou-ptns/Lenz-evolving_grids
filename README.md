# Evolving Grids

Version 1.0.0

Evolving Grids is a dynamic Python application that allows you to experience Conway's Game of Life on your device. This interactive app provides a range of features to enhance your gameplay and experimentation with cellular automata:

* Interactive Grid: Click on the grid to bring cells to life or to kill them.
* Adjustable Grid Size: Customize the size of the game grid to your preference.
* Variable Simulation Speed: Control the speed of the simulation, making it run faster or more slowly according to your needs.
* Pause and Edit: Pause the simulation at any time to make adjustments to your cell setup.
* Responsive Design: The elements are automatically scaled to fit the size of your screen for optimal viewing and interaction.

In addition to the main gameplay features, the codebase includes a number of Python functions designed for grid manipulation. These functions can be valuable for developers who are interested in working with grids, offering a versatile toolkit for their own projects.

Evolving Grids was developed for the the course 'Programming: The Next Step' at University of Amsterdam.
Check it out here: https://github.com/asarafoglou-ptns/Lenz-evolving_grids

## Limitations

- The speed of the simulation decreases and the simulation might get laggy the bigger the size of the grid (due to the workings of Shiny for Python)

## Contents of the Report

1. Scenario
2. Flowchart
3. Screenshots of the app
4. How to for users

   4.1 How to install and run the app

   4.2 How to use the app

   4.3 How to use an exemplary function from the package

### 1. Scenario

__Purpose:__ Scenario that describes the purpose, use and functionalities of the evolving_grids package.

__Individual:__ A university student at the UvA, in the first year of their Master’s.

__Equipment:__ A laptop or computer with Python installed, along with the evolving_grids package and its dependencies (shiny, htmltools, uvicorn, and starlette).

__Scenario:__ A student is bored during class and decides to play Conway’s Game of Life on their laptop to pass the time until the break.

1. The student downloads the evolving_grids package from GitHub and runs the software on their laptop.
2. They read the instructions and rules of the game at the top of the page.
3. The student changes the size of the grid so that it fits the size of their laptop screen by entering the number of rows and columns they want the grid to have in the corresponding input fields.
4. The student starts playing by clicking on the grid to bring some cells to life.
5. Then, the student starts the simulation by clicking on the start button.
6. The student watches the simulation for a while, then clicks ‘pause’.
7. The student makes some changes to their configuration of alive cells by clicking on the grid to bring some more dead cells to life and kill some of the alive ones.
8. Then, the student clicks ‘start’ again to resume the simulation.
9. The student speeds up the simulation using the speed-slider to watch the simulation evolve more quickly.
10. After a while, the simulation is caught in a perpetual cycle of patterns, so the student clicks reset to return the grid to its original blank state.
11. It’s time for the break, so the student stops the software and closes their laptop.


### 2. Flowchart
![flowchart_final_report](https://github.com/asarafoglou-ptns/Lenz-evolving_grids/assets/123644916/7e09470f-464e-43e5-a6b9-97d36e07e1d9)



### 3. Screenshots of the app
#### The UI
The following screenshot shows the entire app (how it looks when you run and open it). At the top of the page, there is some information about the app itself and Conway's Game of Life. Below the rules of the game, there are some instructions for how to use the app to play the game. At the bottom left of the page, there is a control panel and at the bottom right, there is the game grid.

<img width="602" alt="full_page" src="https://github.com/asarafoglou-ptns/Lenz-evolving_grids/assets/123644916/c1c9fb1f-4fc1-4949-a8dc-8911849731cc">

### 4. How to for users
#### 4.1 How to install and run the app
In the following, I will illustrate the steps you need to take to download and run the app on your laptop. 

__1__ Make sure that Python is installed on your computer. If you haven't installed Python yet, you can do it here: https://www.python.org/downloads/

__2__ Install the evolving_grids package using the following command:
````sh
pip install evolving_grids@git+https://github.com/asarafoglou-ptns/Lenz-evolving_grids.git#egg=evolving_grids
````

Now the package is installed on your computer under the name _app_. Before we proceed, here is an explanation of the contents of the package:

Within the _app_ folder, you can find all the code for the shinyapp. Let me run you through the individual files:
* folder `static`, which contains static files, like the stylesheet (`ui.css`) and the .png files used in this README
* several files with code:
    * `__init__.py` indicates to Python that the directory is a Python package
    * `app.py` contains the code for user interface and background processes of the app
    * `grid_functions.py` basic functions required to create and (later) update the game grid
    * `logic_functions.py` functions for implementing the game logic
    * `run.py`  setup for running an ASGI (Asynchronous Server Gateway Interface) application using the Uvicorn server
    * `shiny_extensions.py` extensions to the standard Shiny for Python to make the app work

__3__ Next, you need to find out where exactly you installed the package. You can do this by typing
````python
pip show evolving_grids
````
in your terminal. This will give you something like this:
````python
>> Name: evolving_grids
>> Version: 1.0
>> Summary: A Python package for playing Conway´s Game of Life
>> Home-page:
>> Author: sarah_lenz
>> Author-email: sarah.lenz@student.uva.nl
>> License: MIT
>> Location: C:\Users\sarah\AppData\Local\Programs\Python\Python312\Lib\site-packages
>> Requires: htmltools, shiny, starlette, uvicorn
>> Required-by:
````

__4__ Copy the path that indicates the location of the package (in this example `C:\Users\sarah\AppData\Local\Programs\Python\Python312\Lib\site-packages`).

__5__ Change the directory to the _app_ folder within `C:\Users\sarah\AppData\Local\Programs\Python\Python312\Lib\site-packages` using 
````python
cd C:\path\to\...\app
````
(make sure to __insert the path__ to the package on your computer and to __add \app__ at the end of the path).

__6__ Now you can start the app by running
````python
python run.py
````
in your terminal. Now, there should appear a link (something like `http://127.0.0.1:8000`). Clicking on this link should open the app in your browser.


#### 4.2 How to use the app

##### The Grid
As explained above, the __game grid__ is located at the bottom right of the page. To play Conway's Game of Life, you first need to bring some of the cells to life by clicking on them. Alive cells are marked in orange, dead cells are white.

<img width="696" alt="alive_grid" src="https://github.com/asarafoglou-ptns/Lenz-evolving_grids/assets/123644916/d75ae939-9113-4470-8bd3-edbc25b68db7">


##### The Controls
At the top of the control panel, there is a __start and a reset button__. Clicking on 'start' starts the simulation. While the simulation is running, the inscription of the 'start' button switches to 'pause'. Clicking on 'pause' halts the simulation. It is now possible to make adjustments to the configuration of alive and dead cells. Clicking 'start' again resumes the simulation, while pressing 'reset' resets the grid to its original blank state.

![controls_buttons](https://github.com/asarafoglou-ptns/Lenz-evolving_grids/assets/123644916/3e5addb9-5488-43d6-be5e-8e5fd7c3dd48)


Below the 'start/pause' and 'reset' buttons, there is a __slider__ with which you can adjust the __speed of the simulation__. '1' indicates the lowest, '10' the highest possible speed.

![controls_speed](https://github.com/asarafoglou-ptns/Lenz-evolving_grids/assets/123644916/080e8a72-4acb-4d2f-bd63-f7ec502956e3)


At the bottom of the control panel, there are two input fields for __adjusting the size of the grid__. You can specify the number of rows and columns you want the grid to have. The maximum possible number of rows is 35 and the maximum possible number of columns is 50. To set the grid size, press 'set grid size'.

![controls_size](https://github.com/asarafoglou-ptns/Lenz-evolving_grids/assets/123644916/3dd27b96-30a1-4e0b-ad56-d1f5f6495282)


#### 4.3 How to use an exemplary function from the package
The evolving_grids package contains several functions, which are required to run the app. Strictly, none of these functions is intended to be used by the users of the app. However, one of the course requirements is that one of the functions from the package needs to be usable. Therefore, I chose `create_new_generation()` as an exemplary function from the package and made it available for users.
Please follow the steps outlined below to use the `create_new_generation()` function (please note that you need to install the package on your computer before following the steps outlined below. If you haven't done so already, please follow steps 1 and 2 from the section _How to install and run the app_ before trying to use the function):

__1__ If the app is still running, stop the app in the terminal (using Strg+C or Ctrl+C).

__2__ If Python is still active in your terminal, exit python by typing 
````python
exit()
````
Otherwise, move on to step 3.

__3__ Now, navigate back to the directory in which your _app_ folder lives using `cd` and the path to the package - again, you get the path by typing
````sh
pip show evolving_grids
````
and copying the path reference (see step 3 and 4 from _How to install and run the app_ for more detailed explanations).

__4__ Start Python by typing 
````sh
python
`````
in your console.

__5__ Now, import the function by typing 
````python
from app import create_new_generation
````

__6__ The create_new_generation() function takes one argument: a grid with 1s and 0s of any size. To test the function, you therefore need to set up a grid with only 1s and 0s and pass this grid to the function. You can set up a random 5x5 grid with 1s and 0s using the following code (feel free to adapt the code so that you have bigger or smaller grids):
````python
import random

def generate_grid(rows, cols):
    grid = []
    for _ in range(rows):
        row = [random.choice([0, 1]) for _ in range(cols)]
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

rows = 5
cols = 5
grid = generate_grid(rows, cols)

print(grid)
````
__7__ Pass your grid to the create_new_generation() function (`create_new_generation(grid)`). The function then returns a new grid with 0s and 1s indicating which of the cells in your grid stays alive/comes alive or dies in the next generation according to the game rules.

If there are any issues, suggestions or fixes required for the app, please don't hesitate to reach out through github.

-----------------------
Sarah Lenz,
University of Amsterdam
