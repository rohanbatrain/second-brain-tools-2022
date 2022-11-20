"""
Module which contains directory specific functions.
I know i can use os.probe with some logic to get this working,
But i would really like to hardcode the absolute path for error pruning my script.
"""

# imports
# import re

# Default values
DIR_NOT_FOUND = "Wrong argument passed, the dir code you specified doesn't exist"

def initial_check(dir_code):
    """
    Takes dir code as input and returns the absolute directory path of the code.
    """
    #root_dir_id_start
    if dir_code == "^01":
        ic_01()
    elif dir_code == "^02":
        ic_02()
    elif dir_code == "^03":
        ic_03()
    elif dir_code == "^04":
        ic_04()
    elif dir_code == "^05":
        ic_05()
    elif dir_code == "^06":
        ic_06()
    elif dir_code == "^07":
        ic_07()
    elif dir_code == "^08":
        ic_08()
    #root_dir_id_end.

# 01-Started
def ic_01():
    """
    Placeholder
    """
    print("---1")
# 01-Ended


# 02-Started
def ic_02():
    """
    Placeholder
    """
    print("---")
# 02-Ended


# 03-Started
def ic_03():
    """
    Placeholder
    """
    print("---")
# 03-Ended


# 04-Started
def ic_04():
    """
    Placeholder
    """
    print("---")
# 04-Ended


# 05-Started
def ic_05():
    """
    Placeholder
    """
    print("---")
# 05-Ended


# 06-Started
def ic_06():
    """
    Placeholder
    """
    print("---")
# 06-Ended


# 07-Started
def ic_07():
    """
    Placeholder
    """
    print("---")
# 07-Ended


# 08-Started
def ic_08():
    """
    Placeholder
    """
    print("---")
# 08-Ended

#### Testing //Comment out all the variables below in production.

#initial_check("01")
