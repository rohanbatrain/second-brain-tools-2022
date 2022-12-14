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
# MOC RELATED FUNCTIONS FINISHED


# Bullet-Journal RELATED FUNCTIONS STARTED
def daily_note_bullet_journal_append(note_content, include_time=True):
    """
    appends to
    """
    print("I am a placeholder")


def daily_note_bullet_journal_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# Bullet-Journal RELATED FUNCTIONS FINISHED  # Connections RELATED FUNCTIONS STARTED

def daily_note_connections_append(note_content, include_time=True):
    """
    appends to
    """
    print("I am a placeholder")


def daily_note_connections_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# Connections RELATED FUNCTIONS FINISHED  # Events RELATED FUNCTIONS STARTED
def daily_note_events_append(note_content, include_time=True):
    """
    appends to
    """
    print("I am a placeholder")


def daily_note_events_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# Events RELATED FUNCTIONS FINISHED  # Location RELATED FUNCTIONS STARTED
def daily_note_location_append(note_content, include_time=True):
    """
    appends to
    """
    print("I am a placeholder")


def daily_note_location_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# Location RELATED FUNCTIONS FINISHED  # Reminders RELATED FUNCTIONS STARTED
def daily_note_reminders_append(note_content, include_time=True):
    """
    appends to
    """
    print("I am a placeholder")


def daily_note_reminders_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# Reminders RELATED FUNCTIONS FINISHED  # Routines RELATED FUNCTIONS STARTED
def daily_note_routines_append(note_content, include_time=True):
    """
    appends to
    """
    print("I am a placeholder")


def daily_note_routines_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# Routines RELATED FUNCTIONS FINISHED  # Tasks RELATED FUNCTIONS STARTED
def daily_note_tasks_append(note_content, include_time=True):
    """
    appends to
    """
    print("I am a placeholder")


def daily_note_tasks_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# Tasks RELATED FUNCTIONS FINISHED  # Trackers RELATED FUNCTIONS STARTED # Trackers MOC FUNCTIONS STARTED
def daily_note_trackers_moc_append(note_content, include_time=True):
    """
    appends to
    """
    print("I am a placeholder")


def daily_note_trackers_moc_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# Trackers MOC FUNCTIONS FINISHED # TRACKERS_EXERCISE RELATED FUNCTIONS STARTED

def daily_note_trackers_exercise_append(note_content, include_time=True):
    """

    """
    print("I am a placeholder")


def daily_note_trackers_exercise_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# TRACKERS_EXERCISE RELATED FUNCTIONS FINISHED # TRACKERS_FINANCE RELATED FUNCTIONS STARTED

def daily_note_trackers_finance_append(note_content, include_time=True):
    """

    """
    print("I am a placeholder")


def daily_note_trackers_finance_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# TRACKERS_FINANCE RELATED FUNCTIONS FINISHED # TRACKERS_LOCATION RELATED FUNCTIONS STARTED

def daily_note_trackers_location_append(note_content, include_time=True):
    """

    """
    print("I am a placeholder")


def daily_note_trackers_location_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# TRACKERS_LOCATION RELATED FUNCTIONS FINISHED # TRACKERS_MEAL RELATED FUNCTIONS STARTED

def daily_note_trackers_meal_append(note_content, include_time=True):
    """

    """
    print("I am a placeholder")


def daily_note_trackers_meal_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# TRACKERS_MEAL RELATED FUNCTIONS FINISHED # TRACKERS_MEDICINE RELATED FUNCTIONS STARTED

def daily_note_trackers_medicine_append(note_content, include_time=True):
    """

    """
    print("I am a placeholder")


def daily_note_trackers_medicine_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# TRACKERS_MEDICINE RELATED FUNCTIONS FINISHED # TRACKERS_MOOD RELATED FUNCTIONS STARTED

def daily_note_trackers_mood_append(note_content, include_time=True):
    """

    """
    print("I am a placeholder")


def daily_note_trackers_mood_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# TRACKERS_MOOD RELATED FUNCTIONS FINISHED # TRACKERS_SLEEP RELATED FUNCTIONS STARTED

def daily_note_trackers_sleep_append(note_content, include_time=True):
    """

    """
    print("I am a placeholder")


def daily_note_trackers_sleep_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# TRACKERS_SLEEP RELATED FUNCTIONS FINISHED # TRACKERS_SYMPTOMS RELATED FUNCTIONS STARTED

def daily_note_trackers_symptoms_append(note_content, include_time=True):
    """

    """
    print("I am a placeholder")


def daily_note_trackers_symptoms_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# TRACKERS_SYMPTOMS RELATED FUNCTIONS FINISHED # TRACKERS_WATER RELATED FUNCTIONS STARTED

def daily_note_trackers_water_append(note_content, include_time=True):
    """

    """
    print("I am a placeholder")


def daily_note_trackers_water_generate():
    """

    """
    print("I am a placeholder")


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
    print("I am a placeholder")


# TRACKERS_WATER RELATED FUNCTIONS FINISHED # TRACKERS RELATED FUNCTIONS FINISHED


# Testing below
def test():
    # daily_note_moc_pregenerate_check()
    # daily_note_moc_append(input("Test data: "))
    print(daily_note_moc_location())
    print(daily_note_bullet_journal_location())
    print(daily_note_connections_location())
    print(daily_note_events_location())
    print(daily_note_location_location())
    print(daily_note_reminders_location())
    print(daily_note_routines_location())
    print(daily_note_tasks_location())
    print(daily_note_trackers_moc_location())
    print(daily_note_trackers_exercise_location())
    print(daily_note_trackers_finance_location())
    print(daily_note_trackers_location_location())
    print(daily_note_trackers_meal_location())
    print(daily_note_trackers_medicine_location())
    print(daily_note_trackers_mood_location())
    print(daily_note_trackers_sleep_location())
    print(daily_note_trackers_symptoms_location())
    print(daily_note_trackers_water_location())
    print("Testing completed")


test()
