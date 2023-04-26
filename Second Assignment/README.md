# Assignment 2:  Write a program that does flowing operations on a directory tree.
**a. Add a new folder at a particular path in the directory tree.**
**b. Removed a folder from a particular path in the directory tree.**
**c. Fetch the path of the given folder.**
**d. Update name of the folder.**


## Project Description

* In this project, I built code that allows the user to perform a variety of functions on a directory that he or she provides.

* Tasks that can be performed are: 1) Add a new folder
                                   2) Remove a folder
                                   3) Fetch the path of a folder
                                   4) Update name of the folder
                                   5) Print the directory structure

## Installation

* As we deal with the folder, we will use the Python "os" module, and we will also do command-line parsing, which requires the Python "argparse" module.

* The "os" and "argparse" modules are both part of Python 3's standard library, or stdlib. This means that it is pre-installed with Python and does not need to be installed separately.


## Steps/How to run the code

* Step 1: Switch on the terminal.

* Step 2: Open the project folder.

* Step 3: To run the code, type the following: python app.py print Path of the directory 

* Explanation of the above code: a) app.py is the file name where the code resides

                                 b) "print": It specifies the operation to be performed by the programme.

                                    There are five types of operations that can be performed.
                                               i) add
                                               ii) remove
                                               iii) fetch
                                               iv) update
                                               v) print

                                 c) Path of the directory : The path to the folder in which you want to conduct certain operations. Always specific the path in double quote

* Few sample command which would help the user to get a better understanding
    1) python app.py add "D:\Web\Final Assignment\second"
    2) python app.py remove "D:\Web\Final Assignment\second"
    3) python app.py fetch "D:\Web\Final Assignment\second"
    4) python app.py update "D:\Web\Final Assignment\second"
    5) python app.py print "D:\Web\Final Assignment\second"








