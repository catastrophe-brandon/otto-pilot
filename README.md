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
   * pytest - `pip3 install pytest`
   
# Installation

First, you need to clone the contents of this repository. If you're not familiar with git or source control, you
may want to read about that first.

## If you just want to run the main program

From the root folder of this repository:

    $ python main.py 100

Example output:

```
C:\Users\Brandon\repos\otto-pilot>python main.py 288
You entered: 288
Calculating prime numbers less than or equal to 288
Found 61 prime numbers
```


## If you want to run the tests

Running the tests and getting output should be as simple as:
`pytest` from a terminal or Command-Prompt.

Example Output:

```
C:\Users\Brandon\repos\otto-pilot>pytest
============================= test session starts =============================
platform win32 -- Python 3.6.1, pytest-3.1.3, py-1.4.34, pluggy-0.4.0
metadata: {'Python': '3.6.1', 'Platform': 'Windows-10-10.0.16299-SP0', 'Packages': {'pytest': '3.1.3'
, 'py': '1.4.34', 'pluggy': '0.4.0'}, 'Plugins': {'metadata': '1.5.0', 'html': '1.15.2'}}
rootdir: C:\Users\Brandon\repos\otto-pilot, inifile:
plugins: metadata-1.5.0, html-1.15.2
collected 8 items 

tests\test_prime.py ........

========================== 8 passed in 10.14 seconds ==========================
```
