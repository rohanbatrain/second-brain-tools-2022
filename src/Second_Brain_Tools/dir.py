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
    if len(dir_code)== 2:
        dir_path = dir_len_two(dir_code)
    elif len(dir_code)== 3:
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
    #Implemented regex for making flow choice.
    if re.match("01", dir_code):
        dir_path = dir_len_three_capture_system(dir_code)
    elif re.match("02", dir_code):
        dir_path = dir_len_three_production_system(dir_code)
    elif re.match("03", dir_code):
        dir_path = dir_len_three_knowledge_base(dir_code)
    elif re.match("04", dir_code):
        dir_path = dir_len_three_evergreen(dir_code)
    elif re.match("05", dir_code):
        dir_path = dir_len_three_projects(dir_code)
    elif re.match("06", dir_code):
        dir_path = dir_len_three_personal(dir_code)
    elif re.match("07", dir_code):
        dir_path = dir_len_three_attachments_and_templates(dir_code)
    elif re.match("08", dir_code):
        dir_path = dir_len_three_archive(dir_code)
    else :
        dir_path = DIR_NOT_FOUND
    return dir_path

def dir_len_three_capture_system(dir_code):
    """
    Yet to add
    """
    #01_Capture_System
    if dir_code == "01A":
        dir_path = "01_Capture-System/01A_Inbox/"
    elif dir_code == "01B":
        dir_path = "01_Capture-System/01B_Processed/"
    elif dir_code == "01C":
        dir_path = "01_Capture-System/01C_Periodic-Notes/"

    #01_Capture_System_regex
    else:
        dir_path = DIR_NOT_FOUND
    #01_Capture_System
    return dir_path

def dir_len_three_production_system(dir_code):
    """
    Yet to add
    """
    #02_Production-System
    if dir_code == "02A":
        dir_path = "02A_Youtube/"
    #02_Production-System_regex
    else:
        dir_path = DIR_NOT_FOUND
    #02_Production-System
    return dir_path

def dir_len_three_knowledge_base(dir_code):
    """
    Yet to add
    """
    #03_Knowledge-Base
    if dir_code == "03A":
        dir_path = "03A_Science/"
    elif dir_code == "03B":
        dir_path  = "03B_Languages/"
    elif dir_code == "03C":
        dir_path = "03C_IT-Skills/"
    elif dir_code == "03D":
        dir_path = "03D_Philosphy/"

    #03_Knowledge-Base_regex
    else:
        dir_path = DIR_NOT_FOUND
    #03_Knowledge-Base
    return dir_path

def dir_len_three_evergreen(dir_code):
    """
    Yet to add
    """
    #04_Evergreen
    if dir_code == "04A":
        dir_path = "04A_Network/"
    elif dir_code == "04B":
        dir_path  = "04B_Events/"
    elif dir_code == "04C":
        dir_path = "04C_Locations/"
    #04_Evergreen_regex
    else:
        dir_path = DIR_NOT_FOUND
    #04_Evergreen
    return dir_path

def dir_len_three_projects(dir_code):
    """
    Yet to add
    """
    #05_Projects
    if dir_code == "05A":
        dir_path = "05A_Brands/"
    elif dir_code == "05B":
        dir_path  = "05B_Startup/"
    elif dir_code == "05C":
        dir_path = "05C_Business/"
    elif dir_code == "05D":
        dir_path  = "05D_Story-Writing/"
    elif dir_code == "05E":
        dir_path = "05E_Competitions/"
    #05_Projects_regex
    else:
        dir_path = DIR_NOT_FOUND
    #05_Projects
    return dir_path

def dir_len_three_personal(dir_code):
    """
    Yet to add
    """
    #06_Personal
    if dir_code == "06A":
        dir_path = "06A_Brands/"
    elif dir_code == "06B":
        dir_path  = "06B_Projects/"
    elif dir_code == "06C":
        dir_path = "06C_Workspace-Log/"
    elif dir_code == "06D":
        dir_path  = "06D_Recommendation-List/"
    elif dir_code == "06E":
        dir_path = "06E_Expense-Tracking/"
    #06_Personal_regx
    else:
        dir_path = DIR_NOT_FOUND
    #06_Personal
    return dir_path

def dir_len_three_attachments_and_templates(dir_code):
    """
    Yet to add
    """
    #07_Attachements-and-Templates
    if dir_code == "07A":
        dir_path = "07A_Attachments/"
    elif dir_code == "07B":
        dir_path  = "07B_Templates/"
    #07_Attachements-and-Templates-regex
    else:
        dir_path = DIR_NOT_FOUND
    #07_Attachements-and-Templates
    return dir_path

def dir_len_three_archive(dir_code):
    """
    Yet to add
    """
    #08_Archive
    if dir_code == "08A":
        dir_path = DIR_NOT_FOUND
    #08_Archive_regex
    dir_path = DIR_NOT_FOUND
    #08_Archive
    return dir_path
