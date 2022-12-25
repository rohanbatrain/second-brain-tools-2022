import os
from os.path import exists
from rich import print
from second_brain_tools.time import Today
from second_brain_tools.config import SECOND_BRAIN_DIRECTORY
from second_brain_tools.directories import initial_check
from second_brain_tools.url import get_domain, get_last_section_of_url
import re

# importing content creation
from second_brain_tools.defaults import (
    capture_event_content_creation,
    capture_task_content_creation,
    capture_thought_content_creation,
    capture_reminder_content_creation,
    capture_bullet_journal_content_creation,
    capture_link_content_creation,
    capture_symptoms_content_creation,
    capture_transaction_content_creation,
    capture_exercise_content_creation,
    capture_water_intake_content_creation,
    capture_mood_content_creation,
    capture_medicine_content_creation,
    capture_sleep_content_creation,
    capture_meal_content_creation,
)

# importing content creation

# importing pregenerate_checks
from second_brain_tools.daily_note import (
    daily_note_trackers_meal_pregenerate_check,
    daily_note_events_pregenerate_check,
    daily_note_tasks_pregenerate_check,
    daily_note_reminders_pregenerate_check,
    daily_note_trackers_link_pregenerate_check,
    daily_note_bullet_journal_pregenerate_check,
    daily_note_trackers_thought_pregenerate_check,
    daily_note_trackers_symptoms_pregenerate_check,
    daily_note_trackers_transaction_pregenerate_check,
    daily_note_trackers_sleep_pregenerate_check,
    daily_note_trackers_medicine_pregenerate_check,
    daily_note_trackers_mood_pregenerate_check,
    daily_note_trackers_water_pregenerate_check,
    daily_note_trackers_exercise_pregenerate_check,
)

# importing pregenerate_checks

# importing appends
from second_brain_tools.daily_note import (
    daily_note_events_append,
    daily_note_tasks_append,
    daily_note_reminders_append,
    daily_note_bullet_journal_append,
    daily_note_trackers_link_append,
    daily_note_trackers_thoughts_append,
    daily_note_trackers_symptoms_append,
    daily_note_trackers_meal_append,
    daily_note_trackers_transaction_append,
    daily_note_trackers_sleep_append,
    daily_note_trackers_medicine_append,
    daily_note_trackers_exercise_append,
    daily_note_trackers_water_append,
    daily_note_trackers_mood_append,

)

# importing appends


# def capture_event
def capture_event_file_creation(event_note_path, event_name, event_type, event_location, event_summary, event_status):
    """_summary_

    Args:
        event_note_path (_type_): _description_
        event_name (_type_): _description_
        event_type (_type_): _description_
        event_location (_type_): _description_
        event_summary (_type_): _description_
    """
    CE_FILE_CONTENT_CREATION = capture_event_content_creation(event_name, event_type, event_location, event_summary, event_status)
    event_name_check = len(event_name)
    if event_name_check == "0":
        print("Error! event_name is empty.")
    else:
        with open(event_note_path, 'a+') as ce_file_obj:
            ce_file_obj.write(CE_FILE_CONTENT_CREATION)
        ce_log = "[[" + Today + "_" + event_name + "]]"
        daily_note_events_pregenerate_check()
        daily_note_events_append(ce_log)


def capture_event(event_name, event_type, event_location, event_summary, event_status):
    """_summary_

    Args:
        event_name (_type_): _description_
        event_type (_type_): _description_
        event_location (_type_): _description_
        event_summary (_type_): _description_
    """
    sbd = SECOND_BRAIN_DIRECTORY
    event_directory_location = initial_check("04B")
    event_working_directory = event_directory_location + Today + "/"
    event_note_directory = sbd + event_working_directory
    event_note_path = sbd + event_working_directory + Today + "_" + event_name + ".md"
    ce_file_exist_check = exists(event_note_directory)
    if ce_file_exist_check is False:
        os.makedirs(event_note_directory)
        capture_event_file_creation(event_note_path, event_name, event_type, event_location, event_summary, event_status)
    else:
        capture_event_file_creation(event_note_path, event_name, event_type, event_location, event_summary, event_status)


# def capture_tasks
def capture_task_file_creation(
    task_note_path, task_name, task_status, task_priority, task_labels, task_dependencies, task_parent_task, task_sub_task
):
    """ """
    CT_FILE_CONTENT_CREATION = capture_task_content_creation(
        task_name, task_status, task_priority, task_labels, task_dependencies, task_parent_task, task_sub_task
    )
    task_name_check = len(task_name)
    if task_name_check == "0":
        print("Error! task_name is empty.")
    else:
        with open(task_note_path, 'a+') as ct_file_obj:
            ct_file_obj.write(CT_FILE_CONTENT_CREATION)
        ct_log = "[[" + Today + "_" + task_name + "]]"
        daily_note_tasks_pregenerate_check()
        daily_note_tasks_append(ct_log)


def capture_task(task_name, task_status, task_priority, task_labels, task_dependencies, task_parent_task, task_sub_task):
    sbd = SECOND_BRAIN_DIRECTORY
    task_directory_location = initial_check("01A6")
    task_working_directory = task_directory_location + Today + "/"
    task_note_directory = sbd + task_working_directory
    task_note_path = sbd + task_working_directory + Today + "_" + task_name + ".md"
    ct_file_exist_check = exists(task_note_directory)
    if ct_file_exist_check is False:
        os.makedirs(task_note_directory)
        capture_task_file_creation(
            task_note_path, task_name, task_status, task_priority, task_labels, task_dependencies, task_parent_task, task_sub_task
        )
    else:
        capture_task_file_creation(
            task_note_path, task_name, task_status, task_priority, task_labels, task_dependencies, task_parent_task, task_sub_task
        )


# def capture_thought
def capture_thought_file_creation(
    thought_note_path,
    thought_name,
    thought_summary,
    thought_content,
):
    CT2_FILE_CONTENT_CREATION = capture_thought_content_creation(
        thought_name,
        thought_summary,
        thought_content,
    )
    thought_name_check = len(thought_name)
    if thought_name_check == "0":
        print("Error! thought_name is empty.")
    else:
        with open(thought_note_path, 'a+') as ct2_file_obj:
            ct2_file_obj.write(CT2_FILE_CONTENT_CREATION)
        ct2_log = "[[" + Today + "_" + thought_name + "]]"
        daily_note_trackers_thought_pregenerate_check()
        daily_note_trackers_thoughts_append(ct2_log)


def capture_thought(thought_name, thought_summary, thought_content):
    sbd = SECOND_BRAIN_DIRECTORY
    thought_directory_location = initial_check("01A3")
    thought_working_directory = thought_directory_location + Today + "/"
    thought_note_directory = sbd + thought_working_directory
    thought_note_path = sbd + thought_working_directory + Today + "_" + thought_name + ".md"
    ct2_file_exist_check = exists(thought_note_directory)
    if ct2_file_exist_check is False:
        os.makedirs(thought_note_directory)
        capture_thought_file_creation(
            thought_note_path,
            thought_name,
            thought_summary,
            thought_content,
        )
    else:
        capture_thought_file_creation(
            thought_note_path,
            thought_name,
            thought_summary,
            thought_content,
        )


# Capture_Link_Main
def capture_link(url):
    domain = get_domain(url)
    link_name = get_last_section_of_url(url)
    if re.match(r"linkedin\.com$", domain, re.IGNORECASE):
        capture_link_linkedin(link_name, url, domain)
    elif re.match(r"reddit\.com$", domain, re.IGNORECASE):
        capture_link_reddit(link_name, url, domain)
    else:
        capture_link_root(link_name, url, domain)


# def capture_link_root
def capture_link_root_file_creation(link_note_path, link_name, link_content, link_domain):
    """ """
    CL_FILE_CONTENT_CREATION = capture_link_content_creation(link_name, link_content, link_domain)
    link_name_check = len(link_name)
    if link_name_check == "0":
        print("Error! link_name is empty.")
    else:
        with open(link_note_path, 'a+') as cl_file_obj:
            cl_file_obj.write(CL_FILE_CONTENT_CREATION)
        cl_log = "[[" + Today + "_" + link_name + "]]"
        daily_note_trackers_link_pregenerate_check()
        daily_note_trackers_link_append(cl_log)


def capture_link_root(link_name, link_content, link_domain):
    sbd = SECOND_BRAIN_DIRECTORY
    link_directory_location = initial_check("01A2")
    link_working_directory = link_directory_location + Today + "/"
    link_note_directory = sbd + link_working_directory
    link_note_path = sbd + link_working_directory + Today + "_" + link_name + ".md"
    cl_file_exist_check = exists(link_note_directory)
    if cl_file_exist_check is False:
        os.makedirs(link_note_directory)
        capture_link_root_file_creation(link_note_path, link_name, link_content, link_domain)
    else:
        capture_link_root_file_creation(link_note_path, link_name, link_content, link_domain)


# def capture_link_reddit
def capture_link_reddit_file_creation(
    link_note_path,
    link_name,
    link_content,
    link_domain,
):
    """ """
    CLR_FILE_CONTENT_CREATION = capture_link_content_creation(
        link_name,
        link_content,
        link_domain,
    )
    link_name_check = len(link_name)
    if link_name_check == "0":
        print("Error! link_name is empty.")
    else:
        with open(link_note_path, 'a+') as cl_file_obj:
            cl_file_obj.write(CLR_FILE_CONTENT_CREATION)
        cl_log = "[[" + Today + "_Reddit_" + link_name + "]]"
        daily_note_trackers_link_pregenerate_check()
        daily_note_trackers_link_append(cl_log)


def capture_link_reddit(link_name, link_content, link_domain):
    sbd = SECOND_BRAIN_DIRECTORY
    link_directory_location = initial_check("01A2A1")
    link_working_directory = link_directory_location + Today + "/"
    link_note_directory = sbd + link_working_directory
    link_note_path = sbd + link_working_directory + Today + "_Reddit_" + link_name + ".md"
    clr_file_exist_check = exists(link_note_directory)
    if clr_file_exist_check is False:
        os.makedirs(link_note_directory)
        capture_link_reddit_file_creation(
            link_note_path,
            link_name,
            link_content,
            link_domain,
        )
    else:
        capture_link_reddit_file_creation(
            link_note_path,
            link_name,
            link_content,
            link_domain,
        )


# def capture_link_linkedin
def capture_link_linkedin_file_creation(link_note_path, link_name, link_content, link_domain):
    """ """
    CLL_FILE_CONTENT_CREATION = capture_link_content_creation(
        link_name,
        link_content,
        link_domain,
    )
    link_name_check = len(link_name)
    if link_name_check == "0":
        print("Error! link_name is empty.")
    else:
        with open(link_note_path, 'a+') as cl_file_obj:
            cl_file_obj.write(CLL_FILE_CONTENT_CREATION)
        cl_log = "[[" + Today + "_Linkedin_" + link_name + "]]"
        daily_note_trackers_link_pregenerate_check()
        daily_note_trackers_link_append(cl_log)


def capture_link_linkedin(link_name, link_content, link_domain):
    sbd = SECOND_BRAIN_DIRECTORY
    link_directory_location = initial_check("01A2B1")
    link_working_directory = link_directory_location + Today + "/"
    link_note_directory = sbd + link_working_directory
    link_note_path = sbd + link_working_directory + Today + "_Linkedin_" + link_name + ".md"
    cl_file_exist_check = exists(link_note_directory)
    if cl_file_exist_check is False:
        os.makedirs(link_note_directory)
        capture_link_linkedin_file_creation(
            link_note_path,
            link_name,
            link_content,
            link_domain,
        )
    else:
        capture_link_linkedin_file_creation(
            link_note_path,
            link_name,
            link_content,
            link_domain,
        )


# def capture_reminders
def capture_reminder_file_creation(reminder_note_path, reminder_name, reminder_priority, reminder_labels, reminder_time_to_remind):
    """ """
    CR_FILE_CONTENT_CREATION = capture_reminder_content_creation(reminder_name, reminder_priority, reminder_labels, reminder_time_to_remind)
    reminder_name_check = len(reminder_name)
    if reminder_name_check == "0":
        print("Error! reminder_name is empty.")
    else:
        with open(reminder_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_" + reminder_name + "]]"
        daily_note_reminders_pregenerate_check()
        daily_note_reminders_append(cr_log)


def capture_reminder(reminder_name, reminder_priority, reminder_labels, reminder_time_to_remind):
    sbd = SECOND_BRAIN_DIRECTORY
    reminder_directory_location = initial_check("01A10")
    reminder_working_directory = reminder_directory_location + Today + "/"
    reminder_note_directory = sbd + reminder_working_directory
    reminder_note_path = sbd + reminder_working_directory + Today + "_" + reminder_name + ".md"
    cr_file_exist_check = exists(reminder_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(reminder_note_directory)
        capture_reminder_file_creation(reminder_note_path, reminder_name, reminder_priority, reminder_labels, reminder_time_to_remind)
    else:
        capture_reminder_file_creation(reminder_note_path, reminder_name, reminder_priority, reminder_labels, reminder_time_to_remind)


# def capture_reminders


# def capture_bullet_journal
def capture_bullet_journal_file_creation(bullet_journal_note_path):
    """ """
    CBJ_FILE_CONTENT_CREATION = capture_bullet_journal_content_creation()
    with open(bullet_journal_note_path, 'a+') as cbj_file_obj:
        cbj_file_obj.write(CBJ_FILE_CONTENT_CREATION)
    cbj_log = "[[" + Today + "_" + "Bullet_Journal" + "]]"
    daily_note_bullet_journal_pregenerate_check()
    daily_note_bullet_journal_append(cbj_log)


def capture_bullet_journal():
    sbd = SECOND_BRAIN_DIRECTORY
    bullet_journal_directory_location = initial_check("01C1B")
    bullet_journal_working_directory = bullet_journal_directory_location + Today + "/"
    bullet_journal_note_directory = sbd + bullet_journal_working_directory
    bullet_journal_note_path = sbd + bullet_journal_working_directory + Today + "_" + "Bullet_Journal" + ".md"
    cbj_file_exist_check = exists(bullet_journal_note_directory)
    if cbj_file_exist_check is False:
        os.makedirs(bullet_journal_note_directory)
        capture_bullet_journal_file_creation(bullet_journal_note_path)
    else:
        capture_bullet_journal_file_creation(bullet_journal_note_path)


# def capture_bullet_journal


# def capture_symptoms
def capture_symptoms_file_creation(symptoms_note_path, Symptom_Name, Symptom_Status):
    """ """
    CR_FILE_CONTENT_CREATION = capture_symptoms_content_creation(Symptom_Name, Symptom_Status)
    symptoms_name_check = len(Symptom_Name)
    if symptoms_name_check == "0":
        print("Error! symptoms_name is empty.")
    else:
        with open(symptoms_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_" + Symptom_Name + "]]"
        daily_note_trackers_symptoms_pregenerate_check()
        daily_note_trackers_symptoms_append(cr_log)


def capture_symptoms(Symptom_Name, Symptom_Status):
    sbd = SECOND_BRAIN_DIRECTORY
    symptoms_directory_location = initial_check("01A10")
    symptoms_working_directory = symptoms_directory_location + Today + "/"
    symptoms_note_directory = sbd + symptoms_working_directory
    symptoms_note_path = sbd + symptoms_working_directory + Today + "_" + Symptom_Name + ".md"
    cr_file_exist_check = exists(symptoms_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(symptoms_note_directory)
        capture_symptoms_file_creation(symptoms_note_path, Symptom_Name, Symptom_Status)
    else:
        capture_symptoms_file_creation(symptoms_note_path, Symptom_Name, Symptom_Status)


# def capture_symptoms


# def capture_transactions
def capture_transaction_file_creation(
    transaction_note_path,
    Transaction_Name,
    Transaction_Time,
    Transaction_Type,
    Transaction_Amount,
    Transaction_Account,
    Transaction_Invoice,
):
    """ """
    CR_FILE_CONTENT_CREATION = capture_transaction_content_creation(
        Transaction_Name,
        Transaction_Time,
        Transaction_Type,
        Transaction_Amount,
        Transaction_Account,
        Transaction_Invoice,
    )
    transaction_name_check = len(Transaction_Name)
    if transaction_name_check == "0":
        print("Error! transaction_name is empty.")
    else:
        with open(transaction_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_" + Transaction_Name + "]]"
        daily_note_trackers_transaction_pregenerate_check()
        daily_note_trackers_transaction_append(cr_log)


def capture_transaction(
    Transaction_Name,
    Transaction_Time,
    Transaction_Type,
    Transaction_Amount,
    Transaction_Account,
    Transaction_Invoice,
):
    sbd = SECOND_BRAIN_DIRECTORY
    transaction_directory_location = initial_check("01A10")
    transaction_working_directory = transaction_directory_location + Today + "/"
    transaction_note_directory = sbd + transaction_working_directory
    transaction_note_path = sbd + transaction_working_directory + Today + "_" + Transaction_Name + ".md"
    cr_file_exist_check = exists(transaction_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(transaction_note_directory)
        capture_transaction_file_creation(
            transaction_note_path,
            Transaction_Name,
            Transaction_Time,
            Transaction_Type,
            Transaction_Amount,
            Transaction_Account,
            Transaction_Invoice,
        )
    else:
        capture_transaction_file_creation(
            transaction_note_path,
            Transaction_Name,
            Transaction_Time,
            Transaction_Type,
            Transaction_Amount,
            Transaction_Account,
            Transaction_Invoice,
        )


# def capture_transactions


# def capture_exercise
def capture_exercise_file_creation(
    exercise_note_path,
    Exercise_Name,
    Exercise_Time,
    Exercise_Cohort,
    Exercise_Status,
):
    """ """
    CR_FILE_CONTENT_CREATION = capture_exercise_content_creation()
    exercise_name_check = len(Exercise_Name)
    if exercise_name_check == "0":
        print("Error! exercise_name is empty.")
    else:
        with open(exercise_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_" + Exercise_Name + "]]"
        daily_note_trackers_exercise_pregenerate_check()
        daily_note_trackers_exercise_append(cr_log)


def capture_exercise(
    Exercise_Name,
    Exercise_Time,
    Exercise_Cohort,
    Exercise_Status,
):
    sbd = SECOND_BRAIN_DIRECTORY
    exercise_directory_location = initial_check("01A10")
    exercise_working_directory = exercise_directory_location + Today + "/"
    exercise_note_directory = sbd + exercise_working_directory
    exercise_note_path = sbd + exercise_working_directory + Today + "_" + Exercise_Name + ".md"
    cr_file_exist_check = exists(exercise_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(exercise_note_directory)
        capture_exercise_file_creation(
            exercise_note_path,
            Exercise_Name,
            Exercise_Time,
            Exercise_Cohort,
            Exercise_Status,
        )
    else:
        capture_exercise_file_creation(
            exercise_note_path,
            Exercise_Name,
            Exercise_Time,
            Exercise_Cohort,
            Exercise_Status,
        )


# def capture_exercises


# def capture_water
def capture_water_intake_file_creation(water_intake_name, water_intake_note_path, Water_Intake_Time, Water_Intake_Amount_In_ML):
    """ """
    CR_FILE_CONTENT_CREATION = capture_water_intake_content_creation(
        water_intake_name, water_intake_note_path, Water_Intake_Time, Water_Intake_Amount_In_ML
    )
    water_intake_name_check = len(water_intake_name)
    if water_intake_name_check == "0":
        print("Error! water_intake_name is empty.")
    else:
        with open(water_intake_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_" + water_intake_name + "]]"
        daily_note_trackers_water_pregenerate_check()
        daily_note_trackers_water_append(cr_log)


def capture_water_intake(
    water_intake_name,
    Water_Intake_Time,
    Water_Intake_Amount_In_ML,
):
    sbd = SECOND_BRAIN_DIRECTORY
    water_intake_directory_location = initial_check("01A10")
    water_intake_working_directory = water_intake_directory_location + Today + "/"
    water_intake_note_directory = sbd + water_intake_working_directory
    water_intake_note_path = sbd + water_intake_working_directory + Today + "_" + water_intake_name + ".md"
    cr_file_exist_check = exists(water_intake_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(water_intake_note_directory)
        capture_water_intake_file_creation(water_intake_name, water_intake_note_path, Water_Intake_Time, Water_Intake_Amount_In_ML)
    else:
        capture_water_intake_file_creation(water_intake_name, water_intake_note_path, Water_Intake_Time, Water_Intake_Amount_In_ML)


# def capture_water_intakes


# def capture mood
def capture_mood_file_creation(mood_note_path, Mood_Name, Mood_Status, Mood_Reason):
    CR_FILE_CONTENT_CREATION = capture_mood_content_creation(mood_note_path, Mood_Name, Mood_Status, Mood_Reason)
    mood_name_check = len(Mood_Name)
    if mood_name_check == "0":
        print("Error! mood_name is empty.")
    else:
        with open(mood_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_" + Mood_Name + "]]"
        daily_note_trackers_mood_pregenerate_check()
        daily_note_trackers_mood_append(cr_log)


def capture_mood(Mood_Name, Mood_Status, Mood_Reason):
    sbd = SECOND_BRAIN_DIRECTORY
    mood_directory_location = initial_check("01A10")
    mood_working_directory = mood_directory_location + Today + "/"
    mood_note_directory = sbd + mood_working_directory
    mood_note_path = sbd + mood_working_directory + Today + "_" + Mood_Name + ".md"
    cr_file_exist_check = exists(mood_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(mood_note_directory)
        capture_mood_file_creation(mood_note_path, Mood_Name, Mood_Status, Mood_Reason)
    else:
        capture_mood_file_creation(mood_note_path, Mood_Name, Mood_Status, Mood_Reason)


# def capture_moods


# def capture_medicine
def capture_medicine_file_creation(medicine_note_path, Medicine_Name, Medicine_Time, Medicine_Type, Medicine_Taken):
    """ """
    CR_FILE_CONTENT_CREATION = capture_medicine_content_creation()
    medicine_name_check = len(Medicine_Name)
    if medicine_name_check == "0":
        print("Error! medicine_name is empty.")
    else:
        with open(medicine_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_" + Medicine_Name + "]]"
        daily_note_trackers_medicine_pregenerate_check()
        daily_note_trackers_medicine_append(cr_log)


def capture_medicine(Medicine_Name, Medicine_Time, Medicine_Type, Medicine_Taken):
    sbd = SECOND_BRAIN_DIRECTORY
    medicine_directory_location = initial_check("01A10")
    medicine_working_directory = medicine_directory_location + Today + "/"
    medicine_note_directory = sbd + medicine_working_directory
    medicine_note_path = sbd + medicine_working_directory + Today + "_" + Medicine_Name + ".md"
    cr_file_exist_check = exists(medicine_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(medicine_note_directory)
        capture_medicine_file_creation(medicine_note_path, Medicine_Name, Medicine_Time, Medicine_Type, Medicine_Taken)
    else:
        capture_medicine_file_creation(medicine_note_path, Medicine_Name, Medicine_Time, Medicine_Type, Medicine_Taken)


# def capture_medicines


# def capture_sleep
def capture_sleep_file_creation(sleep_note_path, Sleep_name, Sleep_Type, Sleep_Hours, Sleep_Time):
    """ """
    CR_FILE_CONTENT_CREATION = capture_sleep_content_creation(Sleep_name, Sleep_Type, Sleep_Hours, Sleep_Time)
    sleep_name_check = len(Sleep_name)
    if sleep_name_check == "0":
        print("Error! sleep_name is empty.")
    else:
        with open(sleep_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_" + Sleep_name + "]]"
        daily_note_trackers_sleep_pregenerate_check()
        daily_note_trackers_sleep_append(cr_log)


def capture_sleep(Sleep_name, Sleep_Type, Sleep_Hours, Sleep_Time):
    sbd = SECOND_BRAIN_DIRECTORY
    sleep_directory_location = initial_check("01A10")
    sleep_working_directory = sleep_directory_location + Today + "/"
    sleep_note_directory = sbd + sleep_working_directory
    sleep_note_path = sbd + sleep_working_directory + Today + "_" + Sleep_name + ".md"
    cr_file_exist_check = exists(sleep_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(sleep_note_directory)
        capture_sleep_file_creation(sleep_note_path, Sleep_name, Sleep_Type, Sleep_Hours, Sleep_Time)
    else:
        capture_sleep_file_creation(sleep_note_path, Sleep_name, Sleep_Type, Sleep_Hours, Sleep_Time)


# def capture_sleep


# def capture meal
def capture_meal_file_creation(meal_note_path, Meal_Name, Meal_Time, Meal_Type, Meal_Calories, Meal_Taken):
    """ """
    CR_FILE_CONTENT_CREATION = capture_meal_content_creation(Meal_Name, Meal_Time, Meal_Type, Meal_Calories, Meal_Taken)
    meal_name_check = len(Meal_Name)
    if meal_name_check == "0":
        print("Error! meal_name is empty.")
    else:
        with open(meal_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_" + Meal_Name + "]]"
        daily_note_trackers_meal_pregenerate_check()
        daily_note_trackers_meal_append(cr_log)


def capture_meal(Meal_Name, Meal_Time, Meal_Type, Meal_Calories, Meal_Taken):
    sbd = SECOND_BRAIN_DIRECTORY
    meal_directory_location = initial_check("01A10")
    meal_working_directory = meal_directory_location + Today + "/"
    meal_note_directory = sbd + meal_working_directory
    meal_note_path = sbd + meal_working_directory + Today + "_" + Meal_Name + ".md"
    cr_file_exist_check = exists(meal_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(meal_note_directory)
        capture_meal_file_creation(meal_note_path, Meal_Name, Meal_Time, Meal_Type, Meal_Calories, Meal_Taken)
    else:
        capture_meal_file_creation(meal_note_path, Meal_Name, Meal_Time, Meal_Type, Meal_Calories, Meal_Taken)


# def capture_meals
