"""
Module which contains directory specific functions.
I know i can use os.probe with some logic to get this working,
But i would really like to hardcode the absolute path for error pruning my script.
"""

# imports
import re

# Default values
DIR_NOT_FOUND = "Wrong argument passed, the dir code you specified doesn't exist"

def initial_check(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    #root_dir_id_start
    if dir_code == "01":
        dir_path = "01_Capture-System/"
    elif dir_code == "02":
        dir_path = "02_Production-System/"
    elif dir_code == "03":
        dir_path = "03_Knowledge-Base/"
    elif dir_code == "04":
        dir_path = "04_Evergreen/"
    elif dir_code == "05":
        dir_path = "05_Projects/"
    elif dir_code == "06":
        dir_path = "06_Personal/"
    elif dir_code == "07":
        dir_path = "07_Attachments-and-Templates/"
    elif dir_code == "08":
        dir_path = "08_Archive/"
    else:
        dir_path = ic_root(dir_code)
    return dir_path
    #root_dir_id_end.

# Root-Started
def ic_root(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if re.match("^01", dir_code):
        dir_path = ic_01(dir_code)
    elif re.match("^02", dir_code):
        dir_path = ic_02(dir_code)
    elif re.match("^03", dir_code):
        dir_path = ic_03(dir_code)
    elif re.match("^04", dir_code):
        dir_path = ic_04(dir_code)
    elif re.match("^05", dir_code):
        dir_path = ic_05(dir_code)
    elif re.match("^06", dir_code):
        dir_path = ic_06(dir_code)
    elif re.match("^07", dir_code):
        dir_path = ic_07(dir_code)
    elif re.match("^08", dir_code):
        dir_path = ic_08(dir_code)
    return dir_path
# Root-Ended

# 01-Started
def ic_01(dir_code):
    """
    Placeholder
    """
    dir_path = print("---")
    return dir_path

# 01-Ended


# 02-Started
def ic_02(dir_code):
    """
    Placeholder
    """
    dir_path = print("---")
    return dir_path
# 02-Ended


# 03-Started
def ic_03(dir_code):
    """
    Placeholder
    """
    dir_path = print("---")
    return dir_path
# 03-Ended


# 04-Started
def ic_04(dir_code):
    """
    Placeholder
    """
    dir_path = print("---")
    return dir_path
# 04-Ended


# 05-Started
def ic_05(dir_code):
    """
    Placeholder
    """
    dir_path = print("---")
    return dir_path
# 05-Ended


# 06-Started
def ic_06(dir_code):
    """
    Placeholder
    """
    dir_path = print("---")
    return dir_path
# 06-Ended


# 07-Started
def ic_07(dir_code):
    """
    Placeholder
    """
    dir_path = print("---")
    return dir_path
# 07-Ended


# 08-Started
def ic_08(dir_code):
    """
    Placeholder
    """
    dir_path = print("---")
    return dir_path
# 08-Ended

#### Testing //Comment out all the variables below in production.
