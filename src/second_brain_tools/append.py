# Importing production modules // Meant for production branch
from second_brain_tools.config import PLAIN_TEXT_TIME_INCLUDE, TIME_APPEND_TEXT, CURRENT_TIME, LIST_TIME_INCLUDE
from second_brain_tools.directories import initial_check
from rich import print
# Importing production modules finished

# Default strings assignation Started

# Plain text specific
pta_include_time = PLAIN_TEXT_TIME_INCLUDE
# List Specific
list_append_time = LIST_TIME_INCLUDE

# Default strings assignation Finished


def paragraph_append(note_path, note_content):
    with open(note_path, 'a+') as pa_object:
        pa_object.write(f" {note_content}")


def plain_text_append(note_path, note_content, pta_include_time):
    if pta_include_time is True:
        opener = TIME_APPEND_TEXT + " " + CURRENT_TIME
        with open(note_path, 'a+') as pta_object:
            pta_object.write("\n")
            # pta_object.write("---\n")
            pta_object.write(opener)
            pta_object.write("\n")
            pta_object.write(note_content + "\n\n")
            pta_object.write("---\n")
            pta_object.write("\n")
    else:
        with open(note_path, 'a+') as pta_object:
            pta_object.write("\n")
            # pta_object.write("---\n")
            pta_object.write("\n")
            pta_object.write(note_content + "\n\n")
            pta_object.write("---\n")
            pta_object.write("\n")


def bullet_list_append(note_path, note_content, list_include_time):
    if list_include_time is True:
        with open(note_path, 'a+') as bla_object:
            bla_object.write(f" * {note_content} (at {CURRENT_TIME}) \n")
    else:
        with open(note_path, 'a+') as bla_object:
            bla_object.writelines(f" * {note_content} \n")


def table_append(note_path, note_content):
    with open(note_path, 'a+') as ta_object:
        last_line_check = table_append_last_line_check(note_path, note_content)
        if last_line_check is False:
            ta_object.write("| You Logged -> | on |\n")
            ta_object.write("| ------------- | ----- |\n")
            ta_object.write(f"|{note_content}| {CURRENT_TIME} | \n")
        else:
            ta_object.write(f"|{note_content}| {CURRENT_TIME} | \n")


def table_append_last_line_check(note_path, note_content):
    with open(note_path, 'r') as tallc_object:
        # Read the contents of the file
        contents = tallc_object.read()
        # Split the contents into a list of lines
        lines = contents.split('\n')
        # Iterate over the lines in reverse order
        for line in reversed(lines):
            # Skip empty lines
            if line == '':
                continue
            # Return True if the line matches the given string
            if line == "| ------------- | ----- |":
                return True
        # Return False if no non-empty line is found
        return False


# Append to a note
def append_note(append_type, note_dir_code, note_name, note_content, include_time):
    note_path = initial_check(note_dir_code) + note_name
    if append_type == "paragraph" or "Paragraph" or "PARAGRAPH":
        paragraph_append(note_path, note_content)
    elif append_type == "list" or "LIST" or "List":
        bullet_list_append(note_path, note_content, include_time)
    elif append_type == "plain_text" or "PLAIN_TEXT" or "Plain_Text":
        plain_text_append(note_path, note_content, include_time)
    elif append_type == "table" or "Table" or "TABLE":
        table_append(note_path, note_content)
    else:
        print("Error")
