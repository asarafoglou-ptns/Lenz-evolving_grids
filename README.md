# Evolving Grids

Python app with which you can play Conway's Game of Life (for the course 'Programming: The Next Step' at University of Amsterdam).
Check it out here: https://github.com/asarafoglou-ptns/Lenz-evolving_grids

Version 1.0.0

- Evolving Grids allows you to play Conway's Game of Life on your device
- You can bring cells alive/kill them by clicking on the grid
- You can adjust the size of the game grid
- You can adjust the speed of the simulation to make it run faster or more slowly
- You can pause the simulation and make adjustments to your cell-setup
- The elements are automatically scaled to the size of your screen

## Limitations

- The speed of the simulation decreases and the simulation might get laggy the bigger the size of the grid (due to the workings of Shiny for Python)

## Contents of the Report

1. Scenario
2. Flowchart
3. Screenshots of the app
4. How to install and use the app

### 1. Scenario

__Purpose:__ Scenario that describes the purpose, use and functionalities of the evolving_grids package.

__Individual:__ A university student at the UvA, in the first year of their Master’s.

__Equipment:__ A laptop or computer on which Python, the evolving_grids package and the dependencies listed in `requirements.txt` are installed.

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

![flowchart_final_report.png](app\static\flowchart_final_report.png)


### 3. Screenshots of the app
#### The UI
The following screenshot shows the entire app (how it looks when you run and open it). At the top of the page, there is some information about the app itself and Conway's Game of Life. Below the rules of the game, there are some instructions for how to use the app to play the game. At the bottom left of the page, there is a control panel and at the bottom right, there is the game grid.

![full_page.png](app\static\full_page.png)


### 4. How to install and use the app
#### Installing and running the app
In the following, I will illustrate the steps you need to take to download and run the app on your laptop. 

__1__ Make sure that Python is installed on your computer. If you haven't installed Python yet, you can do it here: https://www.python.org/downloads/

__2__ Download the `evolving_grids-1.0-py3-none-any.whl` file from my github repository (https://github.com/asarafoglou-ptns/Lenz-evolving_grids/blob/week-3/dist/evolving_grids-1.0-py3-none-any.whl).

__3__ Locate the downloaded `evolving_grids-1.0-py3-none-any.whl` file on your computer and copy the file path.

__4__ Open a terminal (e.g., _command prompt_ on Windows or _Terminal_ on iOS) on your computer.

__5__ Install the evolving_grids package by typing `pip install` followed by the path to the downloaded `evolving_grids-1.0-py3-none-any.whl` file. The entire command could look something like this: `pip install C:\Users\sarah\IdeaProjects\evolving_grids\dist\evolving_grids-1.0-py3-none-any.whl`

Now the package is installed on your computer under the name `app`. Before we proceed, here is an explanation of the contents of the package:

Within the `app` package folder, you can find all the code for the shinyapp. Let me run you through the individual files:
* folder `static`, which contains static files, like the stylesheet (`ui.css`) and a couple of .png files used for this report (`final_report.md`)
* several files with code:
    * `__init__.py` indicates to Python that the directory is a Python package
    * `app.py` contains the code for user interface and background processes of the app
    * `grid_functions.py` basic functions required to create and (later) update the game grid
    * `logic_functions.py` functions for implementing the game logic
    * `run.py`  setup for running an ASGI (Asynchronous Server Gateway Interface) application using the Uvicorn server
    * `shiny_extensions.py` extensions to the standard Shiny for Python to make the app work

__6__ Next, you need to find out where exactly you installed the package. You can do this by typing `pip show evolving_grids` in your terminal. This will give you something like this:
````python
>> Name: evolving_grids
>> Version: 1.0
>> Summary:
>> Home-page:
>> Author: sarah_lenz
>> Author-email: sarah.lenz@student.uva.nl
>> License:
>> Location: C:\Users\sarah\AppData\Local\Programs\Python\Python312\Lib\site-packages
>> Requires: htmltools, shiny, starlette, uvicorn
>> Required-by:
````

__7__ Copy the path that indicates the location of the package (in this example `C:\Users\sarah\AppData\Local\Programs\Python\Python312\Lib\site-packages`).

__8__ Change the directory to the `app` folder within `C:\Users\sarah\AppData\Local\Programs\Python\Python312\Lib\site-packages` using `cd C:\Users\sarah\AppData\Local\Programs\Python\Python312\Lib\site-packages\app` (make sure to replace the path with the path to the package on your computer and to add \app at the end of the path).

__9__ Start the app by running `python run.py` in your terminal. Now, there should appear a link (something like `http://127.0.0.1:8000`). Clicking on this link should open the app in your browser.


#### How to use the app

##### The Grid
As explained above, the __game grid__ is located at the bottom right of the page. To play Conway's Game of Life, you need to bring some of the cells to life by clicking on them. Alive cells are marked in orange, dead cells are white.

![alive_grid.png](app\static\alive_grid.png)


##### The Controls
At the top of the control panel, there is a __start and a reset button__. Clicking on 'start' starts the simulation. While the simulation is running, the inscription of the 'start' button switches to 'pause'. Clicking on 'pause' halts the simulation. It is now possible to make adjustments to the configuration of alive and dead cells. Clicking 'start' again resumes the simulation, while pressing 'reset' resets the grid to its original blank state.

![controls_buttons.png](app\static\controls_buttons.png)


Below the 'start/pause' and 'reset' buttons, there is a __slider__ with which the __speed of the simulation__ can be adjusted. '1' indicates the lowest possible speed, '10' the highest.

![controls_speed.png](app\static\controls_speed.png)


At the bottom of the control panel, there are two input fields for __adjusting the size of the grid__. You can specify the number of rows and columns you want the grid to have. The maximum possible number of rows is 35 and the maximum possible number of columns is 50. To set the grid size, press 'set grid size'.

![controls_size.png](app\static\controls_size.png)


#### How to use an exemplary function from the package
The evolving_grids package contains several functions, which are required to run the app. Generally, none of these functions is intended to be used by the users. However, one of the course requirements is that one of the functions from the package needs to be usable. Therefore, I chose `create_new_generation()` as an exemplary function from the package and made it available for users.
Please follow the steps outlined below to use the `create_new_generation()` function (please note that you need to install the package on your computer before following the steps outlined below. If you haven't done so already, please follow steps 1 through 5 from the section _Installing and running the app_):

__1__ If the app is still running, stop the app in the terminal.

__2__ If Python is still active in your console, exit python by typing `exit()`

__3__ Now, navigate back to the directory in which your `app` folder lives using `cd` and the path to the package (again, you get the path by typing `pip show evolving_grids`) and copying the path reference.

__4__ Start Python by typing `python` in your console

__5__ Import the evolving_grids package by typing `import evolving_grids`

__6__ The create_new_generation() function takes one argument: a grid with 1s and 0s of any size. To test the function, you therefore need to set up a grid with only 1s and 0s and hand this grid to the function. You can set up a random 5x5 grid with 1s and 0s using the following code (feel free to adapt the code so that you have bigger or smaller grids):
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
````
__7__ Pass your grid to the create_new_generation() function by typing `app.create_new_generation(grid)`. The function should return a new grid with 0s and 1s indicating which of the cells in your grid stays alive/comes alive or dies in the next generation according to the game rules.

If there are any issues, suggestions or fixes required for the app, please don't hesitate to reach out through github.

-----------------------
Sarah Lenz,
University of Amsterdam