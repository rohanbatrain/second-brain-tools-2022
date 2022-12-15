# Importing production modules // Meant for production branch
from dotenv import load_dotenv
from os.path import exists
from second_brain_tools.time import Today
from second_brain_tools.config import PLAIN_TEXT_TIME_INCLUDE, LIST_TIME_INCLUDE, SECOND_BRAIN_DIRECTORY, FILE_ALREADY_EXIST
from second_brain_tools.directories import initial_check
from second_brain_tools.append import plain_text_append, bullet_list_append, table_append, paragraph_append
# Importing production modules FINISHED

# Default Append Strings Import Started
from second_brain_tools.config import DNM_APPEND_TYPE, DNBJ_APPEND_TYPE,  DNC_APPEND_TYPE,  DNE_APPEND_TYPE,  DNL_APPEND_TYPE,  DNR_APPEND_TYPE,  DNR2_APPEND_TYPE,  DNT_APPEND_TYPE,  DNT2_APPEND_TYPE,  DNTE_APPEND_TYPE,  dntt_APPEND_TYPE,  DNTL_APPEND_TYPE,  DNTM_APPEND_TYPE,  DNTM2_APPEND_TYPE,  DNTM3_APPEND_TYPE,  DNTS_APPEND_TYPE,  DNTS2_APPEND_TYPE,  DNTW_APPEND_TYPE, GLOBAL_APPEND_TYPE, DNR2_HOUR_00_APPEND_TYPE, DNR2_HOUR_01_APPEND_TYPE, DNR2_HOUR_02_APPEND_TYPE, DNR2_HOUR_03_APPEND_TYPE, DNR2_HOUR_04_APPEND_TYPE, DNR2_HOUR_05_APPEND_TYPE, DNR2_HOUR_06_APPEND_TYPE, DNR2_HOUR_07_APPEND_TYPE, DNR2_HOUR_08_APPEND_TYPE, DNR2_HOUR_09_APPEND_TYPE, DNR2_HOUR_10_APPEND_TYPE, DNR2_HOUR_11_APPEND_TYPE, DNR2_HOUR_12_APPEND_TYPE, DNR2_HOUR_13_APPEND_TYPE, DNR2_HOUR_14_APPEND_TYPE, DNR2_HOUR_15_APPEND_TYPE, DNR2_HOUR_16_APPEND_TYPE, DNR2_HOUR_17_APPEND_TYPE, DNR2_HOUR_18_APPEND_TYPE, DNR2_HOUR_19_APPEND_TYPE, DNR2_HOUR_20_APPEND_TYPE, DNR2_HOUR_21_APPEND_TYPE, DNR2_HOUR_22_APPEND_TYPE, DNR2_HOUR_23_APPEND_TYPE  # noqa
# Default Append Strings Import FINISHED

# Default Content_Creation Strings Import Started
from second_brain_tools.config import DNBJ_FILE_CONTENT_CREATION, DNC_FILE_CONTENT_CREATION, DNE_FILE_CONTENT_CREATION, DNL_FILE_CONTENT_CREATION, DNR_FILE_CONTENT_CREATION, DNR2_FILE_CONTENT_CREATION, DNT_FILE_CONTENT_CREATION, DNT2_FILE_CONTENT_CREATION, DNTE_FILE_CONTENT_CREATION, dntt_FILE_CONTENT_CREATION, DNTL_FILE_CONTENT_CREATION, DNTM_FILE_CONTENT_CREATION, DNTM2_FILE_CONTENT_CREATION, DNTM3_FILE_CONTENT_CREATION, DNTS_FILE_CONTENT_CREATION, DNTS2_FILE_CONTENT_CREATION, DNTW_FILE_CONTENT_CREATION, DNM_FILE_CONTENT_CREATION, DNR2_HOUR_00_FILE_CONTENT_CREATION, DNR2_HOUR_01_FILE_CONTENT_CREATION, DNR2_HOUR_02_FILE_CONTENT_CREATION, DNR2_HOUR_03_FILE_CONTENT_CREATION, DNR2_HOUR_04_FILE_CONTENT_CREATION, DNR2_HOUR_05_FILE_CONTENT_CREATION, DNR2_HOUR_06_FILE_CONTENT_CREATION, DNR2_HOUR_07_FILE_CONTENT_CREATION, DNR2_HOUR_08_FILE_CONTENT_CREATION, DNR2_HOUR_09_FILE_CONTENT_CREATION, DNR2_HOUR_10_FILE_CONTENT_CREATION, DNR2_HOUR_11_FILE_CONTENT_CREATION, DNR2_HOUR_12_FILE_CONTENT_CREATION, DNR2_HOUR_13_FILE_CONTENT_CREATION, DNR2_HOUR_14_FILE_CONTENT_CREATION, DNR2_HOUR_15_FILE_CONTENT_CREATION, DNR2_HOUR_16_FILE_CONTENT_CREATION, DNR2_HOUR_17_FILE_CONTENT_CREATION, DNR2_HOUR_18_FILE_CONTENT_CREATION, DNR2_HOUR_19_FILE_CONTENT_CREATION, DNR2_HOUR_20_FILE_CONTENT_CREATION, DNR2_HOUR_21_FILE_CONTENT_CREATION, DNR2_HOUR_22_FILE_CONTENT_CREATION, DNR2_HOUR_23_FILE_CONTENT_CREATION  # noqa: E501
# Default Content_Creation Strings Import FINISHED


# Default Functions Calling
load_dotenv(".sbt_config")
# Default Functions Calling


# MOC RELATED FUNCTIONS STARTED
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


def daily_note_moc_append(note_content, include_time=True):
    """
    Appends to daily note moc.
    """

    dnm_location = daily_note_moc_location()

    if DNM_APPEND_TYPE == "Paragraph":
        paragraph_append(dnm_location, note_content)

    elif DNM_APPEND_TYPE == "Plain_Text":
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
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnm_location, note_content)
        else:
            print("Error")
# MOC RELATED FUNCTIONS FINISHED


# Bullet-Journal RELATED FUNCTIONS STARTED


def daily_note_bullet_journal_append(note_content, include_time=True):
    """
    appends to
    """
    dnbj_location = daily_note_bullet_journal_location()

    if DNBJ_APPEND_TYPE == "Paragraph":
        paragraph_append(dnbj_location, note_content)

    elif DNBJ_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnbj_location, note_content, include_time)
        else:
            plain_text_append(dnbj_location, note_content, include_time)

    elif DNBJ_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnbj_location, note_content, include_time)
        else:
            bullet_list_append(dnbj_location, note_content, include_time)

    elif DNBJ_APPEND_TYPE == "Table":
        table_append(dnbj_location, note_content)

    if not DNBJ_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnbj_location, note_content, include_time)
            else:
                plain_text_append(dnbj_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnbj_location, note_content, include_time)
            else:
                bullet_list_append(dnbj_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnbj_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnbj_location, note_content)
        else:
            print("Error")


def daily_note_bullet_journal_generate(dnbj_location):
    """

    """
    with open(dnbj_location, 'a+') as dnbj_file_obj:
        dnbj_file_obj.write(DNBJ_FILE_CONTENT_CREATION)


def daily_note_bullet_journal_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnbj_directory = initial_check("01C1B1")
    dnbj_location = sbd + dnbj_directory + Today + "_Bullet_Journal" + ".md"
    return dnbj_location


def daily_note_bullet_journal_pregenerate_check():
    """

    """
    dnbj_location = daily_note_bullet_journal_location()
    dnbj_file_exist_check = exists(dnbj_location)
    if dnbj_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_bullet_journal_generate(dnbj_location)


# Bullet-Journal RELATED FUNCTIONS FINISHED  # Connections RELATED FUNCTIONS STARTED

def daily_note_connections_append(note_content, include_time=True):
    """
    appends to
    """
    dnc_location = daily_note_connections_location()

    if DNC_APPEND_TYPE == "Paragraph":
        paragraph_append(dnc_location, note_content)

    elif DNC_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnc_location, note_content, include_time)
        else:
            plain_text_append(dnc_location, note_content, include_time)

    elif DNC_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnc_location, note_content, include_time)
        else:
            bullet_list_append(dnc_location, note_content, include_time)

    elif DNC_APPEND_TYPE == "Table":
        table_append(dnc_location, note_content)

    if not DNC_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnc_location, note_content, include_time)
            else:
                plain_text_append(dnc_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnc_location, note_content, include_time)
            else:
                bullet_list_append(dnc_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnc_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnc_location, note_content)
        else:
            print("Error")


def daily_note_connections_generate(dnc_location):
    """

    """
    with open(dnc_location, 'a+') as dnc_file_obj:
        dnc_file_obj.write(DNC_FILE_CONTENT_CREATION)


def daily_note_connections_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnc_directory = initial_check("01C1C")
    dnc_location = sbd + dnc_directory + Today + "_Connections" + ".md"
    return dnc_location


def daily_note_connections_pregenerate_check():
    """

    """
    dnc_location = daily_note_connections_location()
    dnc_file_exist_check = exists(dnc_location)
    if dnc_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_connections_generate(dnc_location)


# Connections RELATED FUNCTIONS FINISHED  # Events RELATED FUNCTIONS STARTED


def daily_note_events_append(note_content, include_time=True):
    """
    appends to
    """
    dne_location = daily_note_events_location()

    if DNE_APPEND_TYPE == "Paragraph":
        paragraph_append(dne_location, note_content)

    elif DNE_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dne_location, note_content, include_time)
        else:
            plain_text_append(dne_location, note_content, include_time)

    elif DNE_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dne_location, note_content, include_time)
        else:
            bullet_list_append(dne_location, note_content, include_time)

    elif DNE_APPEND_TYPE == "Table":
        table_append(dne_location, note_content)

    if not DNE_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dne_location, note_content, include_time)
            else:
                plain_text_append(dne_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dne_location, note_content, include_time)
            else:
                bullet_list_append(dne_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dne_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dne_location, note_content)
        else:
            print("Error")


def daily_note_events_generate(dne_location):
    """

    """
    with open(dne_location, 'a+') as dne_file_obj:
        dne_file_obj.write(DNE_FILE_CONTENT_CREATION)


def daily_note_events_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dne_directory = initial_check("01C1D")
    dne_location = sbd + dne_directory + Today + "_" + ".md"
    return dne_location


def daily_note_events_pregenerate_check():
    """

    """
    dne_location = daily_note_events_location()
    dne_file_exist_check = exists(dne_location)
    if dne_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_events_generate(dne_location)


# Events RELATED FUNCTIONS FINISHED  # Location RELATED FUNCTIONS STARTED


def daily_note_location_append(note_content, include_time=True):
    """
    appends to
    """
    dnl_location = daily_note_location_location()

    if DNL_APPEND_TYPE == "Paragraph":
        paragraph_append(dnl_location, note_content)

    elif DNL_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnl_location, note_content, include_time)
        else:
            plain_text_append(dnl_location, note_content, include_time)

    elif DNL_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnl_location, note_content, include_time)
        else:
            bullet_list_append(dnl_location, note_content, include_time)

    elif DNL_APPEND_TYPE == "Table":
        table_append(dnl_location, note_content)

    if not DNL_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnl_location, note_content, include_time)
            else:
                plain_text_append(dnl_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnl_location, note_content, include_time)
            else:
                bullet_list_append(dnl_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnl_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnl_location, note_content)
        else:
            print("Error")


def daily_note_location_generate(dnl_location):
    """

    """
    with open(dnl_location, 'a+') as dnl_file_obj:
        dnl_file_obj.write(DNL_FILE_CONTENT_CREATION)


def daily_note_location_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnl_directory = initial_check("01C1E")
    dnl_location = sbd + dnl_directory + Today + "_" + ".md"
    return dnl_location


def daily_note_location_pregenerate_check():
    """

    """
    dnl_location = daily_note_location_location()
    dnl_file_exist_check = exists(dnl_location)
    if dnl_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_location_generate(dnl_location)

# Location RELATED FUNCTIONS FINISHED  # Reminders RELATED FUNCTIONS STARTED


def daily_note_reminders_append(note_content, include_time=True):
    """
    appends to
    """

    dnr_location = daily_note_reminders_location()

    if DNR_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr_location, note_content)

    elif DNR_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr_location, note_content, include_time)
        else:
            plain_text_append(dnr_location, note_content, include_time)

    elif DNR_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr_location, note_content, include_time)
        else:
            bullet_list_append(dnr_location, note_content, include_time)

    elif DNR_APPEND_TYPE == "Table":
        table_append(dnr_location, note_content)

    if not DNR_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr_location, note_content, include_time)
            else:
                plain_text_append(dnr_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr_location, note_content, include_time)
            else:
                bullet_list_append(dnr_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr_location, note_content)
        else:
            print("Error")


def daily_note_reminders_generate(dnr_location):
    """

    """
    with open(dnr_location, 'a+') as dnr_file_obj:
        dnr_file_obj.write(DNR_FILE_CONTENT_CREATION)


def daily_note_reminders_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr_directory = initial_check("01C1F")
    dnr_location = sbd + dnr_directory + Today + "_" + ".md"
    return dnr_location


def daily_note_reminders_pregenerate_check():
    """

    """
    dnr_location = daily_note_reminders_location()
    dnr_file_exist_check = exists(dnr_location)
    if dnr_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_reminders_generate(dnr_location)

# Reminders RELATED FUNCTIONS FINISHED  # Routine RELATED FUNCTIONS STARTED


def daily_note_routine_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_location = daily_note_routine_location()

    if DNR2_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_location, note_content)

    elif DNR2_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_location, note_content, include_time)
        else:
            plain_text_append(dnr2_location, note_content, include_time)

    elif DNR2_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_location, note_content, include_time)

    elif DNR2_APPEND_TYPE == "Table":
        table_append(dnr2_location, note_content)

    if not DNR2_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_location, note_content, include_time)
            else:
                plain_text_append(dnr2_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_location, note_content)
        else:
            print("Error")


def daily_note_routine_generate(dnr2_location):
    """

    """
    with open(dnr2_location, 'a+') as dnr2_file_obj:
        dnr2_file_obj.write(DNR2_FILE_CONTENT_CREATION)


def daily_note_routine_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_directory = initial_check("01C1G25")
    dnr2_location = sbd + dnr2_directory + Today + "_" + ".md"
    return dnr2_location


def daily_note_routine_pregenerate_check():
    """

    """
    dnr2_location = daily_note_routine_location()
    dnr2_file_exist_check = exists(dnr2_location)
    if dnr2_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_generate(dnr2_location)


# Routine Hourly FUNCTIONS STARTED # Routine Hour_00 FUNCTIONS STARTED
def daily_note_routine_hour_00_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_00_location = daily_note_routine_hour_00_location()

    if DNR2_HOUR_00_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_00_location, note_content)

    elif DNR2_HOUR_00_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_00_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_00_location, note_content, include_time)

    elif DNR2_HOUR_00_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_00_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_00_location, note_content, include_time)

    elif DNR2_HOUR_00_APPEND_TYPE == "Table":
        table_append(dnr2_hour_00_location, note_content)

    if not DNR2_HOUR_00_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_00_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_00_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_00_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_00_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_00_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_00_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_00_generate(dnr2_hour_00_location):
    """
    """
    with open(dnr2_hour_00_location, 'a+') as dnr2_hour_00_file_obj:
        dnr2_hour_00_file_obj.write(DNR2_HOUR_00_FILE_CONTENT_CREATION)


def daily_note_routine_hour_00_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_00_directory = initial_check("")
    dnr2_hour_00_location = sbd + dnr2_hour_00_directory + Today + "_" + ".md"
    return dnr2_hour_00_location


def daily_note_routine_hour_00_pregenerate_check():
    """
    """
    dnr2_hour_00_location = daily_note_routine_hour_00_location()
    dnr2_hour_00_file_exist_check = exists(dnr2_hour_00_location)
    if dnr2_hour_00_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_00_generate(dnr2_hour_00_location)


# Routine Hour_00 FUNCTIONS FINISHED # Routine Hour_01 FUNCTIONS STARTED
def daily_note_routine_hour_01_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_01_location = daily_note_routine_hour_01_location()

    if DNR2_HOUR_01_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_01_location, note_content)

    elif DNR2_HOUR_01_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_01_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_01_location, note_content, include_time)

    elif DNR2_HOUR_01_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_01_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_01_location, note_content, include_time)

    elif DNR2_HOUR_01_APPEND_TYPE == "Table":
        table_append(dnr2_hour_01_location, note_content)

    if not DNR2_HOUR_01_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_01_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_01_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_01_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_01_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_01_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_01_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_01_generate(dnr2_hour_01_location):
    """
    """
    with open(dnr2_hour_01_location, 'a+') as dnr2_hour_01_file_obj:
        dnr2_hour_01_file_obj.write(DNR2_HOUR_01_FILE_CONTENT_CREATION)


def daily_note_routine_hour_01_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_01_directory = initial_check("")
    dnr2_hour_01_location = sbd + dnr2_hour_01_directory + Today + "_" + ".md"
    return dnr2_hour_01_location


def daily_note_routine_hour_01_pregenerate_check():
    """
    """
    dnr2_hour_01_location = daily_note_routine_hour_01_location()
    dnr2_hour_01_file_exist_check = exists(dnr2_hour_01_location)
    if dnr2_hour_01_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_01_generate(dnr2_hour_01_location)


# Routine Hour_01 FUNCTIONS FINISHED # Routine Hour_02 FUNCTIONS STARTED
def daily_note_routine_hour_02_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_02_location = daily_note_routine_hour_02_location()

    if DNR2_HOUR_02_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_02_location, note_content)

    elif DNR2_HOUR_02_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_02_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_02_location, note_content, include_time)

    elif DNR2_HOUR_02_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_02_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_02_location, note_content, include_time)

    elif DNR2_HOUR_02_APPEND_TYPE == "Table":
        table_append(dnr2_hour_02_location, note_content)

    if not DNR2_HOUR_02_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_02_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_02_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_02_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_02_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_02_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_02_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_02_generate(dnr2_hour_02_location):
    """
    """
    with open(dnr2_hour_02_location, 'a+') as dnr2_hour_02_file_obj:
        dnr2_hour_02_file_obj.write(DNR2_HOUR_02_FILE_CONTENT_CREATION)


def daily_note_routine_hour_02_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_02_directory = initial_check("")
    dnr2_hour_02_location = sbd + dnr2_hour_02_directory + Today + "_" + ".md"
    return dnr2_hour_02_location


def daily_note_routine_hour_02_pregenerate_check():
    """
    """
    dnr2_hour_02_location = daily_note_routine_hour_02_location()
    dnr2_hour_02_file_exist_check = exists(dnr2_hour_02_location)
    if dnr2_hour_02_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_02_generate(dnr2_hour_02_location)


# Routine Hour_02 FUNCTIONS FINISHED # Routine Hour_03 FUNCTIONS STARTED
def daily_note_routine_hour_03_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_03_location = daily_note_routine_hour_03_location()

    if DNR2_HOUR_03_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_03_location, note_content)

    elif DNR2_HOUR_03_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_03_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_03_location, note_content, include_time)

    elif DNR2_HOUR_03_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_03_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_03_location, note_content, include_time)

    elif DNR2_HOUR_03_APPEND_TYPE == "Table":
        table_append(dnr2_hour_03_location, note_content)

    if not DNR2_HOUR_03_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_03_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_03_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_03_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_03_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_03_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_03_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_03_generate(dnr2_hour_03_location):
    """
    """
    with open(dnr2_hour_03_location, 'a+') as dnr2_hour_03_file_obj:
        dnr2_hour_03_file_obj.write(DNR2_HOUR_03_FILE_CONTENT_CREATION)


def daily_note_routine_hour_03_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_03_directory = initial_check("")
    dnr2_hour_03_location = sbd + dnr2_hour_03_directory + Today + "_" + ".md"
    return dnr2_hour_03_location


def daily_note_routine_hour_03_pregenerate_check():
    """
    """
    dnr2_hour_03_location = daily_note_routine_hour_03_location()
    dnr2_hour_03_file_exist_check = exists(dnr2_hour_03_location)
    if dnr2_hour_03_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_03_generate(dnr2_hour_03_location)


# Routine Hour_03 FUNCTIONS FINISHED # Routine Hour_04 FUNCTIONS STARTED
def daily_note_routine_hour_04_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_04_location = daily_note_routine_hour_04_location()

    if DNR2_HOUR_04_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_04_location, note_content)

    elif DNR2_HOUR_04_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_04_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_04_location, note_content, include_time)

    elif DNR2_HOUR_04_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_04_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_04_location, note_content, include_time)

    elif DNR2_HOUR_04_APPEND_TYPE == "Table":
        table_append(dnr2_hour_04_location, note_content)

    if not DNR2_HOUR_04_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_04_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_04_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_04_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_04_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_04_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_04_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_04_generate(dnr2_hour_04_location):
    """
    """
    with open(dnr2_hour_04_location, 'a+') as dnr2_hour_04_file_obj:
        dnr2_hour_04_file_obj.write(DNR2_HOUR_04_FILE_CONTENT_CREATION)


def daily_note_routine_hour_04_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_04_directory = initial_check("")
    dnr2_hour_04_location = sbd + dnr2_hour_04_directory + Today + "_" + ".md"
    return dnr2_hour_04_location


def daily_note_routine_hour_04_pregenerate_check():
    """
    """
    dnr2_hour_04_location = daily_note_routine_hour_04_location()
    dnr2_hour_04_file_exist_check = exists(dnr2_hour_04_location)
    if dnr2_hour_04_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_04_generate(dnr2_hour_04_location)


# Routine Hour_04 FUNCTIONS FINISHED # Routine Hour_05 FUNCTIONS STARTED
def daily_note_routine_hour_05_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_05_location = daily_note_routine_hour_05_location()

    if DNR2_HOUR_05_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_05_location, note_content)

    elif DNR2_HOUR_05_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_05_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_05_location, note_content, include_time)

    elif DNR2_HOUR_05_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_05_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_05_location, note_content, include_time)

    elif DNR2_HOUR_05_APPEND_TYPE == "Table":
        table_append(dnr2_hour_05_location, note_content)

    if not DNR2_HOUR_05_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_05_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_05_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_05_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_05_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_05_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_05_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_05_generate(dnr2_hour_05_location):
    """
    """
    with open(dnr2_hour_05_location, 'a+') as dnr2_hour_05_file_obj:
        dnr2_hour_05_file_obj.write(DNR2_HOUR_05_FILE_CONTENT_CREATION)


def daily_note_routine_hour_05_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_05_directory = initial_check("")
    dnr2_hour_05_location = sbd + dnr2_hour_05_directory + Today + "_" + ".md"
    return dnr2_hour_05_location


def daily_note_routine_hour_05_pregenerate_check():
    """
    """
    dnr2_hour_05_location = daily_note_routine_hour_05_location()
    dnr2_hour_05_file_exist_check = exists(dnr2_hour_05_location)
    if dnr2_hour_05_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_05_generate(dnr2_hour_05_location)


# Routine Hour_05 FUNCTIONS FINISHED

# Routine Hour_06 FUNCTIONS STARTED
def daily_note_routine_hour_06_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_06_location = daily_note_routine_hour_06_location()

    if DNR2_HOUR_06_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_06_location, note_content)

    elif DNR2_HOUR_06_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_06_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_06_location, note_content, include_time)

    elif DNR2_HOUR_06_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_06_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_06_location, note_content, include_time)

    elif DNR2_HOUR_06_APPEND_TYPE == "Table":
        table_append(dnr2_hour_06_location, note_content)

    if not DNR2_HOUR_06_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_06_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_06_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_06_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_06_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_06_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_06_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_06_generate(dnr2_hour_06_location):
    """
    """
    with open(dnr2_hour_06_location, 'a+') as dnr2_hour_06_file_obj:
        dnr2_hour_06_file_obj.write(DNR2_HOUR_06_FILE_CONTENT_CREATION)


def daily_note_routine_hour_06_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_06_directory = initial_check("")
    dnr2_hour_06_location = sbd + dnr2_hour_06_directory + Today + "_" + ".md"
    return dnr2_hour_06_location


def daily_note_routine_hour_06_pregenerate_check():
    """
    """
    dnr2_hour_06_location = daily_note_routine_hour_06_location()
    dnr2_hour_06_file_exist_check = exists(dnr2_hour_06_location)
    if dnr2_hour_06_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_06_generate(dnr2_hour_06_location)


# Routine Hour_06 FUNCTIONS FINISHED

# Routine Hour_07 FUNCTIONS STARTED
def daily_note_routine_hour_07_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_07_location = daily_note_routine_hour_07_location()

    if DNR2_HOUR_07_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_07_location, note_content)

    elif DNR2_HOUR_07_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_07_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_07_location, note_content, include_time)

    elif DNR2_HOUR_07_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_07_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_07_location, note_content, include_time)

    elif DNR2_HOUR_07_APPEND_TYPE == "Table":
        table_append(dnr2_hour_07_location, note_content)

    if not DNR2_HOUR_07_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_07_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_07_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_07_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_07_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_07_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_07_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_07_generate(dnr2_hour_07_location):
    """
    """
    with open(dnr2_hour_07_location, 'a+') as dnr2_hour_07_file_obj:
        dnr2_hour_07_file_obj.write(DNR2_HOUR_07_FILE_CONTENT_CREATION)


def daily_note_routine_hour_07_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_07_directory = initial_check("")
    dnr2_hour_07_location = sbd + dnr2_hour_07_directory + Today + "_" + ".md"
    return dnr2_hour_07_location


def daily_note_routine_hour_07_pregenerate_check():
    """
    """
    dnr2_hour_07_location = daily_note_routine_hour_07_location()
    dnr2_hour_07_file_exist_check = exists(dnr2_hour_07_location)
    if dnr2_hour_07_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_07_generate(dnr2_hour_07_location)


# Routine Hour_07 FUNCTIONS FINISHED

# Routine Hour_08 FUNCTIONS STARTED
def daily_note_routine_hour_08_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_08_location = daily_note_routine_hour_08_location()

    if DNR2_HOUR_08_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_08_location, note_content)

    elif DNR2_HOUR_08_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_08_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_08_location, note_content, include_time)

    elif DNR2_HOUR_08_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_08_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_08_location, note_content, include_time)

    elif DNR2_HOUR_08_APPEND_TYPE == "Table":
        table_append(dnr2_hour_08_location, note_content)

    if not DNR2_HOUR_08_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_08_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_08_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_08_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_08_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_08_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_08_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_08_generate(dnr2_hour_08_location):
    """
    """
    with open(dnr2_hour_08_location, 'a+') as dnr2_hour_08_file_obj:
        dnr2_hour_08_file_obj.write(DNR2_HOUR_08_FILE_CONTENT_CREATION)


def daily_note_routine_hour_08_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_08_directory = initial_check("")
    dnr2_hour_08_location = sbd + dnr2_hour_08_directory + Today + "_" + ".md"
    return dnr2_hour_08_location


def daily_note_routine_hour_08_pregenerate_check():
    """
    """
    dnr2_hour_08_location = daily_note_routine_hour_08_location()
    dnr2_hour_08_file_exist_check = exists(dnr2_hour_08_location)
    if dnr2_hour_08_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_08_generate(dnr2_hour_08_location)


# Routine Hour_08 FUNCTIONS FINISHED

# Routine Hour_09 FUNCTIONS STARTED
def daily_note_routine_hour_09_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_09_location = daily_note_routine_hour_09_location()

    if DNR2_HOUR_09_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_09_location, note_content)

    elif DNR2_HOUR_09_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_09_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_09_location, note_content, include_time)

    elif DNR2_HOUR_09_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_09_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_09_location, note_content, include_time)

    elif DNR2_HOUR_09_APPEND_TYPE == "Table":
        table_append(dnr2_hour_09_location, note_content)

    if not DNR2_HOUR_09_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_09_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_09_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_09_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_09_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_09_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_09_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_09_generate(dnr2_hour_09_location):
    """
    """
    with open(dnr2_hour_09_location, 'a+') as dnr2_hour_09_file_obj:
        dnr2_hour_09_file_obj.write(DNR2_HOUR_09_FILE_CONTENT_CREATION)


def daily_note_routine_hour_09_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_09_directory = initial_check("")
    dnr2_hour_09_location = sbd + dnr2_hour_09_directory + Today + "_" + ".md"
    return dnr2_hour_09_location


def daily_note_routine_hour_09_pregenerate_check():
    """
    """
    dnr2_hour_09_location = daily_note_routine_hour_09_location()
    dnr2_hour_09_file_exist_check = exists(dnr2_hour_09_location)
    if dnr2_hour_09_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_09_generate(dnr2_hour_09_location)


# Routine Hour_09 FUNCTIONS FINISHED

# Routine Hour_10 FUNCTIONS STARTED
def daily_note_routine_hour_10_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_10_location = daily_note_routine_hour_10_location()

    if DNR2_HOUR_10_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_10_location, note_content)

    elif DNR2_HOUR_10_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_10_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_10_location, note_content, include_time)

    elif DNR2_HOUR_10_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_10_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_10_location, note_content, include_time)

    elif DNR2_HOUR_10_APPEND_TYPE == "Table":
        table_append(dnr2_hour_10_location, note_content)

    if not DNR2_HOUR_10_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_10_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_10_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_10_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_10_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_10_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_10_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_10_generate(dnr2_hour_10_location):
    """
    """
    with open(dnr2_hour_10_location, 'a+') as dnr2_hour_10_file_obj:
        dnr2_hour_10_file_obj.write(DNR2_HOUR_10_FILE_CONTENT_CREATION)


def daily_note_routine_hour_10_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_10_directory = initial_check("")
    dnr2_hour_10_location = sbd + dnr2_hour_10_directory + Today + "_" + ".md"
    return dnr2_hour_10_location


def daily_note_routine_hour_10_pregenerate_check():
    """
    """
    dnr2_hour_10_location = daily_note_routine_hour_10_location()
    dnr2_hour_10_file_exist_check = exists(dnr2_hour_10_location)
    if dnr2_hour_10_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_10_generate(dnr2_hour_10_location)


# Routine Hour_10 FUNCTIONS FINISHED

# Routine Hour_11 FUNCTIONS STARTED
def daily_note_routine_hour_11_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_11_location = daily_note_routine_hour_11_location()

    if DNR2_HOUR_11_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_11_location, note_content)

    elif DNR2_HOUR_11_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_11_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_11_location, note_content, include_time)

    elif DNR2_HOUR_11_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_11_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_11_location, note_content, include_time)

    elif DNR2_HOUR_11_APPEND_TYPE == "Table":
        table_append(dnr2_hour_11_location, note_content)

    if not DNR2_HOUR_11_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_11_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_11_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_11_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_11_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_11_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_11_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_11_generate(dnr2_hour_11_location):
    """
    """
    with open(dnr2_hour_11_location, 'a+') as dnr2_hour_11_file_obj:
        dnr2_hour_11_file_obj.write(DNR2_HOUR_11_FILE_CONTENT_CREATION)


def daily_note_routine_hour_11_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_11_directory = initial_check("")
    dnr2_hour_11_location = sbd + dnr2_hour_11_directory + Today + "_" + ".md"
    return dnr2_hour_11_location


def daily_note_routine_hour_11_pregenerate_check():
    """
    """
    dnr2_hour_11_location = daily_note_routine_hour_11_location()
    dnr2_hour_11_file_exist_check = exists(dnr2_hour_11_location)
    if dnr2_hour_11_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_11_generate(dnr2_hour_11_location)


# Routine Hour_11 FUNCTIONS FINISHED

# Routine Hour_12 FUNCTIONS STARTED
def daily_note_routine_hour_12_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_12_location = daily_note_routine_hour_12_location()

    if DNR2_HOUR_12_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_12_location, note_content)

    elif DNR2_HOUR_12_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_12_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_12_location, note_content, include_time)

    elif DNR2_HOUR_12_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_12_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_12_location, note_content, include_time)

    elif DNR2_HOUR_12_APPEND_TYPE == "Table":
        table_append(dnr2_hour_12_location, note_content)

    if not DNR2_HOUR_12_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_12_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_12_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_12_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_12_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_12_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_12_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_12_generate(dnr2_hour_12_location):
    """
    """
    with open(dnr2_hour_12_location, 'a+') as dnr2_hour_12_file_obj:
        dnr2_hour_12_file_obj.write(DNR2_HOUR_12_FILE_CONTENT_CREATION)


def daily_note_routine_hour_12_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_12_directory = initial_check("")
    dnr2_hour_12_location = sbd + dnr2_hour_12_directory + Today + "_" + ".md"
    return dnr2_hour_12_location


def daily_note_routine_hour_12_pregenerate_check():
    """
    """
    dnr2_hour_12_location = daily_note_routine_hour_12_location()
    dnr2_hour_12_file_exist_check = exists(dnr2_hour_12_location)
    if dnr2_hour_12_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_12_generate(dnr2_hour_12_location)


# Routine Hour_12 FUNCTIONS FINISHED

# Routine Hour_13 FUNCTIONS STARTED
def daily_note_routine_hour_13_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_13_location = daily_note_routine_hour_13_location()

    if DNR2_HOUR_13_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_13_location, note_content)

    elif DNR2_HOUR_13_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_13_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_13_location, note_content, include_time)

    elif DNR2_HOUR_13_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_13_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_13_location, note_content, include_time)

    elif DNR2_HOUR_13_APPEND_TYPE == "Table":
        table_append(dnr2_hour_13_location, note_content)

    if not DNR2_HOUR_13_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_13_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_13_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_13_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_13_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_13_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_13_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_13_generate(dnr2_hour_13_location):
    """
    """
    with open(dnr2_hour_13_location, 'a+') as dnr2_hour_13_file_obj:
        dnr2_hour_13_file_obj.write(DNR2_HOUR_13_FILE_CONTENT_CREATION)


def daily_note_routine_hour_13_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_13_directory = initial_check("")
    dnr2_hour_13_location = sbd + dnr2_hour_13_directory + Today + "_" + ".md"
    return dnr2_hour_13_location


def daily_note_routine_hour_13_pregenerate_check():
    """
    """
    dnr2_hour_13_location = daily_note_routine_hour_13_location()
    dnr2_hour_13_file_exist_check = exists(dnr2_hour_13_location)
    if dnr2_hour_13_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_13_generate(dnr2_hour_13_location)


# Routine Hour_13 FUNCTIONS FINISHED

# Routine Hour_14 FUNCTIONS STARTED
def daily_note_routine_hour_14_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_14_location = daily_note_routine_hour_14_location()

    if DNR2_HOUR_14_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_14_location, note_content)

    elif DNR2_HOUR_14_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_14_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_14_location, note_content, include_time)

    elif DNR2_HOUR_14_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_14_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_14_location, note_content, include_time)

    elif DNR2_HOUR_14_APPEND_TYPE == "Table":
        table_append(dnr2_hour_14_location, note_content)

    if not DNR2_HOUR_14_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_14_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_14_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_14_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_14_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_14_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_14_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_14_generate(dnr2_hour_14_location):
    """
    """
    with open(dnr2_hour_14_location, 'a+') as dnr2_hour_14_file_obj:
        dnr2_hour_14_file_obj.write(DNR2_HOUR_14_FILE_CONTENT_CREATION)


def daily_note_routine_hour_14_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_14_directory = initial_check("")
    dnr2_hour_14_location = sbd + dnr2_hour_14_directory + Today + "_" + ".md"
    return dnr2_hour_14_location


def daily_note_routine_hour_14_pregenerate_check():
    """
    """
    dnr2_hour_14_location = daily_note_routine_hour_14_location()
    dnr2_hour_14_file_exist_check = exists(dnr2_hour_14_location)
    if dnr2_hour_14_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_14_generate(dnr2_hour_14_location)


# Routine Hour_14 FUNCTIONS FINISHED

# Routine Hour_15 FUNCTIONS STARTED
def daily_note_routine_hour_15_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_15_location = daily_note_routine_hour_15_location()

    if DNR2_HOUR_15_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_15_location, note_content)

    elif DNR2_HOUR_15_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_15_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_15_location, note_content, include_time)

    elif DNR2_HOUR_15_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_15_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_15_location, note_content, include_time)

    elif DNR2_HOUR_15_APPEND_TYPE == "Table":
        table_append(dnr2_hour_15_location, note_content)

    if not DNR2_HOUR_15_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_15_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_15_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_15_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_15_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_15_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_15_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_15_generate(dnr2_hour_15_location):
    """
    """
    with open(dnr2_hour_15_location, 'a+') as dnr2_hour_15_file_obj:
        dnr2_hour_15_file_obj.write(DNR2_HOUR_15_FILE_CONTENT_CREATION)


def daily_note_routine_hour_15_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_15_directory = initial_check("")
    dnr2_hour_15_location = sbd + dnr2_hour_15_directory + Today + "_" + ".md"
    return dnr2_hour_15_location


def daily_note_routine_hour_15_pregenerate_check():
    """
    """
    dnr2_hour_15_location = daily_note_routine_hour_15_location()
    dnr2_hour_15_file_exist_check = exists(dnr2_hour_15_location)
    if dnr2_hour_15_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_15_generate(dnr2_hour_15_location)


# Routine Hour_15 FUNCTIONS FINISHED

# Routine Hour_16 FUNCTIONS STARTED
def daily_note_routine_hour_16_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_16_location = daily_note_routine_hour_16_location()

    if DNR2_HOUR_16_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_16_location, note_content)

    elif DNR2_HOUR_16_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_16_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_16_location, note_content, include_time)

    elif DNR2_HOUR_16_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_16_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_16_location, note_content, include_time)

    elif DNR2_HOUR_16_APPEND_TYPE == "Table":
        table_append(dnr2_hour_16_location, note_content)

    if not DNR2_HOUR_16_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_16_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_16_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_16_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_16_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_16_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_16_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_16_generate(dnr2_hour_16_location):
    """
    """
    with open(dnr2_hour_16_location, 'a+') as dnr2_hour_16_file_obj:
        dnr2_hour_16_file_obj.write(DNR2_HOUR_16_FILE_CONTENT_CREATION)


def daily_note_routine_hour_16_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_16_directory = initial_check("")
    dnr2_hour_16_location = sbd + dnr2_hour_16_directory + Today + "_" + ".md"
    return dnr2_hour_16_location


def daily_note_routine_hour_16_pregenerate_check():
    """
    """
    dnr2_hour_16_location = daily_note_routine_hour_16_location()
    dnr2_hour_16_file_exist_check = exists(dnr2_hour_16_location)
    if dnr2_hour_16_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_16_generate(dnr2_hour_16_location)


# Routine Hour_16 FUNCTIONS FINISHED

# Routine Hour_17 FUNCTIONS STARTED
def daily_note_routine_hour_17_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_17_location = daily_note_routine_hour_17_location()

    if DNR2_HOUR_17_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_17_location, note_content)

    elif DNR2_HOUR_17_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_17_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_17_location, note_content, include_time)

    elif DNR2_HOUR_17_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_17_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_17_location, note_content, include_time)

    elif DNR2_HOUR_17_APPEND_TYPE == "Table":
        table_append(dnr2_hour_17_location, note_content)

    if not DNR2_HOUR_17_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_17_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_17_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_17_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_17_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_17_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_17_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_17_generate(dnr2_hour_17_location):
    """
    """
    with open(dnr2_hour_17_location, 'a+') as dnr2_hour_17_file_obj:
        dnr2_hour_17_file_obj.write(DNR2_HOUR_17_FILE_CONTENT_CREATION)


def daily_note_routine_hour_17_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_17_directory = initial_check("")
    dnr2_hour_17_location = sbd + dnr2_hour_17_directory + Today + "_" + ".md"
    return dnr2_hour_17_location


def daily_note_routine_hour_17_pregenerate_check():
    """
    """
    dnr2_hour_17_location = daily_note_routine_hour_17_location()
    dnr2_hour_17_file_exist_check = exists(dnr2_hour_17_location)
    if dnr2_hour_17_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_17_generate(dnr2_hour_17_location)


# Routine Hour_17 FUNCTIONS FINISHED

# Routine Hour_18 FUNCTIONS STARTED
def daily_note_routine_hour_18_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_18_location = daily_note_routine_hour_18_location()

    if DNR2_HOUR_18_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_18_location, note_content)

    elif DNR2_HOUR_18_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_18_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_18_location, note_content, include_time)

    elif DNR2_HOUR_18_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_18_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_18_location, note_content, include_time)

    elif DNR2_HOUR_18_APPEND_TYPE == "Table":
        table_append(dnr2_hour_18_location, note_content)

    if not DNR2_HOUR_18_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_18_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_18_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_18_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_18_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_18_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_18_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_18_generate(dnr2_hour_18_location):
    """
    """
    with open(dnr2_hour_18_location, 'a+') as dnr2_hour_18_file_obj:
        dnr2_hour_18_file_obj.write(DNR2_HOUR_18_FILE_CONTENT_CREATION)


def daily_note_routine_hour_18_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_18_directory = initial_check("")
    dnr2_hour_18_location = sbd + dnr2_hour_18_directory + Today + "_" + ".md"
    return dnr2_hour_18_location


def daily_note_routine_hour_18_pregenerate_check():
    """
    """
    dnr2_hour_18_location = daily_note_routine_hour_18_location()
    dnr2_hour_18_file_exist_check = exists(dnr2_hour_18_location)
    if dnr2_hour_18_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_18_generate(dnr2_hour_18_location)


# Routine Hour_18 FUNCTIONS FINISHED

# Routine Hour_19 FUNCTIONS STARTED
def daily_note_routine_hour_19_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_19_location = daily_note_routine_hour_19_location()

    if DNR2_HOUR_19_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_19_location, note_content)

    elif DNR2_HOUR_19_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_19_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_19_location, note_content, include_time)

    elif DNR2_HOUR_19_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_19_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_19_location, note_content, include_time)

    elif DNR2_HOUR_19_APPEND_TYPE == "Table":
        table_append(dnr2_hour_19_location, note_content)

    if not DNR2_HOUR_19_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_19_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_19_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_19_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_19_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_19_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_19_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_19_generate(dnr2_hour_19_location):
    """
    """
    with open(dnr2_hour_19_location, 'a+') as dnr2_hour_19_file_obj:
        dnr2_hour_19_file_obj.write(DNR2_HOUR_19_FILE_CONTENT_CREATION)


def daily_note_routine_hour_19_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_19_directory = initial_check("")
    dnr2_hour_19_location = sbd + dnr2_hour_19_directory + Today + "_" + ".md"
    return dnr2_hour_19_location


def daily_note_routine_hour_19_pregenerate_check():
    """
    """
    dnr2_hour_19_location = daily_note_routine_hour_19_location()
    dnr2_hour_19_file_exist_check = exists(dnr2_hour_19_location)
    if dnr2_hour_19_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_19_generate(dnr2_hour_19_location)


# Routine Hour_19 FUNCTIONS FINISHED # Routine Hour_20 FUNCTIONS STARTED
def daily_note_routine_hour_20_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_20_location = daily_note_routine_hour_20_location()

    if DNR2_HOUR_20_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_20_location, note_content)

    elif DNR2_HOUR_20_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_20_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_20_location, note_content, include_time)

    elif DNR2_HOUR_20_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_20_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_20_location, note_content, include_time)

    elif DNR2_HOUR_20_APPEND_TYPE == "Table":
        table_append(dnr2_hour_20_location, note_content)

    if not DNR2_HOUR_20_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_20_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_20_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_20_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_20_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_20_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_20_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_20_generate(dnr2_hour_20_location):
    """
    """
    with open(dnr2_hour_20_location, 'a+') as dnr2_hour_20_file_obj:
        dnr2_hour_20_file_obj.write(DNR2_HOUR_20_FILE_CONTENT_CREATION)


def daily_note_routine_hour_20_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_20_directory = initial_check("")
    dnr2_hour_20_location = sbd + dnr2_hour_20_directory + Today + "_" + ".md"
    return dnr2_hour_20_location


def daily_note_routine_hour_20_pregenerate_check():
    """
    """
    dnr2_hour_20_location = daily_note_routine_hour_20_location()
    dnr2_hour_20_file_exist_check = exists(dnr2_hour_20_location)
    if dnr2_hour_20_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_20_generate(dnr2_hour_20_location)


# Routine Hour_20 FUNCTIONS FINISHED

# Routine Hour_21 FUNCTIONS STARTED
def daily_note_routine_hour_21_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_21_location = daily_note_routine_hour_21_location()

    if DNR2_HOUR_21_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_21_location, note_content)

    elif DNR2_HOUR_21_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_21_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_21_location, note_content, include_time)

    elif DNR2_HOUR_21_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_21_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_21_location, note_content, include_time)

    elif DNR2_HOUR_21_APPEND_TYPE == "Table":
        table_append(dnr2_hour_21_location, note_content)

    if not DNR2_HOUR_21_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_21_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_21_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_21_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_21_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_21_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_21_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_21_generate(dnr2_hour_21_location):
    """
    """
    with open(dnr2_hour_21_location, 'a+') as dnr2_hour_21_file_obj:
        dnr2_hour_21_file_obj.write(DNR2_HOUR_21_FILE_CONTENT_CREATION)


def daily_note_routine_hour_21_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_21_directory = initial_check("")
    dnr2_hour_21_location = sbd + dnr2_hour_21_directory + Today + "_" + ".md"
    return dnr2_hour_21_location


def daily_note_routine_hour_21_pregenerate_check():
    """
    """
    dnr2_hour_21_location = daily_note_routine_hour_21_location()
    dnr2_hour_21_file_exist_check = exists(dnr2_hour_21_location)
    if dnr2_hour_21_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_21_generate(dnr2_hour_21_location)


# Routine Hour_21 FUNCTIONS FINISHED # Routine Hour_22 FUNCTIONS STARTED
def daily_note_routine_hour_22_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_22_location = daily_note_routine_hour_22_location()

    if DNR2_HOUR_22_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_22_location, note_content)

    elif DNR2_HOUR_22_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_22_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_22_location, note_content, include_time)

    elif DNR2_HOUR_22_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_22_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_22_location, note_content, include_time)

    elif DNR2_HOUR_22_APPEND_TYPE == "Table":
        table_append(dnr2_hour_22_location, note_content)

    if not DNR2_HOUR_22_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_22_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_22_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_22_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_22_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_22_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_22_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_22_generate(dnr2_hour_22_location):
    """
    """
    with open(dnr2_hour_22_location, 'a+') as dnr2_hour_22_file_obj:
        dnr2_hour_22_file_obj.write(DNR2_HOUR_22_FILE_CONTENT_CREATION)


def daily_note_routine_hour_22_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_22_directory = initial_check("")
    dnr2_hour_22_location = sbd + dnr2_hour_22_directory + Today + "_" + ".md"
    return dnr2_hour_22_location


def daily_note_routine_hour_22_pregenerate_check():
    """
    """
    dnr2_hour_22_location = daily_note_routine_hour_22_location()
    dnr2_hour_22_file_exist_check = exists(dnr2_hour_22_location)
    if dnr2_hour_22_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_22_generate(dnr2_hour_22_location)


# Routine Hour_22 FUNCTIONS FINISHED # Routine Hour_23 FUNCTIONS STARTED
def daily_note_routine_hour_23_append(note_content, include_time=True):
    """
    appends to
    """
    dnr2_hour_23_location = daily_note_routine_hour_23_location()

    if DNR2_HOUR_23_APPEND_TYPE == "Paragraph":
        paragraph_append(dnr2_hour_23_location, note_content)

    elif DNR2_HOUR_23_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnr2_hour_23_location, note_content, include_time)
        else:
            plain_text_append(dnr2_hour_23_location, note_content, include_time)

    elif DNR2_HOUR_23_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnr2_hour_23_location, note_content, include_time)
        else:
            bullet_list_append(dnr2_hour_23_location, note_content, include_time)

    elif DNR2_HOUR_23_APPEND_TYPE == "Table":
        table_append(dnr2_hour_23_location, note_content)

    if not DNR2_HOUR_23_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnr2_hour_23_location, note_content, include_time)
            else:
                plain_text_append(dnr2_hour_23_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnr2_hour_23_location, note_content, include_time)
            else:
                bullet_list_append(dnr2_hour_23_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnr2_hour_23_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnr2_hour_23_location, note_content)
        else:
            print("Error")


def daily_note_routine_hour_23_generate(dnr2_hour_23_location):
    """
    """
    with open(dnr2_hour_23_location, 'a+') as dnr2_hour_23_file_obj:
        dnr2_hour_23_file_obj.write(DNR2_HOUR_23_FILE_CONTENT_CREATION)


def daily_note_routine_hour_23_location():
    """
    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_hour_23_directory = initial_check("")
    dnr2_hour_23_location = sbd + dnr2_hour_23_directory + Today + "_" + ".md"
    return dnr2_hour_23_location


def daily_note_routine_hour_23_pregenerate_check():
    """
    """
    dnr2_hour_23_location = daily_note_routine_hour_23_location()
    dnr2_hour_23_file_exist_check = exists(dnr2_hour_23_location)
    if dnr2_hour_23_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routine_hour_23_generate(dnr2_hour_23_location)


# Routine Hour_23 FUNCTIONS FINISHED # Routine Hourly FUNCTIONS FINISHED # Routine RELATED FUNCTIONS FINISHED
# Tasks RELATED FUNCTIONS STARTED
def daily_note_tasks_append(note_content, include_time=True):
    """
    appends to
    """
    dnt_location = daily_note_tasks_location()

    if DNT_APPEND_TYPE == "Paragraph":
        paragraph_append(dnt_location, note_content)

    elif DNT_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnt_location, note_content, include_time)
        else:
            plain_text_append(dnt_location, note_content, include_time)

    elif DNT_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnt_location, note_content, include_time)
        else:
            bullet_list_append(dnt_location, note_content, include_time)

    elif DNT_APPEND_TYPE == "Table":
        table_append(dnt_location, note_content)

    if not DNT_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnt_location, note_content, include_time)
            else:
                plain_text_append(dnt_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnt_location, note_content, include_time)
            else:
                bullet_list_append(dnt_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnt_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnt_location, note_content)
        else:
            print("Error")


def daily_note_tasks_generate(dnt_location):
    """

    """

    with open(dnt_location, 'a+') as dnt_file_obj:
        dnt_file_obj.write(DNT_FILE_CONTENT_CREATION)


def daily_note_tasks_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnt_directory = initial_check("01C1H")
    dnt_location = sbd + dnt_directory + Today + "_" + ".md"
    return dnt_location


def daily_note_tasks_pregenerate_check():
    """

    """
    dnt_location = daily_note_tasks_location()
    dnt_file_exist_check = exists(dnt_location)
    if dnt_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_tasks_generate(dnt_location)

# Tasks RELATED FUNCTIONS FINISHED  # Trackers RELATED FUNCTIONS STARTED # Trackers MOC FUNCTIONS STARTED


def daily_note_trackers_moc_append(note_content, include_time=True):
    """
    appends to
    """
    dnt2_location = daily_note_trackers_moc_location()

    if DNT2_APPEND_TYPE == "Paragraph":
        paragraph_append(dnt2_location, note_content)

    elif DNT2_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnt2_location, note_content, include_time)
        else:
            plain_text_append(dnt2_location, note_content, include_time)

    elif DNT2_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnt2_location, note_content, include_time)
        else:
            bullet_list_append(dnt2_location, note_content, include_time)

    elif DNT2_APPEND_TYPE == "Table":
        table_append(dnt2_location, note_content)

    if not DNT2_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnt2_location, note_content, include_time)
            else:
                plain_text_append(dnt2_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnt2_location, note_content, include_time)
            else:
                bullet_list_append(dnt2_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnt2_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnt2_location, note_content)
        else:
            print("Error")


def daily_note_trackers_moc_generate(dnt2_location):
    """

    """
    with open(dnt2_location, 'a+') as dnt2_file_obj:
        dnt2_file_obj.write(DNT2_FILE_CONTENT_CREATION)


def daily_note_trackers_moc_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnt2_directory = initial_check("01C1I")
    dnt2_location = sbd + dnt2_directory + Today + "_" + ".md"
    return dnt2_location


def daily_note_trackers_moc_pregenerate_check():
    """

    """
    dnt2_location = daily_note_trackers_moc_location()
    dnt2_file_exist_check = exists(dnt2_location)
    if dnt2_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_moc_generate(dnt2_location)


# Trackers MOC FUNCTIONS FINISHED # TRACKERS_EXERCISE RELATED FUNCTIONS STARTED

def daily_note_trackers_exercise_append(note_content, include_time=True):
    """

    """
    dnte_location = daily_note_trackers_exercise_location()

    if DNTE_APPEND_TYPE == "Paragraph":
        paragraph_append(dnte_location, note_content)

    elif DNTE_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnte_location, note_content, include_time)
        else:
            plain_text_append(dnte_location, note_content, include_time)

    elif DNTE_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnte_location, note_content, include_time)
        else:
            bullet_list_append(dnte_location, note_content, include_time)

    elif DNTE_APPEND_TYPE == "Table":
        table_append(dnte_location, note_content)

    if not DNTE_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnte_location, note_content, include_time)
            else:
                plain_text_append(dnte_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnte_location, note_content, include_time)
            else:
                bullet_list_append(dnte_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnte_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnte_location, note_content)
        else:
            print("Error")


def daily_note_trackers_exercise_generate(dnte_location):
    """

    """
    with open(dnte_location, 'a+') as dnte_file_obj:
        dnte_file_obj.write(DNTE_FILE_CONTENT_CREATION)


def daily_note_trackers_exercise_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnte_directory = initial_check("01C1I7")
    dnte_location = sbd + dnte_directory + Today + "_" + ".md"
    return dnte_location


def daily_note_trackers_exercise_pregenerate_check():
    """

    """
    dnte_location = daily_note_trackers_exercise_location()
    dnte_file_exist_check = exists(dnte_location)
    if dnte_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_exercise_generate(dnte_location)


# Trackers_EXERCISE RELATED FUNCTIONS FINISHED # TRACKERS_TRANSACTION RELATED FUNCTIONS STARTED

def daily_note_trackers_transaction_append(note_content, include_time=True):
    """

    """
    dntt_location = daily_note_trackers_transaction_location()

    if dntt_APPEND_TYPE == "Paragraph":
        paragraph_append(dntt_location, note_content)

    elif dntt_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dntt_location, note_content, include_time)
        else:
            plain_text_append(dntt_location, note_content, include_time)

    elif dntt_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dntt_location, note_content, include_time)
        else:
            bullet_list_append(dntt_location, note_content, include_time)

    elif dntt_APPEND_TYPE == "Table":
        table_append(dntt_location, note_content)

    if not dntt_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dntt_location, note_content, include_time)
            else:
                plain_text_append(dntt_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dntt_location, note_content, include_time)
            else:
                bullet_list_append(dntt_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dntt_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dntt_location, note_content)
        else:
            print("Error")


def daily_note_trackers_transaction_generate(dntt_location):
    """

    """
    with open(dntt_location, 'a+') as dntt_file_obj:
        dntt_file_obj.write(dntt_FILE_CONTENT_CREATION)


def daily_note_trackers_transaction_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dntt_directory = initial_check("01C1I1")
    dntt_location = sbd + dntt_directory + Today + "_" + ".md"
    return dntt_location


def daily_note_trackers_transaction_pregenerate_check():
    """

    """
    dntt_location = daily_note_trackers_transaction_location()
    dntt_file_exist_check = exists(dntt_location)
    if dntt_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_transaction_generate(dntt_location)


# Trackers_TRANSACTION RELATED FUNCTIONS FINISHED # TRACKERS_LOCATION RELATED FUNCTIONS STARTED

def daily_note_trackers_location_append(note_content, include_time=True):
    """

    """
    dntl_location = daily_note_trackers_location_location()

    if DNTL_APPEND_TYPE == "Paragraph":
        paragraph_append(dntl_location, note_content)

    elif DNTL_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dntl_location, note_content, include_time)
        else:
            plain_text_append(dntl_location, note_content, include_time)

    elif DNTL_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dntl_location, note_content, include_time)
        else:
            bullet_list_append(dntl_location, note_content, include_time)

    elif DNTL_APPEND_TYPE == "Table":
        table_append(dntl_location, note_content)

    if not DNTL_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dntl_location, note_content, include_time)
            else:
                plain_text_append(dntl_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dntl_location, note_content, include_time)
            else:
                bullet_list_append(dntl_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dntl_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dntl_location, note_content)
        else:
            print("Error")


def daily_note_trackers_location_generate(dntl_location):
    """

    """
    with open(dntl_location, 'a+') as dntl_file_obj:
        dntl_file_obj.write(DNTL_FILE_CONTENT_CREATION)


def daily_note_trackers_location_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dntl_directory = initial_check("01C1I9")
    dntl_location = sbd + dntl_directory + Today + "_" + ".md"
    return dntl_location


def daily_note_trackers_location_pregenerate_check():
    """

    """
    dntl_location = daily_note_trackers_location_location()
    dntl_file_exist_check = exists(dntl_location)
    if dntl_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_location_generate(dntl_location)


# Trackers_LOCATION RELATED FUNCTIONS FINISHED # TRACKERS_MEAL RELATED FUNCTIONS STARTED

def daily_note_trackers_meal_append(note_content, include_time=True):
    """

    """
    dntm_location = daily_note_trackers_meal_location()

    if DNTM_APPEND_TYPE == "Paragraph":
        paragraph_append(dntm_location, note_content)

    elif DNTM_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dntm_location, note_content, include_time)
        else:
            plain_text_append(dntm_location, note_content, include_time)

    elif DNTM_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dntm_location, note_content, include_time)
        else:
            bullet_list_append(dntm_location, note_content, include_time)

    elif DNTM_APPEND_TYPE == "Table":
        table_append(dntm_location, note_content)

    if not DNTM_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dntm_location, note_content, include_time)
            else:
                plain_text_append(dntm_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dntm_location, note_content, include_time)
            else:
                bullet_list_append(dntm_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dntm_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dntm_location, note_content)
        else:
            print("Error")


def daily_note_trackers_meal_generate(dntm_location):
    """

    """
    with open(dntm_location, 'a+') as dntm_file_obj:
        dntm_file_obj.write(DNTM_FILE_CONTENT_CREATION)


def daily_note_trackers_meal_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dntm_directory = initial_check("01C1I3")
    dntm_location = sbd + dntm_directory + Today + "_" + ".md"
    return dntm_location


def daily_note_trackers_meal_pregenerate_check():
    """

    """
    dntm_location = daily_note_trackers_meal_location()
    dntm_file_exist_check = exists(dntm_location)
    if dntm_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_meal_generate(dntm_location)


# Trackers_MEAL RELATED FUNCTIONS FINISHED # TRACKERS_MEDICINE RELATED FUNCTIONS STARTED

def daily_note_trackers_medicine_append(note_content, include_time=True):
    """

    """
    dntm2_location = daily_note_trackers_medicine_location()

    if DNTM2_APPEND_TYPE == "Paragraph":
        paragraph_append(dntm2_location, note_content)

    elif DNTM2_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dntm2_location, note_content, include_time)
        else:
            plain_text_append(dntm2_location, note_content, include_time)

    elif DNTM2_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dntm2_location, note_content, include_time)
        else:
            bullet_list_append(dntm2_location, note_content, include_time)

    elif DNTM2_APPEND_TYPE == "Table":
        table_append(dntm2_location, note_content)

    if not DNTM2_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dntm2_location, note_content, include_time)
            else:
                plain_text_append(dntm2_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dntm2_location, note_content, include_time)
            else:
                bullet_list_append(dntm2_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dntm2_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dntm2_location, note_content)
        else:
            print("Error")


def daily_note_trackers_medicine_generate(dntm2_location):
    """

    """
    with open(dntm2_location, 'a+') as dntm2_file_obj:
        dntm2_file_obj.write(DNTM2_FILE_CONTENT_CREATION)


def daily_note_trackers_medicine_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dntm2_directory = initial_check("01C1I4")
    dntm2_location = sbd + dntm2_directory + Today + "_" + ".md"
    return dntm2_location


def daily_note_trackers_medicine_pregenerate_check():
    """

    """
    dntm2_location = daily_note_trackers_medicine_location()
    dntm2_file_exist_check = exists(dntm2_location)
    if dntm2_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_medicine_generate(dntm2_location)


# Trackers_MEDICINE RELATED FUNCTIONS FINISHED # TRACKERS_MOOD RELATED FUNCTIONS STARTED

def daily_note_trackers_mood_append(note_content, include_time=True):
    """

    """
    dntm3_location = daily_note_trackers_mood_location()

    if DNTM3_APPEND_TYPE == "Paragraph":
        paragraph_append(dntm3_location, note_content)

    elif DNTM3_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dntm3_location, note_content, include_time)
        else:
            plain_text_append(dntm3_location, note_content, include_time)

    elif DNTM3_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dntm3_location, note_content, include_time)
        else:
            bullet_list_append(dntm3_location, note_content, include_time)

    elif DNTM3_APPEND_TYPE == "Table":
        table_append(dntm3_location, note_content)

    if not DNTM3_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dntm3_location, note_content, include_time)
            else:
                plain_text_append(dntm3_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dntm3_location, note_content, include_time)
            else:
                bullet_list_append(dntm3_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dntm3_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dntm3_location, note_content)
        else:
            print("Error")


def daily_note_trackers_mood_generate(dntm3_location):
    """

    """
    with open(dntm3_location, 'a+') as dntm3_file_obj:
        dntm3_file_obj.write(DNTM3_FILE_CONTENT_CREATION)


def daily_note_trackers_mood_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dntm3_directory = initial_check("01C1I5")
    dntm3_location = sbd + dntm3_directory + Today + "_" + ".md"
    return dntm3_location


def daily_note_trackers_mood_pregenerate_check():
    """

    """
    dntm3_location = daily_note_trackers_mood_location()
    dntm3_file_exist_check = exists(dntm3_location)
    if dntm3_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_mood_generate(dntm3_location)


# Trackers_MOOD RELATED FUNCTIONS FINISHED # TRACKERS_SLEEP RELATED FUNCTIONS STARTED

def daily_note_trackers_sleep_append(note_content, include_time=True):
    """

    """
    dnts_location = daily_note_trackers_sleep_location()

    if DNTS_APPEND_TYPE == "Paragraph":
        paragraph_append(dnts_location, note_content)

    elif DNTS_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnts_location, note_content, include_time)
        else:
            plain_text_append(dnts_location, note_content, include_time)

    elif DNTS_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnts_location, note_content, include_time)
        else:
            bullet_list_append(dnts_location, note_content, include_time)

    elif DNTS_APPEND_TYPE == "Table":
        table_append(dnts_location, note_content)

    if not DNTS_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnts_location, note_content, include_time)
            else:
                plain_text_append(dnts_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnts_location, note_content, include_time)
            else:
                bullet_list_append(dnts_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnts_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnts_location, note_content)
        else:
            print("Error")


def daily_note_trackers_sleep_generate(dnts_location):
    """

    """
    with open(dnts_location, 'a+') as dnts_file_obj:
        dnts_file_obj.write(DNTS_FILE_CONTENT_CREATION)


def daily_note_trackers_sleep_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnts_directory = initial_check("01C1I2")
    dnts_location = sbd + dnts_directory + Today + "_" + ".md"
    return dnts_location


def daily_note_trackers_sleep_pregenerate_check():
    """

    """
    dnts_location = daily_note_trackers_sleep_location()
    dnts_file_exist_check = exists(dnts_location)
    if dnts_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_sleep_generate(dnts_location)


# Trackers_SLEEP RELATED FUNCTIONS FINISHED # TRACKERS_SYMPTOMS RELATED FUNCTIONS STARTED

def daily_note_trackers_symptoms_append(note_content, include_time=True):
    """

    """
    dnts2_location = daily_note_trackers_symptoms_location()

    if DNTS2_APPEND_TYPE == "Paragraph":
        paragraph_append(dnts2_location, note_content)

    elif DNTS2_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dnts2_location, note_content, include_time)
        else:
            plain_text_append(dnts2_location, note_content, include_time)

    elif DNTS2_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dnts2_location, note_content, include_time)
        else:
            bullet_list_append(dnts2_location, note_content, include_time)

    elif DNTS2_APPEND_TYPE == "Table":
        table_append(dnts2_location, note_content)

    if not DNTS2_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dnts2_location, note_content, include_time)
            else:
                plain_text_append(dnts2_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dnts2_location, note_content, include_time)
            else:
                bullet_list_append(dnts2_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dnts2_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dnts2_location, note_content)
        else:
            print("Error")


def daily_note_trackers_symptoms_generate(dnts2_location):
    """

    """
    with open(dnts2_location, 'a+') as dnts2_file_obj:
        dnts2_file_obj.write(DNTS2_FILE_CONTENT_CREATION)


def daily_note_trackers_symptoms_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnts2_directory = initial_check("01C1I8")
    dnts2_location = sbd + dnts2_directory + Today + "_" + ".md"
    return dnts2_location


def daily_note_trackers_symptoms_pregenerate_check():
    """

    """
    dnts2_location = daily_note_trackers_symptoms_location()
    dnts2_file_exist_check = exists(dnts2_location)
    if dnts2_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_symptoms_generate(dnts2_location)


# Trackers_SYMPTOMS RELATED FUNCTIONS FINISHED # TRACKERS_WATER RELATED FUNCTIONS STARTED

def daily_note_trackers_water_append(note_content, include_time=True):
    """

    """
    dntw_location = daily_note_trackers_water_location()

    if DNTW_APPEND_TYPE == "Paragraph":
        paragraph_append(dntw_location, note_content)

    elif DNTW_APPEND_TYPE == "Plain_Text":
        PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
        if PT_Time_check == "False":
            include_time = False
            plain_text_append(dntw_location, note_content, include_time)
        else:
            plain_text_append(dntw_location, note_content, include_time)

    elif DNTW_APPEND_TYPE == "Bullet_List":
        BL_Time_check = LIST_TIME_INCLUDE
        if BL_Time_check == "False":
            include_time = False
            bullet_list_append(dntw_location, note_content, include_time)
        else:
            bullet_list_append(dntw_location, note_content, include_time)

    elif DNTW_APPEND_TYPE == "Table":
        table_append(dntw_location, note_content)

    if not DNTW_APPEND_TYPE:
        if GLOBAL_APPEND_TYPE == "Plain_Text":
            PT_Time_check = PLAIN_TEXT_TIME_INCLUDE
            if PT_Time_check == "False":
                include_time = False
                plain_text_append(dntw_location, note_content, include_time)
            else:
                plain_text_append(dntw_location, note_content, include_time)

        elif GLOBAL_APPEND_TYPE == "Bullet_List":
            BL_Time_check = LIST_TIME_INCLUDE
            if BL_Time_check == "False":
                include_time = False
                bullet_list_append(dntw_location, note_content, include_time)
            else:
                bullet_list_append(dntw_location, note_content, include_time)
        elif GLOBAL_APPEND_TYPE == "Table":
            table_append(dntw_location, note_content)
        elif GLOBAL_APPEND_TYPE == "Paragraph":
            paragraph_append(dntw_location, note_content)
        else:
            print("Error")


def daily_note_trackers_water_generate(dntw_location):
    """

    """
    with open(dntw_location, 'a+') as dntw_file_obj:
        dntw_file_obj.write(DNTW_FILE_CONTENT_CREATION)


def daily_note_trackers_water_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dntw_directory = initial_check("01C1I6")
    dntw_location = sbd + dntw_directory + Today + "_" + ".md"
    return dntw_location


def daily_note_trackers_water_pregenerate_check():
    """

    """
    dntw_location = daily_note_trackers_water_location()
    dntw_file_exist_check = exists(dntw_location)
    if dntw_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_water_generate(dntw_location)

# Trackers_WATER RELATED FUNCTIONS FINISHED # TRACKERS RELATED FUNCTIONS FINISHED


# Testing below
def test():
    # daily_note_moc_pregenerate_check()
    # daily_note_moc_append(input("Test data: "))
    print("Testing completed")


test()
