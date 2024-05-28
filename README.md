### Evolving grids

Python app with which you can play Conway's Game of Life (for the course 'Programming: The Next Step' at University of Amsterdam).
Check it out here: TODO add link

__Guide to the repository:__

The main code for my app is in the `app` folder. Here is a small run through of this directory:

* one folder `static`, which contains static files, like the stylesheet (`ui.css`) 
* `__init__.py` indicates to Python that the directory is a Python package
* `shinyapp.py` contains the code for user interface and background processes of the app
* `grid_functions.py` basic functions required to create and (later) update the game grid
* `logic_functions.py` functions for implementing the game logic
* `run.py`  setup for running an ASGI (Asynchronous Server Gateway Interface) application using the Uvicorn server
* `shiny_extensions.py` extensions to the standard Shiny for Python to make the app work


If there are any issues, suggestions or fixes required for the app, please don't hesitate to reach out through github.

-----------------------
Sarah Lenz,
University of Amsterdam