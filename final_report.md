# Evolving Grids

A Python shiny app for playing Conway's Game of Life

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


### 4. How do install and use the app
#### Installing and running the app
In the following, I will illustrate the steps you need to take to download and run the app on your laptop. Before you follow the steps outlined below, please make sure that you have Python (https://www.python.org/downloads/) installed on your computer.

__1__ Install the package in your Python IDE using `pip install git+https://github.com/asarafoglou-ptns/Lenz-evolving_grids.git`

Now you will have my directory on your computer. Before we proceed, here is an explanation of the contents of the repository:

Within the root directory there is a `LICENSE`, `README.ipynb`, `requirements.txt`, `final_report.md` and a `setup.py` file (TODO). These are not very relevant, except maybe check out the `README.md` (although this report will fill you in more extensively).

There is also one folder called `app`. This folder contains the code of the app itself. Let me run you through the individual files:
* folder `static`, which contains static files, like the stylesheet (`ui.css`) and a couple of .png files used for this report (`final_report.md`)
* several files with code:
  * `__init__.py` indicates to Python that the directory is a Python package
  * `app.py` contains the code for user interface and background processes of the app
  * `grid_functions.py` basic functions required to create and (later) update the game grid
  * `logic_functions.py` functions for implementing the game logic
  * `run.py`  setup for running an ASGI (Asynchronous Server Gateway Interface) application using the Uvicorn server
  * `shiny_extensions.py` extensions to the standard Shiny for Python to make the app work

__2__ Import the package into your IDE using `import evolving_grids`

TODO try running command from 4. from root directory and if it works, remove:
__3__ Locate the imported evolving_grids package within your IDE navigate to the `app` folder within the package (cd path\to\evolving_grids\app)

__4__ Start the app by executing the `run.py` module using `python -m evolving_grids.app.run`

__5__ Now, you can the app! Enjoy! You can also use my code and make changes to the app, like styling it in a different way or adding more features to it.

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
