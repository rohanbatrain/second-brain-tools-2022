# importing modules started
import os
from second_brain_tools.directories import initial_check
from second_brain_tools.config import SECOND_BRAIN_DIRECTORY
from rich.console import Console
from rich.markdown import Markdown
# importing modules finished


def create_note(dir_code, note_name, note_body):
    note_path = SECOND_BRAIN_DIRECTORY + initial_check(dir_code) + note_name + ".md"
    with open(note_path, 'w') as cn_obj_1:
        cn_obj_1.write(note_body)


def delete_note(dir_code, note_name):
    note_path = SECOND_BRAIN_DIRECTORY + initial_check(dir_code) + note_name + ".md"
    print(f"Caution, You are deleting a file at \n {note_path}")
    choice = input("Are you sure, you want to delte this file?(Y/N): ")
    if choice == "Y":
        os.remove(note_path)
    elif choice == "N":
        print("Aborting!!!")


def move_note(old_dir_code, new_dir_code, note_name):
    odc_note_path = SECOND_BRAIN_DIRECTORY + initial_check(old_dir_code) + note_name + ".md"
    ndc_note_path = SECOND_BRAIN_DIRECTORY + initial_check(new_dir_code) + note_name + ".md"
    os.replace(odc_note_path, ndc_note_path)


def view_note(dir_code, note_name):
    note_path = SECOND_BRAIN_DIRECTORY + initial_check(dir_code) + note_name + ".md"
    with open(note_path, 'r') as vn:
        content = vn.read()
        console = Console()
        console.print(Markdown(content))
