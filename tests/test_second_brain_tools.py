"""
Module that holds all the test of SBT
"""

from second_brain_tools.dir import ic_custom

# cli.py Tests

# dir.py Tests

## Starting the initial check

def initial_check_test():
    "first test"
    var = "01A"
    var_return = "01_Capture-System/"
    assert ic_custom(var) == var_return,  "01A returned 01_Capture-System/"
