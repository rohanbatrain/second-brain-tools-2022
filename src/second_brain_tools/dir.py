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
    Takes dir_code as input and
    returns the absolute directory
    path of the code.
    """

    dir_path = ic_custom(dir_code)

    return dir_path
    #root_dir_id_end.

# User-Custom Directories
def ic_custom(dir_code):
    """
    Checks for user defined directories first from the config.
    """
    #some example dir
    if dir_code=="example":
        dir_path = "This/is/a/boiler/plate/example/"
    elif dir_code == "example-elif" :
        dir_path = "This/is/an/example/"
    #loading user defined commands from config started

    #loading user defined commands from config started
    else:
        dir_path = ic_root(dir_code)
    return dir_path

# Root-Started
def ic_root(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
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
        dir_path = ic_root_regex(dir_code)
    return dir_path

def ic_root_regex (dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    #ic_custom_regex-started
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
    #ic_custom_regex-end
    return dir_path

# Root-Ended

# 01-Started

#ic_01-Started
def ic_01(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "01A":
        dir_path = "01_Capture-System/01A_Inbox/"
    elif dir_code == "01B":
        dir_path = "01_Capture-System/01B_Processed/"
    elif dir_code == "01C":
        dir_path = "01_Capture-System/01C_Periodic-Notes/"
    #01_regex
    else:
        if re.match("^01A", dir_code):
            dir_path = ic_01a(dir_code)
        if re.match("^01B", dir_code):
            dir_path = ic_01b(dir_code)
        if re.match("^01C", dir_code):
            dir_path = ic_01c(dir_code)
    return dir_path
#ic_01-Ended

#ic_01A-Started
def ic_01a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "01A1":
        dir_path = "01_Capture-System/01A_Inbox/01A1_Quick-Capture"
    elif dir_code == "01A2":
        dir_path = "01_Capture-System/01A_Inbox/01A2_Link-Capture"
    elif dir_code == "01A3":
        dir_path = "01_Capture-System/01A_Inbox/01A3_Thought-Capture"
    elif dir_code == "01A3":
        dir_path = "01_Capture-System/01A_Inbox/01A4_API-Capture"
    else:
        if re.match("^01A1", dir_code):
            dir_path = ic_01a1(dir_code)
        if re.match("^01A2", dir_code):
            dir_path = ic_01a2(dir_code)
        if re.match("^01A3", dir_code):
            dir_path = ic_01a3(dir_code)
    return dir_path


#ic_01a1-Started
def ic_01a1(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    dir_path = print("---")
    return dir_path
#newic_01a1-Ended


#ic_01a2-Started
def ic_01a2(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    dir_path = print("---")
    return dir_path
#ic_01a2-Ended


#ic_01a3-Started
def ic_01a3(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    dir_path = print("---")
    return dir_path
#ic_01a3-Ended


#ic_01a4-Started
def ic_01a4(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    dir_path = print("---")
    return dir_path
#ic_01a4-Ended

#ic_01A_Ended

# 01-Ended


# 02-Started
def ic_02(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    dir_path = print("---")
    return dir_path
# 02-Ended


# 03-Started
def ic_03(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    dir_path = print("---")
    return dir_path
# 03-Ended


# 04-Started
def ic_04(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    dir_path = print("---")
    return dir_path
# 04-Ended


# 05-Started
def ic_05(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    dir_path = print("---")
    return dir_path
# 05-Ended


# 06-Started
def ic_06(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    dir_path = print("---")
    return dir_path
# 06-Ended


# 07-Started
def ic_07(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    dir_path = print("---")
    return dir_path
# 07-Ended


# 08-Started
def ic_08(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    dir_path = print("---")
    return dir_path
# 08-Ended

#### Testing //Comment out all the variables below in production.
