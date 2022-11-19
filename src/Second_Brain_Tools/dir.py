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
    Takes dir code as input and returns the absolute directory path of the code.
    """
    if len(dir_code)==2:
        dir_path = dir_len_two(dir_code)
    elif len(dir_code)==3:
        dir_path = dir_len_three(dir_code)
    return dir_path

def dir_len_two(dir_code):
    """
    Takes dir code of two characters as input and
    returns the absolute directory path of the code in the root dir.
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
    #root_dir_id_end.
    return dir_path

def dir_len_three (dir_code):
    """
    Takes dir code of three characters as input and
    returns the absolute directory path of the code in the root dir.
    """
    #01_Capture_System
    if re.match("01", dir_code):
        if dir_code == "01A":
            dir_path = "01_Capture-System/01A_Inbox/"
        elif dir_code == "01B":
            dir_path = "01_Capture-System/01B_Processed/"
        elif dir_code == "01C":
            dir_path = "01_Capture-System/01C_Periodic-Notes/"
        #01_Capture_System_regex
        else:
            print(DIR_NOT_FOUND)
    #01_Capture_System


    #   02_Production-System
    if re.match("02", dir_code):
        if dir_code == "02A":
            dir_path = "02_Production-System/02A_Youtube/"
        #02_Production-System_regex
        else:
            print(DIR_NOT_FOUND)
    #   02_Production-System


    #   03_Knowledge-Base
    if re.match("03", dir_code):
        if dir_code == "03A":
            dir_path = ""
        #03_Knowledge-Base_regex
        else:
            print(DIR_NOT_FOUND)
    #   03_Knowledge-Base

    #   04_Evergreen
    if re.match("03", dir_code):
        if dir_code == "03A":
            dir_path = ""
    #   04_Evergreen_regex
        else:
            print(DIR_NOT_FOUND)
    #   04_Evergreen

    #   05_Projects
    if re.match("03", dir_code):
        if dir_code == "03A":
            dir_path = ""
    #   05_Projects_regex
        else:
            print(DIR_NOT_FOUND)
    #   05_Projects

    #   06_Personal
    if re.match("03", dir_code):
        if dir_code == "03A":
            dir_path = ""
    #   06_Personal_regex
        else:
            print(DIR_NOT_FOUND)
    #   06_Personal

    #   07_Attachments-and-Templates
    if re.match("03", dir_code):
        if dir_code == "03A":
            dir_path = ""
    #   07_Attachments-and-Templates_regex
        else:
            print(DIR_NOT_FOUND)
    #   07_Attachments-and-Templates

    #   08_Archive
    if re.match("03", dir_code):
        if dir_code == "03A":
            dir_path = ""
    #   08_Archive_regex
        else:
            print(DIR_NOT_FOUND)
    #   08_Archive
    return dir_path
