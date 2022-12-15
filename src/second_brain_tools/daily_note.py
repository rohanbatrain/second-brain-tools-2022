# Importing production modules // Meant for production branch
from dotenv import load_dotenv
from os.path import exists
from second_brain_tools.config import Today, PLAIN_TEXT_TIME_INCLUDE, LIST_TIME_INCLUDE
from second_brain_tools.config import SECOND_BRAIN_DIRECTORY, FILE_ALREADY_EXIST
from second_brain_tools.directories import initial_check
from second_brain_tools.append import plain_text_append, bullet_list_append, table_append, paragraph_append
# Importing production modules finished

# Default Append Strings Import Started
from second_brain_tools.config import DNM_APPEND_TYPE, DNBJ_APPEND_TYPE,  DNC_APPEND_TYPE,  DNE_APPEND_TYPE,  DNL_APPEND_TYPE,  DNR_APPEND_TYPE,  DNR2_APPEND_TYPE,  DNT_APPEND_TYPE,  DNT2_APPEND_TYPE,  DNTE_APPEND_TYPE,  DNTF_APPEND_TYPE,  DNTL_APPEND_TYPE,  DNTM_APPEND_TYPE,  DNTM2_APPEND_TYPE,  DNTM3_APPEND_TYPE,  DNTS_APPEND_TYPE,  DNTS2_APPEND_TYPE,  DNTW_APPEND_TYPE, GLOBAL_APPEND_TYPE
from second_brain_tools.config import DNBJ_FILE_CONTENT_CREATION, DNC_FILE_CONTENT_CREATION, DNE_FILE_CONTENT_CREATION, DNL_FILE_CONTENT_CREATION, DNR_FILE_CONTENT_CREATION, DNR2_FILE_CONTENT_CREATION, DNT_FILE_CONTENT_CREATION, DNT2_FILE_CONTENT_CREATION, DNTE_FILE_CONTENT_CREATION, DNTF_FILE_CONTENT_CREATION, DNTL_FILE_CONTENT_CREATION, DNTM_FILE_CONTENT_CREATION, DNTM2_FILE_CONTENT_CREATION, DNTM3_FILE_CONTENT_CREATION, DNTS_FILE_CONTENT_CREATION, DNTS2_FILE_CONTENT_CREATION, DNTW_FILE_CONTENT_CREATION, DNM_FILE_CONTENT_CREATION  # noqa: E501
# Default Append Strings Import Finished

# Default Functions Calling
load_dotenv(".sbt_config")
# Default Functions Calling

# Default variable assignation started.

# Default variable assignation completed


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
# MOC RELATED FUNCTIONS FINISHED


# Bullet-Journal RELATED FUNCTIONS STARTED


def daily_note_bullet_journal_append(note_content, include_time=True):
    """
    appends to
    """


def daily_note_bullet_journal_generate(dnbj_location):
    """

    """
    with open(dnbj_location, 'a+') as dnbj_file_obj:
        dnbj_file_obj.write(DNBJ_FILE_CONTENT_CREATION)


def daily_note_bullet_journal_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnbj_directory = initial_check("01C1B")
    dnbj_location = sbd + dnbj_directory + Today + "_Bullet_Journal" + ".md"
    return dnbj_location


def daily_note_bullet_journal_pregenerate_check():
    """

    """
    dnbj_location = daily_note_moc_location()
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
    dnc_location = daily_note_moc_location()
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
    dne_location = daily_note_moc_location()
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
    dnl_location = daily_note_moc_location()
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
    dnr_location = daily_note_moc_location()
    dnr_file_exist_check = exists(dnr_location)
    if dnr_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_reminders_generate(dnr_location)

# Reminders RELATED FUNCTIONS FINISHED  # Routines RELATED FUNCTIONS STARTED


def daily_note_routines_append(note_content, include_time=True):
    """
    appends to
    """


def daily_note_routines_generate(dnr2_location):
    """

    """
    with open(dnr2_location, 'a+') as dnr2_file_obj:
        dnr2_file_obj.write(DNR2_FILE_CONTENT_CREATION)


def daily_note_routines_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dnr2_directory = initial_check("01C1G")
    dnr2_location = sbd + dnr2_directory + Today + "_" + ".md"
    return dnr2_location


def daily_note_routines_pregenerate_check():
    """

    """
    dnr2_location = daily_note_moc_location()
    dnr2_file_exist_check = exists(dnr2_location)
    if dnr2_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_routines_generate(dnr2_location)

# Routines RELATED FUNCTIONS FINISHED  # Tasks RELATED FUNCTIONS STARTED


def daily_note_tasks_append(note_content, include_time=True):
    """
    appends to
    """


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
    dnt_location = daily_note_moc_location()
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
    dnt2_location = daily_note_moc_location()
    dnt2_file_exist_check = exists(dnt2_location)
    if dnt2_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_moc_generate(dnt2_location)


# Trackers MOC FUNCTIONS FINISHED # TRACKERS_EXERCISE RELATED FUNCTIONS STARTED

def daily_note_trackers_exercise_append(note_content, include_time=True):
    """

    """


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
    dnte_location = daily_note_moc_location()
    dnte_file_exist_check = exists(dnte_location)
    if dnte_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_exercise_generate(dnte_location)


# Trackers_EXERCISE RELATED FUNCTIONS FINISHED # TRACKERS_FINANCE RELATED FUNCTIONS STARTED

def daily_note_trackers_finance_append(note_content, include_time=True):
    """

    """


def daily_note_trackers_finance_generate(dntf_location):
    """

    """
    with open(dntf_location, 'a+') as dntf_file_obj:
        dntf_file_obj.write(DNTF_FILE_CONTENT_CREATION)


def daily_note_trackers_finance_location():
    """

    """
    sbd = SECOND_BRAIN_DIRECTORY
    dntf_directory = initial_check("01C1I1")
    dntf_location = sbd + dntf_directory + Today + "_" + ".md"
    return dntf_location


def daily_note_trackers_finance_pregenerate_check():
    """

    """
    dntf_location = daily_note_moc_location()
    dntf_file_exist_check = exists(dntf_location)
    if dntf_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_finance_generate(dntf_location)


# Trackers_FINANCE RELATED FUNCTIONS FINISHED # TRACKERS_LOCATION RELATED FUNCTIONS STARTED

def daily_note_trackers_location_append(note_content, include_time=True):
    """

    """


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
    dntl_location = daily_note_moc_location()
    dntl_file_exist_check = exists(dntl_location)
    if dntl_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_location_generate(dntl_location)


# Trackers_LOCATION RELATED FUNCTIONS FINISHED # TRACKERS_MEAL RELATED FUNCTIONS STARTED

def daily_note_trackers_meal_append(note_content, include_time=True):
    """

    """


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
    dntm_location = daily_note_moc_location()
    dntm_file_exist_check = exists(dntm_location)
    if dntm_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_meal_generate(dntm_location)


# Trackers_MEAL RELATED FUNCTIONS FINISHED # TRACKERS_MEDICINE RELATED FUNCTIONS STARTED

def daily_note_trackers_medicine_append(note_content, include_time=True):
    """

    """


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
    dntm2_location = daily_note_moc_location()
    dntm2_file_exist_check = exists(dntm2_location)
    if dntm2_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_medicine_generate(dntm2_location)


# Trackers_MEDICINE RELATED FUNCTIONS FINISHED # TRACKERS_MOOD RELATED FUNCTIONS STARTED

def daily_note_trackers_mood_append(note_content, include_time=True):
    """

    """


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
    dntm3_location = daily_note_moc_location()
    dntm3_file_exist_check = exists(dntm3_location)
    if dntm3_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_mood_generate(dntm3_location)


# Trackers_MOOD RELATED FUNCTIONS FINISHED # TRACKERS_SLEEP RELATED FUNCTIONS STARTED

def daily_note_trackers_sleep_append(note_content, include_time=True):
    """

    """


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
    dnts_location = daily_note_moc_location()
    dnts_file_exist_check = exists(dnts_location)
    if dnts_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_sleep_generate(dnts_location)


# Trackers_SLEEP RELATED FUNCTIONS FINISHED # TRACKERS_SYMPTOMS RELATED FUNCTIONS STARTED

def daily_note_trackers_symptoms_append(note_content, include_time=True):
    """

    """


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
    dnts2_location = daily_note_moc_location()
    dnts2_file_exist_check = exists(dnts2_location)
    if dnts2_file_exist_check is True:
        print(FILE_ALREADY_EXIST)
    else:
        daily_note_trackers_symptoms_generate(dnts2_location)


# Trackers_SYMPTOMS RELATED FUNCTIONS FINISHED # TRACKERS_WATER RELATED FUNCTIONS STARTED

def daily_note_trackers_water_append(note_content, include_time=True):
    """

    """


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
    dntw_location = daily_note_moc_location()
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
    print(dnbj_location=daily_note_bullet_journal_location())
    print(dnc_location=daily_note_connections_location())
    print(dne_location=daily_note_events_location())
    print(dnl_location=daily_note_location_location())
    print(dnr_location=daily_note_reminders_location())
    print(dnr2_location=daily_note_routines_location())
    print(dnt_location=daily_note_tasks_location())
    print(dnt2_location=daily_note_trackers_moc_location())
    print(dnte_location=daily_note_trackers_exercise_location())
    print(dntf_location=daily_note_trackers_finance_location())
    print(dntl_location=daily_note_trackers_location_location())
    print(dntm_location=daily_note_trackers_meal_location())
    print(dntm2_location=daily_note_trackers_medicine_location())
    print(dntm3_location=daily_note_trackers_mood_location())
    print(dnts_location=daily_note_trackers_sleep_location())
    print(dnts2_location=daily_note_trackers_symptoms_location())
    print(dntw_location=daily_note_trackers_water_location())
    print("Testing completed")


test()
