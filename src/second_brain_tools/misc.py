"""
This module contains all the functions which are miscellaneous by nature.
Which means they are either very micro and/or too micro to hold somewhere else.
"""
import os
import random as rand
from second_brain_tools.directories import initial_check
from second_brain_tools.defaults import NO_MARKDOWN_FILE
from rich.console import Console
from rich.markdown import Markdown


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
    rffd_dir = initial_check("01A1")
    all_files = []
    for root, dirs, files in os.walk(rffd_dir):
        for file in files:
            all_files.append(os.path.join(root, file))
    md_files = [f for f in all_files if f.endswith(".md")]
    if md_files:
        return rand.choice(md_files)
    else:
        return None


def view_note_with_dir(vnwd_dir):
    vnwd_file_path = random_file_from_dir(vnwd_dir)
    if vnwd_file_path:
        with open(vnwd_file_path, "r") as vnwd_obj:
            content = vnwd_obj.read()
            console = Console()
            console.print(Markdown(content))
    else:
        print(NO_MARKDOWN_FILE)


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
