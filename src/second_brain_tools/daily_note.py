# Importing production modules // Meant for production branch
from dotenv import load_dotenv
from os.path import exists
from second_brain_tools.config import Today, PLAIN_TEXT_TIME_INCLUDE, LIST_TIME_INCLUDE, DNM_APPEND_TYPE, GLOBAL_APPEND_TYPE, SECOND_BRAIN_DIRECTORY, FILE_ALREADY_EXIST, DNM_FILE_CONTENT_CREATION  # noqa: E501
from second_brain_tools.directories import initial_check
from second_brain_tools.append import plain_text_append, bullet_list_append, table_append
# Importing production modules finished

# Default Functions Calling
load_dotenv(".sbt_config")
# Default Functions Calling

# Default variable assignation started.

# Default variable assignation completed


def daily_note_moc_location():
    sbd = SECOND_BRAIN_DIRECTORY
    dnm_directory = initial_check("01C1A")
    dnm_location = sbd + dnm_directory + Today + ".md"
    return dnm_location


def daily_note_moc_pregenerate_check():
    dnm_location = daily_note_moc_location()
    dnm_file_exist_check = exists(dnm_location)
    if dnm_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_moc_generate(dnm_location)


def daily_note_moc_generate(dnm_location):
    """
    """
    with open(dnm_location, 'a+') as dnm_file_obj:
        dnm_file_obj.write(DNM_FILE_CONTENT_CREATION)


def daily_note_append(note_content, include_time=True):
    """
    Appends to daily note moc.
    """

    dnm_location = daily_note_moc_location()
    if DNM_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnm_location, note_content, include_time)
        else:
            plain_text_append(dnm_location, note_content, include_time)

    elif DNM_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnm_location, note_content, include_time)
        else:
            bullet_list_append(dnm_location, note_content, include_time)

    elif DNM_APPEND_TYPE == "Table":
        table_append(dnm_location, note_content)

    if not DNM_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnm_location, note_content, include_time)
            else:
                plain_text_append(dnm_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnm_location, note_content, include_time)
            else:
                bullet_list_append(dnm_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnm_location, note_content)


# Testing below
def test():
    daily_note_moc_pregenerate_check()
    daily_note_append("Hello new entry")


test()
