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
    """
    paragraph_append: Appends a new paragraph to a file.

    This function appends a new paragraph to the end of a file.

    Args:
    note_path (str): The path to the file.
    note_content (str): The content of the new paragraph to be appended.

    Returns:
    None
    """
    with open(note_path, 'a+') as pa_object:
        pa_object.write(f" {note_content}")


def plain_text_append(note_path, note_content, pta_include_time):
    """
    plain_text_append: Appends plain text to a file.

    This function appends plain text to the end of a file. The user can choose to include the current time in the text.

    Args:
    note_path (str): The path to the file.
    note_content (str): The plain text to be appended.
    pta_include_time (bool): Whether to include the current time in the text.

    Returns:
    None"""
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
    """
    bullet_list_append: Appends a bullet point to a list in a file.

    This function appends a bullet point to a list in a file. The user can choose to include the current time in the bullet point.

    Args:
    note_path (str): The path to the file.
    note_content (str): The content of the bullet point to be appended.
    list_include_time (bool): Whether to include the current time in the bullet point.

    Returns:
    None"""
    if list_include_time is True:
        with open(note_path, 'a+') as bla_object:
            bla_object.write(f" * {note_content} (at {CURRENT_TIME}) \n")
    else:
        with open(note_path, 'a+') as bla_object:
            bla_object.writelines(f" * {note_content} \n")


def table_append(note_path, note_content):
    """
    table_append: Appends a new row to a table in a file.

    This function appends a new row to a table in a file.
    The new row consists of a single column containing the given content and a second column containing the current time.

    Args:
    note_path (str): The path to the file.
    note_content (str): The content to be added to the first column of the new row.

    Returns:
    None"""
    with open(note_path, 'a+') as ta_object:
        last_line_check = table_append_last_line_check(note_path, note_content)
        if last_line_check is False:
            ta_object.write("| You Logged -> | on |\n")
            ta_object.write("| ------------- | ----- |\n")
            ta_object.write(f"|{note_content}| {CURRENT_TIME} | \n")
        else:
            ta_object.write(f"|{note_content}| {CURRENT_TIME} | \n")


def table_append_last_line_check(note_path, note_content):
    """
        table_append_last_line_check: Checks the last line of a file for a specific string.

    This function checks the last non-empty line of a file for a specific string.

    Args:
    note_path (str): The path to the file.
    note_content (str): The string to search for.

    Returns:
    bool: True if the string is found, False otherwise.
    """
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
    """
    append_note: Appends content to a file in a specified format.

    This function appends content to a file in a specified format.
    The available formats are "paragraph", "list", "plain_text", and "table".
    The user can choose to include the current time in the content.

    Args:
    append_type (str): The format for the content.
    note_dir_code (str): The code for the directory containing the file.
    note_name (str): The name of the file.
    note_content (str): The content to be appended.
    include_time (bool): Whether to include the current time in the content.

    Returns:
    None
    """
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
