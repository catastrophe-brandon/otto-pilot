# otto-pilot
I just watched Airplane!

# About

This is part of an exercise in writing and testing a program that computes prime numbers.

# Pre-requisites

You will need to have the following installed and set up on your system in order to get the code running:
   * Python 3.6
        * Mac - `brew install python3`
        * Windows - Download the installer, and install as one normally would
            * Don't forget to add PYTHONPATH to your path for command-line convenience
            * Don't forget to click the Python installer's checkbox to set the PYTHONPATH variable if you're installing on
              windows.
        * Confirm installation by running `python --version` from a terminal or Command Prompt.
   * pip3 - This is typically bundled with Python 3.6. Confirm by running `pip3 --version` from a terminal or Command Prompt.
   * tox - Just `pip3 install tox` and you should be all set. Confirm install by running `tox --version`

# Installation

First, you need to clone the contents of this repository. If you're not familiar with git or source control, you
may want to read about that first.

## If you just want to run the main program

From the root folder of this repository:

    1. `pip install -r requirements.txt`
    2. `python main.py`

## If you want to run the tests

Tox is setup to execute all the tests for you. Running the tests and getting output should be as simple as:
`tox -re test` from a terminal or Command-Prompt.
