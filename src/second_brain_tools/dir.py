"""
Module which contains directory specific functions.
I know i can use os.probe with some logic to get this working,
But i would really like to hardcode the absolute path for error pruning my script.
"""

# imports
import re

# Default values assignation started
DIR_NOT_FOUND = "Wrong argument passed, the dir code you specified doesn't exist"
# Default values assignation ended

# Initial check started
def initial_check(dir_code):
    """
    Takes dir_code as input and
    returns the absolute directory
    path of the code.
    """

    dir_path = ic_custom(dir_code)

    return dir_path
# Initial check Ended
#-------------------------------------#
# User-Custom Directories Started
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

    #loading user defined commands from config ended
    else:
        dir_path = ic_root(dir_code)
    return dir_path

# User-Custom Directories Ended
#-------------------------------------#
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
#-------------------------------------#
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
        elif re.match("^01B", dir_code):
            dir_path = ic_01b(dir_code)
        elif re.match("^01C", dir_code):
            dir_path = ic_01c(dir_code)
    return dir_path

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
        elif re.match("^01A2", dir_code):
            dir_path = ic_01a2(dir_code)
        elif re.match("^01A3", dir_code):
            dir_path = ic_01a3(dir_code)
    return dir_path

#ic_01a1-Started
def ic_01a1(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    #Flow ended
    print(dir_code)
    dir_path = DIR_NOT_FOUND
    return dir_path
#ic_01a1-Ended

#ic_01a2-Started
def ic_01a2(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "01A2A":
        dir_path = "01_Capture-System/01A_Inbox/01A2_Link-Capture/01A2A_Social-Networking"
    elif dir_code == "01A2B":
        dir_path = "01_Capture-System/01A_Inbox/01A2_Link-Capture/01A2B_Professional-Networking"
    else:
        if re.match("^01A2A", dir_code):
            dir_path = ic_01a2a(dir_code)
        elif re.match("^01A2B", dir_code):
            dir_path = ic_01a2b(dir_code)
    return dir_path

#ic_01a2a-Started
def ic_01a2a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "01A2A1":
        dir_path = "01_Capture-System/01A_Inbox/01A2_Link-Capture/01A2A_Social-Networking/01A2A1_Reddit/"
    else :
        print(dir_code)
        dir_path = DIR_NOT_FOUND
    return dir_path
#ic_01a2a-Ended

#ic_01a2b-Started
def ic_01a2b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "01A2B1":
        dir_path = "01_Capture-System/01A_Inbox/01A2_Link-Capture/01A2B_Professional-Networking/01A2B1_LinkedIn/"
    else :
        print(dir_code)
        dir_path = DIR_NOT_FOUND
    return dir_path
#ic_01a2b-Ended

#ic_01a2-Ended


#ic_01a3-Started
def ic_01a3(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "01A3":
        dir_path = "01_Capture-System/01A_Inbox/01A3_Thought-Capture/"
    else :
        print(dir_code)
        dir_path = DIR_NOT_FOUND
    return dir_path
#ic_01a3-Ended


#ic_01a4-Started
def ic_01a4(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "01A4":
        dir_path = "01_Capture-System/01A_Inbox/01A4_API-Capture/"
    else :
        print(dir_code)
        dir_path = DIR_NOT_FOUND
    return dir_path
#ic_01a4-Ended

#ic_01A_Ended

#ic_01B_Started
def ic_01b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "01B":
        dir_path = "01_Capture-System/01B_Processed"
    else :
        print(dir_code)
        dir_path = DIR_NOT_FOUND
    return dir_path
#ic_01B_Ended

#ic_01C_Started
def ic_01c(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "01C":
        dir_path = "01_Capture-System/01C_Periodic-Notes"
    else :
        dir_path = ic_01c1(dir_code)
    return dir_path

#ic_01C1_Started
def ic_01c1(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "01C1":
        dir_path = "01_Capture-System/01C_Periodic-Notes/01C1_Reminders"
    else :
        print(dir_code)
        dir_path = DIR_NOT_FOUND
    return dir_path
#ic_01C1_Ended

#ic_01C_Ended

#ic_01-Ended

# 01-Ended
#-------------------------------------#
# 02-Started

#ic_02-Started
def ic_02(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "02A":
        dir_path = "02_Production-System/02A_Youtube/"
    elif dir_code == "02B":
        dir_path = "02_Production-System/02B_Medium"
#02_regex
    else:
        if re.match("^02A", dir_code):
            dir_path = ic_02a(dir_code)
        elif re.match("^02B", dir_code):
            dir_path = ic_02b(dir_code)
    return dir_path

#ic_02a-Started
def ic_02a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "02A1":
        dir_path = "02_Production-System/02A_Youtube/02A1_Videos/"
    elif dir_code == "02A2":
        dir_path = "02_Production-System/02A_Youtube/02A2_Shorts/"
    elif dir_code == "02A3":
        dir_path = "02_Production-System/02A_Youtube/02A3_Stories/"
    else:
        print(dir_code)
        dir_path = DIR_NOT_FOUND
    return dir_path
#ic_02a-Ended

#ic_02b-Started
def ic_02b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "02B1":
        dir_path = "02_Production-System/02B_Medium/02B1_Articles/"
    else:
        print(dir_code)
        dir_path = DIR_NOT_FOUND
    return dir_path
#ic_02b-Ended

#ic_02-Ended

# 02-Ended
#-------------------------------------#
# 03-Started

# ic_03-Started
def ic_03(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03A":
        dir_path = "03_Knowledge-Base/03A_Science/"
    elif dir_code == "03B":
        dir_path = "03_Knowledge-Base/03B_Languages/"
    elif dir_code == "03C":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/"
    elif dir_code =="03D":
        dir_path = "03_Knowledge-Base/03D_Philosphy"
    else:
        if re.match("^03A", dir_code):
            dir_path = ic_03a(dir_code)
        elif re.match("^03B", dir_code):
            dir_path = ic_03b(dir_code)
        elif re.match("^03C", dir_code):
            dir_path = ic_03c(dir_code)
        elif re.match("^03D", dir_code):
            dir_path = ic_03d(dir_code)
    return dir_path

# ic_03a-Started
def ic_03a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03A1":
        dir_path = "03_Knowledge-Base/03A_Science/03A1_Chemistry"
    elif dir_code == "03A2":
        dir_path = "03_Knowledge-Base/03A_Science/03A2_Computer-Science"
    elif dir_code == "03A3":
        dir_path = "03_Knowledge-Base/03A_Science/03A3_Mathematics"
    elif dir_code == "03A4":
        dir_path = "03_Knowledge-Base/03A_Science/03A4_Physics"
    else:
        print(dir_code)
        dir_path = DIR_NOT_FOUND
    return dir_path
# ic_03a-Ended

# ic_03b-Started
def ic_03b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03B1":
        dir_path = "03_Knowledge-Base/03B_Languages/03B1_Hindi"
    if dir_code == "03B2":
        dir_path = "03_Knowledge-Base/03B_Languages/03B2_English"
    if dir_code == "03B3":
        dir_path = "03_Knowledge-Base/03B_Languages/03B3_Sanskrit"
    if dir_code == "03B4":
        dir_path = "03_Knowledge-Base/03B_Languages/03B4_Japanese"
    if dir_code == "03B5":
        dir_path = "03_Knowledge-Base/03B_Languages/03B5_Bengali"
    if dir_code == "03B6":
        dir_path = "03_Knowledge-Base/03B_Languages/03B6_Korean"
    if dir_code == "03B7":
        dir_path = "03_Knowledge-Base/03B_Languages/03B7_Punjabi"
    if dir_code == "03B8":
        dir_path = "03_Knowledge-Base/03B_Languages/03B8_Russian"
    if dir_code == "03B9":
        dir_path = "03_Knowledge-Base/03B_Languages/03B9_French"
    if dir_code == "03B10":
        dir_path = "03_Knowledge-Base/03B_Languages/03B10_Spanish"
    else:
        print(dir_code)
        dir_path = DIR_NOT_FOUND
    return dir_path
# ic_03b-Ended

# ic_03c-Started
def ic_03c(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03C1":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming"
    if dir_code == "03C2":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C2_Machine-Learning"
    if dir_code == "03C3":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software"
    if dir_code == "03C4":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C4_System-Administration"
    else:
        if re.match("^03C1", dir_code):
            dir_path = ic_03c1(dir_code)
        elif re.match("^03C2", dir_code):
            dir_path = ic_03c2(dir_code)
        elif re.match("^03C3", dir_code):
            dir_path = ic_03c3(dir_code)
        elif re.match("^03C4", dir_code):
            dir_path = ic_03c4(dir_code)
    return dir_path

# ic_03c-Ended
def ic_03c1(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03C1A":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages"
    if dir_code == "03C1B":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1B_Programming-Projects"
    if dir_code == "03C1C":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1C_Query-Languages"
    else:
        print(dir_code)
        dir_path = DIR_NOT_FOUND
    return dir_path
# ic_03c1-Ended

# ic_03c-Ended

# ic_03-Ended
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
