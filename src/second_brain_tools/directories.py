"""
Module which contains directory specific functions.
I know i can use os.probe with some logic to get this working,
But i would really like to hardcode the absolute path for error pruning my script.
"""
# Importing production modules Started
import re
import second_brain_tools.config as sbtc
import sys

# Importing production modules finished
# Default values assignation started
DIR_NOT_FOUND = sbtc.DIR_NOT_FOUND

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
# -------------------------------------#
# User-Custom Directories Started


def ic_custom(dir_code):
    """
    Checks for user defined directories first from the config.
    """
    # some example dir
    if dir_code == "example":
        dir_path = sbtc.example
    elif dir_code == "example_elif":
        dir_path = sbtc.example_elif
    elif dir_code == "root":
        dir_path = sbtc.SECOND_BRAIN_DIRECTORY
    # Add your directories here.
    # Add your directories here.
    # Add your directories here.
    # Add your directories here.
    # Add your directories here.
    else:
        dir_path = ic_root(dir_code)
    return dir_path


# User-Custom Directories Ended
# -------------------------------------#
# Root-Started


def ic_root(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "01":
        dir_path = sbtc._01
    elif dir_code == "02":
        dir_path = sbtc._02
    elif dir_code == "03":
        dir_path = sbtc._03
    elif dir_code == "04":
        dir_path = sbtc._04
    elif dir_code == "05":
        dir_path = sbtc._05
    elif dir_code == "06":
        dir_path = sbtc._06
    elif dir_code == "07":
        dir_path = sbtc._07
    elif dir_code == "08":
        dir_path = sbtc._08
    else:
        dir_path = ic_root_regex(dir_code)
    return dir_path


def ic_root_regex(dir_code):
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
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# Root-Ended
# 01-Started # ic_01-Started


def ic_01(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "01A":
        dir_path = sbtc._01A
    elif dir_code == "01B":
        dir_path = sbtc._01B
    elif dir_code == "01C":
        dir_path = sbtc._01C
    # 01_regex
    else:
        if re.match("^01A", dir_code):
            dir_path = ic_01a(dir_code)
        elif re.match("^01B", dir_code):
            dir_path = ic_01b(dir_code)
        elif re.match("^01C", dir_code):
            dir_path = ic_01c(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01A-Started


def ic_01a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "01A1":
        dir_path = sbtc._01A1
    elif dir_code == "01A2":
        dir_path = sbtc._01A2
    elif dir_code == "01A3":
        dir_path = sbtc._01A3
    elif dir_code == "01A4":
        dir_path = sbtc._01A4
    elif dir_code == "01A5":
        dir_path = sbtc._01A5
    elif dir_code == "01A6":
        dir_path = sbtc._01A6
    elif dir_code == "01A7":
        dir_path = sbtc._01A7
    elif dir_code == "01A8":
        dir_path = sbtc._01A8
    elif dir_code == "01A9":
        dir_path = sbtc._01A9
    elif dir_code == "01A10":
        dir_path = sbtc._01A10
    else:
        if re.match("^01A1", dir_code):
            dir_path = ic_01a1(dir_code)
        elif re.match("^01A2", dir_code):
            dir_path = ic_01a2(dir_code)
        elif re.match("^01A8", dir_code):
            dir_path = ic_01a8(dir_code)
        elif re.match("^01A9", dir_code):
            dir_path = ic_01a9(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01a1-Started


def ic_01a1(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    # Flow ended
    dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01a1-Ended # ic_01a2-Started


def ic_01a2(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "01A2A":
        dir_path = sbtc._01A2A
    elif dir_code == "01A2B":
        dir_path = sbtc._01A2B
    else:
        if re.match("^01A2A", dir_code):
            dir_path = ic_01a2a(dir_code)
        elif re.match("^01A2B", dir_code):
            dir_path = ic_01a2b(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01a2a-Started


def ic_01a2a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "01A2A1":
        dir_path = sbtc._01A2A1
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01a2a-Ended # ic_01a2b-Started


def ic_01a2b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "01A2B1":
        dir_path = sbtc._01A2B1
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01a2b-Ended
# # ic_01a2-Ended
# ic_01a8-Started


def ic_01a8(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "01A8A":
        dir_path = sbtc._01A8A
    elif dir_code == "01A8B":
        dir_path = sbtc._01A8B
    elif dir_code == "01A8C":
        dir_path = sbtc._01A8C
    elif dir_code == "01A8D":
        dir_path = sbtc._01A8D
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01a8-Ended # ic_01a9-Started


def ic_01a9(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "01A9A":
        dir_path = sbtc._01A9A
    elif dir_code == "01A9B":
        dir_path = sbtc._01A9B
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01a9-Ended # ic_01A-Ended # ic_01B-Started


def ic_01b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "01B1":
        dir_path = sbtc._01B1
    elif dir_code == "01B2":
        dir_path = sbtc._01B2
    elif dir_code == "01B3":
        dir_path = sbtc._01B3
    else:
        if re.match("^01B3", dir_code):
            dir_path = ic_01b3(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01B-Ended # ic_01B2-Started


def ic_01b3(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "01B3A":
        dir_path = sbtc._01B3A
    elif dir_code == "01B3B":
        dir_path = sbtc._01B3B
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01B2-Ended # ic_01C-Started


def ic_01c(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "01C1":
        dir_path = sbtc._01C1
    else:
        if re.match("^01C1", dir_code):
            dir_path = ic_01c1(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01C1-Started


def ic_01c1(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "01C1A":
        dir_path = sbtc._01C1A
    elif dir_code == "01C1B":
        dir_path = sbtc._01C1B
    elif dir_code == "01C1C":
        dir_path = sbtc._01C1C
    elif dir_code == "01C1D":
        dir_path = sbtc._01C1D
    elif dir_code == "01C1E":
        dir_path = sbtc._01C1E
    elif dir_code == "01C1F":
        dir_path = sbtc._01C1F
    elif dir_code == "01C1G":
        dir_path = sbtc._01C1G
    elif dir_code == "01C1H":
        dir_path = sbtc._01C1H
    elif dir_code == "01C1I":
        dir_path = sbtc._01C1I
    else:
        if re.match("^01C1B", dir_code):
            dir_path = ic_01c1b(dir_code)
        if re.match("^01C1I", dir_code):
            dir_path = ic_01c1i(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01C1-Ended # ic_01C1B-Started


def ic_01c1b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "01C1B1":
        dir_path = sbtc._01C1B1
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01C1B-Ended # ic_01C1i-Started


def ic_01c1i(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "01C1I1":
        dir_path = sbtc._01C1I1
    elif dir_code == "01C1I2":
        dir_path = sbtc._01C1I2
    elif dir_code == "01C1I3":
        dir_path = sbtc._01C1I3
    elif dir_code == "01C1I4":
        dir_path = sbtc._01C1I4
    elif dir_code == "01C1I5":
        dir_path = sbtc._01C1I5
    elif dir_code == "01C1I6":
        dir_path = sbtc._01C1I6
    elif dir_code == "01C1I7":
        dir_path = sbtc._01C1I7
    elif dir_code == "01C1I8":
        dir_path = sbtc._01C1I8
    elif dir_code == "01C1I9":
        dir_path = sbtc._01C1I9
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_01C1i-Ended # ic_01C-Ended # ic_01-Ended # 01-Ended # 02-Started # c_02-Started


def ic_02(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "02A":
        dir_path = sbtc._02A
    elif dir_code == "02B":
        dir_path = sbtc._02B
    # 02_regex
    else:
        if re.match("^02A", dir_code):
            dir_path = ic_02a(dir_code)
        elif re.match("^02B", dir_code):
            dir_path = ic_02b(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


# ic_02a-Started


def ic_02a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "02A1":
        dir_path = sbtc._02A1
    elif dir_code == "02A2":
        dir_path = sbtc._02A2
    elif dir_code == "02A3":
        dir_path = sbtc._02A3
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_02a-Ended # ic_02b-Started


def ic_02b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "02B1":
        dir_path = sbtc._02B1
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_02b-Ended # ic_02-Ended # 02-Ended # 03-Started # ic_03-Started


def ic_03(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03A":
        dir_path = sbtc._03A
    elif dir_code == "03B":
        dir_path = sbtc._03B
    elif dir_code == "03C":
        dir_path = sbtc._03C
    elif dir_code == "03D":
        dir_path = sbtc._03D
    else:
        if re.match("^03A", dir_code):
            dir_path = ic_03a(dir_code)
        elif re.match("^03B", dir_code):
            dir_path = ic_03b(dir_code)
        elif re.match("^03C", dir_code):
            dir_path = ic_03c(dir_code)
        elif re.match("^03D", dir_code):
            dir_path = ic_03d(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03a-Started


def ic_03a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03A1":
        dir_path = sbtc._03A1
    elif dir_code == "03A2":
        dir_path = sbtc._03A2
    elif dir_code == "03A3":
        dir_path = sbtc._03A3
    elif dir_code == "03A4":
        dir_path = sbtc._03A4
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03a-Ended # ic_03b-Started


def ic_03b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03B1":
        dir_path = sbtc._03B1
    elif dir_code == "03B2":
        dir_path = sbtc._03B2
    elif dir_code == "03B3":
        dir_path = sbtc._03B3
    elif dir_code == "03B4":
        dir_path = sbtc._03B4
    elif dir_code == "03B5":
        dir_path = sbtc._03B5
    elif dir_code == "03B6":
        dir_path = sbtc._03B6
    elif dir_code == "03B7":
        dir_path = sbtc._03B7
    elif dir_code == "03B8":
        dir_path = sbtc._03B8
    elif dir_code == "03B9":
        dir_path = sbtc._03B9
    elif dir_code == "03B10":
        dir_path = sbtc._03B10
    elif dir_code == "03B11":
        dir_path = sbtc._03B11
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03b-Ended # ic_03c-Started


def ic_03c(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03C1":
        dir_path = sbtc._03C1
    elif dir_code == "03C2":
        dir_path = sbtc._03C2
    elif dir_code == "03C3":
        dir_path = sbtc._03C3
    elif dir_code == "03C4":
        dir_path = sbtc._03C4
    else:
        if re.match("^03C1", dir_code):
            dir_path = ic_03c1(dir_code)
        elif re.match("^03C2", dir_code):
            dir_path = ic_03c2(dir_code)
        elif re.match("^03C3", dir_code):
            dir_path = ic_03c3(dir_code)
        elif re.match("^03C4", dir_code):
            dir_path = ic_03c4(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03c-Ended


def ic_03c1(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03C1A":
        dir_path = sbtc._03C1A
    elif dir_code == "03C1B":
        dir_path = sbtc._03C1B
    elif dir_code == "03C1C":
        dir_path = sbtc._03C1C
    else:
        if re.match("^03C1A", dir_code):
            dir_path = ic_03c1a(dir_code)
        elif re.match("^03C1B", dir_code):
            dir_path = ic_03c1b(dir_code)
        elif re.match("^03C1C", dir_code):
            dir_path = ic_03c1c(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03c1a-Started


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


# ic_03c1a_part_1-Started


def ic_03c1a_part_1(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03C1A1":
        dir_path = sbtc._03C1A1
    elif dir_code == "03C1A2":
        dir_path = sbtc._03C1A2
    elif dir_code == "03C1A3":
        dir_path = sbtc._03C1A3
    elif dir_code == "03C1A4":
        dir_path = sbtc._03C1A4
    elif dir_code == "03C1A5":
        dir_path = sbtc._03C1A5
    elif dir_code == "03C1A6":
        dir_path = sbtc._03C1A6
    elif dir_code == "03C1A7":
        dir_path = sbtc._03C1A7
    elif dir_code == "03C1A8":
        dir_path = sbtc._03C1A8
    elif dir_code == "03C1A9":
        dir_path = sbtc._03C1A9
    elif dir_code == "03C1A10":
        dir_path = sbtc._03C1A10
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03c1a_part_1-Ended # ic_03c1a_part_2-Started


def ic_03c1a_part_2(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03C1A11":
        dir_path = sbtc._03C1A11
    elif dir_code == "03C1A12":
        dir_path = sbtc._03C1A12
    elif dir_code == "03C1A13":
        dir_path = sbtc._03C1A13
    elif dir_code == "03C1A14":
        dir_path = sbtc._03C1A14
    elif dir_code == "03C1A15":
        dir_path = sbtc._03C1A15
    elif dir_code == "03C1A16":
        dir_path = sbtc._03C1A16
    elif dir_code == "03C1A17":
        dir_path = sbtc._03C1A17
    elif dir_code == "03C1A18":
        dir_path = sbtc._03C1A18
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03c1a_part_2-Ended # ic_03c1a-Ended # ic_03c1b-Started


def ic_03c1b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03C1B1":
        dir_path = sbtc._03C1B1
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03c1b-Ended # ic_03c1c-Started


def ic_03c1c(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03C1C1":
        dir_path = sbtc._03C1C1
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03c1c-Ended # ic_03c1-Ended # ic_03c2-Started


def ic_03c2(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03C2A":
        dir_path = sbtc._03C2A
    elif dir_code == "03C2B":
        dir_path = sbtc._03C2B
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03c2-Ended # ic_03c3-Started


def ic_03c3(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03C3A":
        dir_path = sbtc._03C3A
    elif dir_code == "03C3B":
        dir_path = sbtc._03C3B
    else:
        if re.match("^03C3A", dir_code):
            dir_path = ic_03c3a(dir_code)
        elif re.match("^03C3B", dir_code):
            dir_path = ic_03c3b(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03c3a-Started


def ic_03c3a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03C3A1":
        dir_path = sbtc._03C3A1
    elif dir_code == "03C3A2":
        dir_path = sbtc._03C3A2
    elif dir_code == "03C3A3":
        dir_path = sbtc._03C3A3
    elif dir_code == "03C3A4":
        dir_path = sbtc._03C3A4
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03c3a-Ended # ic_03c3b-Started


def ic_03c3b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03C3B1":
        dir_path = sbtc._03C3B1
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03c3b-Ended # ic_03c3-Ended # ic_03c4-Started


def ic_03c4(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03C4A":
        dir_path = sbtc._03C4A
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03c4-Ended # ic_03c-Ended # ic_03d-Started


def ic_03d(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "03D1":
        dir_path = sbtc._03D1
    elif dir_code == "03D2":
        dir_path = sbtc._03D2
    elif dir_code == "03D3":
        dir_path = sbtc._03D3
    elif dir_code == "03D4":
        dir_path = sbtc._03D4
    elif dir_code == "03D5":
        dir_path = sbtc._03D5
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_03d-Ended # ic_03-Ended # 03-Ended # 04-Started # ic_04-Started


def ic_04(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "04A":
        dir_path = sbtc._04A
    elif dir_code == "04B":
        dir_path = sbtc._04B
    elif dir_code == "04C":
        dir_path = sbtc._04C
    # elif dir_code == "04D":
    # dir_path = sbtc._04D
    else:
        if re.match("^04A", dir_code):
            dir_path = ic_04a(dir_code)
        elif re.match("^04C", dir_code):
            dir_path = ic_04c(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


# ic_04A-Started


def ic_04a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "04A1":
        dir_path = sbtc._04A1
    elif dir_code == "04A2":
        dir_path = sbtc._04A2
    elif dir_code == "04A3":
        dir_path = sbtc._04A3
    elif dir_code == "04A4":
        dir_path = sbtc._04A4
    elif dir_code == "04A5":
        dir_path = sbtc._04A5
    elif dir_code == "04A6":
        dir_path = sbtc._04A6
    elif dir_code == "04A7":
        dir_path = sbtc._04A7
    elif dir_code == "04A99":
        dir_path = sbtc._04A99
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_04A-Ended # ic_04C-Started


def ic_04c(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "04C1":
        dir_path = sbtc._04C1
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# ic_04C-Ended # ic_04-Ended # 04-Ended # 05-Started


def ic_05(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """
    if dir_code == "05A":
        dir_path = sbtc._05A
    elif dir_code == "05B":
        dir_path = sbtc._05B
    elif dir_code == "05C":
        dir_path = sbtc._05C
    elif dir_code == "05D":
        dir_path = sbtc._05D
    elif dir_code == "05E":
        dir_path = sbtc._05E
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# 05-Ended # 06-Started


def ic_06(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "06A":
        dir_path = sbtc._06A
    elif dir_code == "06B":
        dir_path = sbtc._06B
    elif dir_code == "06C":
        dir_path = sbtc._06C
    elif dir_code == "06D":
        dir_path = sbtc._06D
    elif dir_code == "06E":
        dir_path = sbtc._06E
    else:
        if re.match("^06A", dir_code):
            dir_path = ic_06a(dir_code)
        elif re.match("^06B", dir_code):
            dir_path = ic_06b(dir_code)
        # elif re.match("^06C", dir_code):
        # dir_path = ic_06c(dir_code)
        # elif re.match("^06D", dir_code):
        # dir_path = ic_06d(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


def ic_06a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "06A1":
        dir_path = sbtc._06A1
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


def ic_06b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "06B1":
        dir_path = sbtc._06B1
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# def ic_06c(dir_code):
# """
# Takes dir_code as input and returns the absolute directory path of the code.
# """
# global dir_path
# if dir_code == "06C1":
#    dir_path = sbtc._06C1
# elif dir_code == "06C2":
#    dir_path = sbtc._06C2
# else:
#    dir_path = DIR_NOT_FOUND
# return dir_path


# def ic_06d(dir_code):
# """
# Takes dir_code as input and returns the absolute directory path of the code.
# """
# global dir_path
# if dir_code == "06D1":
#   dir_path = sbtc._06D1
# elif dir_code == "06D2":
#   dir_path = sbtc._06D2
# elif dir_code == "06D3":
#   dir_path = sbtc._06D3
# else:
#   dir_path = DIR_NOT_FOUND
# return dir_path
# 06-Ended # 07-Started


def ic_07(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "07A":
        dir_path = sbtc._07A
    elif dir_code == "07B":
        dir_path = sbtc._07B
    else:
        if re.match("^07A", dir_code):
            dir_path = ic_07a(dir_code)
        elif re.match("^07B", dir_code):
            dir_path = ic_07b(dir_code)
        else:
            dir_path = DIR_NOT_FOUND
    return dir_path


def ic_07a(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "07A1":
        dir_path = sbtc._07A1
    elif dir_code == "07A2":
        dir_path = sbtc._07A2
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


def ic_07b(dir_code):
    """
    Takes dir_code as input and returns the absolute directory path of the code.
    """

    if dir_code == "07B1":
        dir_path = sbtc._07B1
    else:
        dir_path = DIR_NOT_FOUND
    return dir_path


# 07-Ended


"""
Testing stuff realtime.
"""


def directories_test():
    """
    Manual Testing apart from pytest to be 100% sure
    that the fx returns correct directory.
    """
    test_code = input("Please enter the code to test: ")
    if test_code == "Quit":
        print("Testing Completed, Exiting....")
        sys.exit()
    else:
        print(initial_check(test_code))
    directories_test()


# directories_test()
