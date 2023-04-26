# Assignment 1: Come up with a config (data structure) and load a new directory tree from config.


## Project Description

* In this assignment, I created a config.yaml file that included a "dir" key that contained the location of a folder.

* We utilise the user's current working directory if no path is provided.

* This path is retrieved in the "app.py" file, and the user is then prompted to choose which operations to do, such as add, remove, fetch, update, and print.


## Installation

* As we are using yaml files and fetching the data from yaml files, we would be required to use the Python package called PyYAML.

* To install PyYAML, use the following command: "pip install PyYAML".

* We also used the os module, which is part of Python 3's standard library, or stdlib. This means that it is included with your Python installation and does not need to be installed separately.

* Please change the file path of config.yaml with your file path, wherever the YAML file is located, in the app.py file on line 6.
