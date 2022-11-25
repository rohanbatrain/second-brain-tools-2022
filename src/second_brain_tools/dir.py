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
    #elif re.match("^08", dir_code):
    #    dir_path = ic_08(dir_code)
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

#ic_01A-Ended

#ic_01B-Started
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
#ic_01B-Ended

#ic_01C-Started
def ic_01c(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "01C":
        dir_path = "01_Capture-System/01C_Periodic-Notes"
    else :
        dir_path = ic_01c1(dir_code)
    return dir_path

#ic_01C1-Started
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
#ic_01C1-Ended

#ic_01C-Ended

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
        dir_path = "03_Knowledge-Base/03D_Theology"
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
    elif dir_code == "03B2":
        dir_path = "03_Knowledge-Base/03B_Languages/03B2_English"
    elif dir_code == "03B3":
        dir_path = "03_Knowledge-Base/03B_Languages/03B3_Sanskrit"
    elif dir_code == "03B4":
        dir_path = "03_Knowledge-Base/03B_Languages/03B4_Japanese"
    elif dir_code == "03B5":
        dir_path = "03_Knowledge-Base/03B_Languages/03B5_Bengali"
    elif dir_code == "03B6":
        dir_path = "03_Knowledge-Base/03B_Languages/03B6_Korean"
    elif dir_code == "03B7":
        dir_path = "03_Knowledge-Base/03B_Languages/03B7_Punjabi"
    elif dir_code == "03B8":
        dir_path = "03_Knowledge-Base/03B_Languages/03B8_Russian"
    elif dir_code == "03B9":
        dir_path = "03_Knowledge-Base/03B_Languages/03B9_French"
    elif dir_code == "03B10":
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
    elif dir_code == "03C2":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C2_Machine-Learning"
    elif dir_code == "03C3":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software"
    elif dir_code == "03C4":
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
    elif dir_code == "03C1B":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1B_Programming-Projects"
    elif dir_code == "03C1C":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1C_Query-Languages"
    else:
        if re.match("^03C1A", dir_code):
            dir_path = ic_03c1a(dir_code)
        elif re.match("^03C1B", dir_code):
            dir_path = ic_03c1b(dir_code)
        elif re.match("^03C1C", dir_code):
            dir_path = ic_03c1c(dir_code)
    return dir_path

#ic_03c1a-Started
def ic_03c1a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    # Splitting the code into two parts without regex, to follow pylint specifications,
    # line too long.
    dir_path = ic_03c1a_part_1(dir_code)

    if dir_path == DIR_NOT_FOUND:
        dir_path = ic_03c1a_part_2(dir_code)

    return dir_path

#ic_03c1a_part_1-Started
def ic_03c1a_part_1(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03C1A1":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A1_Bash"
    elif dir_code == "03C1A2":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A2_Python"
    elif dir_code == "03C1A3":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A3_C-Lang"
    elif dir_code == "03C1A4":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A4_Javascript"
    elif dir_code == "03C1A5":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A5_Dart"
    elif dir_code == "03C1A6":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A6_Flutter"
    elif dir_code == "03C1A7":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A7_C++"
    elif dir_code == "03C1A8":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A8_TypeScript"
    elif dir_code == "03C1A9":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A9_Java"
    elif dir_code == "03C1A10":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A10_C-Sharp"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path
#ic_03c1a_part_1-Ended

#ic_03c1a_part_2-Started
def ic_03c1a_part_2(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03C1A11":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A11_PHP"
    elif dir_code == "03C1A12":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A12_Groovy"
    elif dir_code == "03C1A13":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A13_Ruby"
    elif dir_code == "03C1A14":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A14_Rust"
    elif dir_code == "03C1A15":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A15_Kotlin"
    elif dir_code == "03C1A16":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A16_Golang"
    elif dir_code == "03C1A17":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A17_Perl"
    elif dir_code == "03C1A18":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A18_Visual-Basic-Dot-Net"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path
#ic_03c1a_part_2-Ended

#ic_03c1a-Ended

#ic_03c1b-Started
def ic_03c1b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03C1B1":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1B_Programming-Projects/Project-1/"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path
#ic_03c1b-Ended

#ic_03c1c-Started
def ic_03c1c(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03C1C1":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1C_Query-Languages/03C1C1_SQL"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path
#ic_03c1c-Ended

# ic_03c1-Ended

# ic_03c2-Started
def ic_03c2(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03C2A":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C2_Machine-Learning/03C2A_Reinforcement-Learning/"
    elif dir_code == "03C2B":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C2_Machine-Learning/03C2B_Deep-Learning/"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path
# ic_03c2-Ended

# ic_03c3-Started
def ic_03c3(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03C3A":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application"
    elif dir_code == "03C3B":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3B_Operating-System"
    else:
        if re.match("^03C3A", dir_code):
            dir_path = ic_03c3a(dir_code)
        elif re.match("^03C3B", dir_code):
            dir_path = ic_03c3b(dir_code)
    return dir_path

# ic_03c3a-Started
def ic_03c3a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03C3A1":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/03C3A1__Unreal-Engine"
    elif dir_code == "03C3A2":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/03C3A2__Blender"
    elif dir_code == "03C3A3":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/03C3A3__Unity"
    elif dir_code == "03C3A4":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/03C3A4__MariaDB"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path
# ic_03c3a-Ended

# ic_03c3b-Started
def ic_03c3b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03C3B1":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3B_Operating-System/03C3B1_Linux"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path
# ic_03c3b-Ended

# ic_03c3-Ended

# ic_03c4-Started
def ic_03c4(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03C4A":
        dir_path = "03_Knowledge-Base/03C_IT-Skills/03C4_System-Administration/03C4A_Web-Servers"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path
# ic_03c4-Ended

# ic_03c-Ended

# ic_03d-Started
def ic_03d(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "03D1":
        dir_path = "03_Knowledge-Base/03D_Theology/03D1_Hinduism"
    elif dir_code == "03D2":
        dir_path = "03_Knowledge-Base/03D_Theology/03D2_Sikhism"
    elif dir_code == "03D3":
        dir_path = "03_Knowledge-Base/03D_Theology/03D3_Buddhism"
    elif dir_code == "03D4":
        dir_path = "03_Knowledge-Base/03D_Theology/03D4_Islam"
    elif dir_code == "03D5":
        dir_path = "03_Knowledge-Base/03D_Theology/03D5_Christianity"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path
# ic_03d-Ended

# ic_03-Ended

# 03-Ended


# 04-Started

# ic_04-Started
def ic_04(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "04A":
        dir_path = "04_Evergreen/04A_Network"
    elif dir_code == "04B":
        dir_path = "04_Evergreen/04B_Events"
    elif dir_code == "04C":
        dir_path = "04_Evergreen/04C_Locations"
    else:
        if re.match("^04A", dir_code):
            dir_path = ic_04a(dir_code)
        elif re.match("^04B", dir_code):
            dir_path = ic_04b(dir_code)
        elif re.match("^04C", dir_code):
            dir_path = ic_04c(dir_code)
    return dir_path

# ic_04A-Started
def ic_04a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "04A1":
        dir_path = "04_Evergreen/04A_Network/04A1_Bros"
    elif dir_code == "04A2":
        dir_path = "04_Evergreen/04A_Network/04A2_Class-Room"
    elif dir_code == "04A3":
        dir_path = "04_Evergreen/04A_Network/04A3_Social-Media"
    elif dir_code == "04A4":
        dir_path = "04_Evergreen/04A_Network/04A4_Friends"
    elif dir_code == "04A5":
        dir_path = "04_Evergreen/04A_Network/04A5_Family"
    elif dir_code == "04A6":
        dir_path = "04_Evergreen/04A_Network/04A6_Corporate"
    elif dir_code == "04A7":
        dir_path = "04_Evergreen/04A_Network/04A7_Relatives"
    elif dir_code == "04A99":
        dir_path = "04_Evergreen/04A_Network/04A99_Miscellaneous"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path
# ic_04A-Ended

# ic_04B-Started
def ic_04b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "04B1":
        dir_path = "04_Evergreen/04B_Events/04B1_Incidents/"
    elif dir_code == "04B2":
        dir_path = "04_Evergreen/04B_Events/04B2_Planned-Events/"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path
# ic_04B-Ended

# ic_04C-Started
def ic_04c(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "04C1":
        dir_path = "04_Evergreen/04C_Locations/04C1_School"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path
# ic_04C-Ended

# ic_04-Ended

# 04-Ended


# 05-Started
def ic_05(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "05A":
        dir_path = "05_Projects/05A_Brands"
    elif dir_code == "05B":
        dir_path = "05_Projects/05B_Startup"
    elif dir_code == "05C":
        dir_path = "05_Projects/05C_Business"
    elif dir_code == "05D":
        dir_path = "05_Projects/05D_Story-Writing"
    elif dir_code == "05E":
        dir_path = "05_Projects/05E_Competitions"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path
# 05-Ended


# 06-Started
def ic_06(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "06A":
        dir_path = "06_Personal/06A_Brand"
    elif dir_code == "06B":
        dir_path = "06_Personal/06B_Projects"
    elif dir_code == "06C":
        dir_path = "06_Personal/06C_Workspace-Log"
    elif dir_code == "06D":
        dir_path = "06_Personal/06D_Recommendation-List"
    else:
        if re.match("^06A", dir_code):
            dir_path = ic_06a(dir_code)
        elif re.match("^06B", dir_code):
            dir_path = ic_06b(dir_code)
        elif re.match("^06C", dir_code):
            dir_path = ic_06c(dir_code)
        elif re.match("^06D", dir_code):
            dir_path = ic_06d(dir_code)
    return dir_path

def ic_06a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "06A1":
        dir_path = "06_Personal/06A_Brand/06A1_Brand-1"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path

def ic_06b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "06B1":
        dir_path = "06_Personal/06B_Projects/06B1_Home-Lab"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path

def ic_06c(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "06C1":
        dir_path = "06_Personal/06C_Workspace-Log/06C1_Laptop-Workspace/"
    elif dir_code == "06C2":
        dir_path = "06_Personal/06C_Workspace-Log/06C2_Web-Presence/"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path

def ic_06d(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "06D1":
        dir_path = "06_Personal/06D_Recommendation-List/06D1_Movies"
    elif dir_code == "06D2":
        dir_path = "06_Personal/06D_Recommendation-List/06D2_Music"
    elif dir_code == "06D3":
        dir_path = "06_Personal/06D_Recommendation-List/06D3_Books"
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path

# 06-Ended


# 07-Started
def ic_07(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "07A":
        dir_path = "07_Attachments-and-Templates/07A_Attachments"
    elif dir_code == "07B":
        dir_path = "07_Attachments-and-Templates/07B_Templates"
    else:
        if re.match("^07B", dir_code):
            dir_path = ic_07b(dir_code)
    return dir_path

def ic_07b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "07B1":
        dir_path = "07_Attachments-and-Templates/07B_Templates/07B1_Periodic-Notes"
    else:
        if re.match("^07B", dir_code):
            dir_path = ic_07b(dir_code)
    return dir_path
# 07-Ended


#### Testing //Comment out all the variables below in production.
