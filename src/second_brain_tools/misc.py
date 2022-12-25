"""
This module contains all the functions which are miscellaneous by nature.
Which means they are either very micro and/or too micro to hold somewhere else.
"""
import os
import random
import re
from second_brain_tools.defaults import NO_MARKDOWN_FILE
from rich.console import Console
from second_brain_tools.config import SECOND_BRAIN_DIRECTORY
from rich.markdown import Markdown
from rich import print
from second_brain_tools.directories import initial_check


def file_name_check(fnc_name):
    """
    Takes file name and checks if it is empty or not and mark it as valid/invalid.
    returns false if invalid, else True if valid.
    """
    fnc_check = len(fnc_name)
    if fnc_check == "0":
        result = False
    else:
        result = True
    return result


def file_creation(file_location, file_content):
    with open(file_location, 'a+') as qc_object:
        qc_object.write(file_content)


def random_file_from_dir(rffd_dir_code):
    rffd_dir = initial_check(rffd_dir_code)
    random_file = choose_random_markdown_file(rffd_dir)
    view_note_with_dir(random_file)
    return


def choose_random_markdown_file(dir_path):
    # Get a list of all markdown files in the directory
    working_dir = SECOND_BRAIN_DIRECTORY + dir_path
    markdown_files = [f for f in os.listdir(working_dir) if f.endswith('.md')]

    # Choose a random file from the list
    try:
        chosen_file = random.choice(markdown_files)
    except IndexError:
        chosen_file = "The index is out of range!"
    # Return the full path to the chosen file
    return os.path.join(working_dir, chosen_file)


def view_note_with_dir(vnwd_dir):
    if vnwd_dir == '/home/rohan/Vaults/SBT_TOOLS_TESTING/04_Evergreen/04A_Network/The index is out of range!':
        print(NO_MARKDOWN_FILE)
    elif vnwd_dir:
        with open(vnwd_dir, "r") as vnwd_obj:
            content = vnwd_obj.read()
            console = Console()
            console.print(Markdown(content))
    else:
        print(NO_MARKDOWN_FILE)


def check_ending_char(string):
    return bool(re.search(r'[1-9]$', string))


"""
def get_dir_existence_percentage(dirs):
    # Count the number of directories that exist
    num_dirs_exist = 0
    for dir in dirs:
        if os.path.isdir(dir):
            num_dirs_exist += 1

    # Calculate the percentage of directories that exist
    percentage = (num_dirs_exist / len(dirs)) * 100

    return percentage
"""
