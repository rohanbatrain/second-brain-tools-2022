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
    capture_symptom_content_creation,
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
    """
    Capture event file creation - creates a new event file with given information.
    It first creates a string containing the event information using the capture_event_content_creation() function.
    It then checks if the event name is empty.
    If it is, it prints an error message.
    Otherwise, it creates a new file at the given path and writes the event information to it.
    It then appends a log of the event to the daily notes using the daily_note_events_append() function.

    Args:
    event_note_path: the path to the event file to be created
    event_name: the name of the event
    event_type: the type of the event
    event_location: the location of the event
    event_summary: a summary of the event
    event_status: the status of the event

    Returns:
    None"""
    CE_FILE_CONTENT_CREATION = capture_event_content_creation(event_name, event_type, event_location, event_summary, event_status)
    event_name_check = len(event_name)
    if event_name_check == "0":
        print("Error! event_name is empty.")
    else:
        with open(event_note_path, 'a+') as ce_file_obj:
            ce_file_obj.write(CE_FILE_CONTENT_CREATION)
        ce_log = "[[" + Today + "_Event_" + event_name + "]]"
        daily_note_events_pregenerate_check()
        daily_note_events_append(ce_log)


def capture_event(event_name, event_type, event_location, event_summary, event_status):
    """
    Capture event information and create a markdown file with the specified details.

    This function first checks if the event directory and working directory exists.
    If not, it creates the directories. It then creates a markdown file with the specified event name
    and saves it to the event working directory.

    Args:
    event_name (str): The name of the event.
    event_type (str): The type of event (e.g. conference, workshop).
    event_location (str): The location of the event.
    event_summary (str): A summary of the event.
    event_status (str): The status of the event (e.g. attended, missed).

    Returns:
    None"""
    sbd = SECOND_BRAIN_DIRECTORY
    event_directory_location = initial_check("04B")
    event_working_directory = event_directory_location + Today + "/"
    event_note_directory = sbd + event_working_directory
    event_note_path = sbd + event_working_directory + Today + "_Event_" + event_name + ".md"
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
    """
    Capture Task File Creation

    This function creates a new task file with the specified parameters and appends it to the specified task note path.
    If the task name is empty, it will print an error message.
    The function also updates the daily tasks list by appending a log entry.

    Args:
    task_note_path (str): The path to the task note where the new task file will be created.
    task_name (str): The name of the task.
    task_status (str): The status of the task (e.g. "In Progress", "Completed").
    task_priority (str): The priority of the task (e.g. "Low", "Medium", "High").
    task_labels (str): A list of labels for the task (e.g. ["Work", "Important"]).
    task_dependencies (str): A list of tasks that this task depends on.
    task_parent_task (str): The parent task of this task, if it is a sub-task.
    task_sub_task (str): A list of sub-tasks for this task.

    Returns:
    None"""
    CT_FILE_CONTENT_CREATION = capture_task_content_creation(
        task_name, task_status, task_priority, task_labels, task_dependencies, task_parent_task, task_sub_task
    )
    task_name_check = len(task_name)
    if task_name_check == "0":
        print("Error! task_name is empty.")
    else:
        with open(task_note_path, 'a+') as ct_file_obj:
            ct_file_obj.write(CT_FILE_CONTENT_CREATION)
        ct_log = "[[" + Today + "_Task_" + task_name + "]]"
        daily_note_tasks_pregenerate_check()
        daily_note_tasks_append(ct_log)


def capture_task(task_name, task_status, task_priority, task_labels, task_dependencies, task_parent_task, task_sub_task):
    """
    Capture a task in a file.

    This function captures the details of a task in a file with the given name.
    The task details include the task name, status, priority, labels, dependencies, parent task, and sub task.
    If the file or directory for the task does not exist, it will be created.

    Args:
    task_name (str): The name of the task.
    task_status (str): The current status of the task (e.g. "in progress", "completed").
    task_priority (str): The priority of the task (e.g. "high", "medium", "low").
    task_labels (list): A list of labels for the task.
    task_dependencies (list): A list of task dependencies.
    task_parent_task (str): The parent task, if applicable.
    task_sub_task (list): A list of sub tasks, if applicable.

    Returns:
    None"""
    sbd = SECOND_BRAIN_DIRECTORY
    task_directory_location = initial_check("01A6")
    task_working_directory = task_directory_location + Today + "/"
    task_note_directory = sbd + task_working_directory
    task_note_path = sbd + task_working_directory + Today + "_Task_" + task_name + ".md"
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
    """
    capture_thought_file_creation creates and writes a new thought file with the provided thought content.

    Args:
    thought_note_path (str): the file path for the new thought file
    thought_name (str): the name of the new thought
    thought_summary (str): a summary of the new thought
    thought_content (str): the content of the new thought

    Returns:
    None"""
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
        ct2_log = "[[" + Today + "_Thought_" + thought_name + "]]"
        daily_note_trackers_thought_pregenerate_check()
        daily_note_trackers_thoughts_append(ct2_log)


def capture_thought(thought_name, thought_summary, thought_content):
    """
    capture_thought creates and writes a new thought file with the provided thought content.

    Args:
    thought_name (str): the name of the new thought
    thought_summary (str): a summary of the new thought
    thought_content (str): the content of the new thought

    Returns:
    None"""
    sbd = SECOND_BRAIN_DIRECTORY
    thought_directory_location = initial_check("01A3")
    thought_working_directory = thought_directory_location + Today + "/"
    thought_note_directory = sbd + thought_working_directory
    thought_note_path = sbd + thought_working_directory + Today + "_Thought_" + thought_name + ".md"
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
    """
    capture_link captures and stores a new link.

    Args:
    url (str): the url of the link to be captured

    Returns:
    None"""
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
    """
    capture_link_root_file_creation creates and writes a new link file with the provided link content.

    Args:
    link_note_path (str): the file path for the new link file
    link_name (str): the name of the new link
    link_content (str): the content of the new link
    link_domain (str): the domain of the new link

    Returns:
    None"""
    CL_FILE_CONTENT_CREATION = capture_link_content_creation(link_name, link_content, link_domain)
    link_name_check = len(link_name)
    if link_name_check == "0":
        print("Error! link_name is empty.")
    else:
        with open(link_note_path, 'a+') as cl_file_obj:
            cl_file_obj.write(CL_FILE_CONTENT_CREATION)
        cl_log = "[[" + Today + "_Link_" + link_name + "]]"
        daily_note_trackers_link_pregenerate_check()
        daily_note_trackers_link_append(cl_log)


def capture_link_root(link_name, link_content, link_domain):
    """
    capture_link_root captures and stores a new link under the root domain.

    Args:
    link_name (str): the name of the new link
    link_content (str): the content of the new link
    link_domain (str): the domain of the new link

    Returns:
    None"""
    sbd = SECOND_BRAIN_DIRECTORY
    link_directory_location = initial_check("01A2")
    link_working_directory = link_directory_location + Today + "/"
    link_note_directory = sbd + link_working_directory
    link_note_path = sbd + link_working_directory + Today + "_Link_" + link_name + ".md"
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
    """
    capture_link_reddit_file_creation creates and writes a new link file for a link from the Reddit domain with the provided link content.

    Args:
    link_note_path (str): the file path for the new link file
    link_name (str): the name of the new link
    link_content (str): the content of the new link
    link_domain (str): the domain of the new link

    Returns:
    None"""
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
    """
    capture_link_reddit captures and stores a new link from the Reddit domain.

    Args:
    link_name (str): the name of the new link
    link_content (str): the content of the new link
    link_domain (str): the domain of the new link

    Returns:
    None"""
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
    """
    capture_link_linkedin_file_creation creates and writes a new link file
    for a link from the LinkedIn domain with the provided link content.

    Args:
    link_note_path (str): the file path for the new link file
    link_name (str): the name of the new link
    link_content (str): the content of the new link
    link_domain (str): the domain of the new link

    Returns:
    None"""
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
    """
    capture_link_linkedin captures and stores a new link from the LinkedIn domain.

    Args:
    link_name (str): the name of the new link
    link_content (str): the content of the new link
    link_domain (str): the domain of the new link

    Returns:
    None"""
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
    """
    capture_reminder_file_creation creates and writes a new reminder file with the provided reminder content.

    Args:
    reminder_note_path (str): the file path for the new reminder file
    reminder_name (str): the name of the new reminder
    reminder_priority (str): the priority of the new reminder
    reminder_labels (str): the labels of the new reminder
    reminder_time_to_remind (str): the time to remind for the new reminder

    Returns:
    None"""
    CR_FILE_CONTENT_CREATION = capture_reminder_content_creation(reminder_name, reminder_priority, reminder_labels, reminder_time_to_remind)
    reminder_name_check = len(reminder_name)
    if reminder_name_check == "0":
        print("Error! reminder_name is empty.")
    else:
        with open(reminder_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_Reminder_" + reminder_name + "]]"
        daily_note_reminders_pregenerate_check()
        daily_note_reminders_append(cr_log)


def capture_reminder(reminder_name, reminder_priority, reminder_labels, reminder_time_to_remind):
    """
    capture_reminder captures and stores a new reminder.

    Args:
    reminder_name (str): the name of the new reminder
    reminder_priority (str): the priority of the new reminder
    reminder_labels (str): the labels of the new reminder
    reminder_time_to_remind (str): the time to remind for the new reminder

    Returns:
    None"""
    sbd = SECOND_BRAIN_DIRECTORY
    reminder_directory_location = initial_check("01A10")
    reminder_working_directory = reminder_directory_location + Today + "/"
    reminder_note_directory = sbd + reminder_working_directory
    reminder_note_path = sbd + reminder_working_directory + Today + "_Reminder_" + reminder_name + ".md"
    cr_file_exist_check = exists(reminder_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(reminder_note_directory)
        capture_reminder_file_creation(reminder_note_path, reminder_name, reminder_priority, reminder_labels, reminder_time_to_remind)
    else:
        capture_reminder_file_creation(reminder_note_path, reminder_name, reminder_priority, reminder_labels, reminder_time_to_remind)


# def capture_reminders


# def capture_bullet_journal
def capture_bullet_journal_file_creation(bullet_journal_note_path):
    """
    capture_bullet_journal_file_creation creates and writes a new bullet journal file with the provided content.

    Args:
    bullet_journal_note_path (str): the file path for the new bullet journal file

    Returns:
    None"""
    CBJ_FILE_CONTENT_CREATION = capture_bullet_journal_content_creation()
    with open(bullet_journal_note_path, 'a+') as cbj_file_obj:
        cbj_file_obj.write(CBJ_FILE_CONTENT_CREATION)
    cbj_log = "[[" + Today + "_Journal_" + "Bullet_Journal" + "]]"
    daily_note_bullet_journal_pregenerate_check()
    daily_note_bullet_journal_append(cbj_log)


def capture_bullet_journal():
    """
    capture_bullet_journal captures and stores a new bullet journal entry.

    Returns:
    None"""
    sbd = SECOND_BRAIN_DIRECTORY
    bullet_journal_directory_location = initial_check("01C1B")
    bullet_journal_working_directory = bullet_journal_directory_location + Today + "/"
    bullet_journal_note_directory = sbd + bullet_journal_working_directory
    bullet_journal_note_path = sbd + bullet_journal_working_directory + Today + "_Journal_" + "Bullet_Journal" + ".md"
    cbj_file_exist_check = exists(bullet_journal_note_directory)
    if cbj_file_exist_check is False:
        os.makedirs(bullet_journal_note_directory)
        capture_bullet_journal_file_creation(bullet_journal_note_path)
    else:
        capture_bullet_journal_file_creation(bullet_journal_note_path)


# def capture_bullet_journal


# def capture_symptom
def capture_symptom_file_creation(symptoms_note_path, Symptom_Name, Symptom_Status):
    """
    capture_symptom_file_creation creates and writes a new symptom file with the provided symptom content.

    Args:
    symptoms_note_path (str): the file path for the new symptom file
    Symptom_Name (str): the name of the new symptom
    Symptom_Status (str): the status of the new symptom

    Returns:
    None"""
    CR_FILE_CONTENT_CREATION = capture_symptom_content_creation(Symptom_Name, Symptom_Status)
    symptoms_name_check = len(Symptom_Name)
    if symptoms_name_check == "0":
        print("Error! symptoms_name is empty.")
    else:
        with open(symptoms_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_Symptom_" + Symptom_Name + "]]"
        daily_note_trackers_symptoms_pregenerate_check()
        daily_note_trackers_symptoms_append(cr_log)


def capture_symptom(Symptom_Name, Symptom_Status):
    """
    capture_symptom captures and stores a new symptom.

    Args:
    Symptom_Name (str): the name of the new symptom
    Symptom_Status (str): the status of the new symptom

    Returns:
    None"""
    sbd = SECOND_BRAIN_DIRECTORY
    symptoms_directory_location = initial_check("01A10")
    symptoms_working_directory = symptoms_directory_location + Today + "/"
    symptoms_note_directory = sbd + symptoms_working_directory
    symptoms_note_path = sbd + symptoms_working_directory + Today + "_Symptom_" + Symptom_Name + ".md"
    cr_file_exist_check = exists(symptoms_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(symptoms_note_directory)
        capture_symptom_file_creation(symptoms_note_path, Symptom_Name, Symptom_Status)
    else:
        capture_symptom_file_creation(symptoms_note_path, Symptom_Name, Symptom_Status)


# def capture_symptom


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
    """
    Creates a file and writes content to it,
    with the given file path, transaction name,
    time of transaction, type of transaction, amount, account and invoice.
    If the transaction name is empty, it will print an error message.
    It will also append a log to track the transaction.

    Args:
    transaction_note_path (str): The path to the file where the content will be written.
    Transaction_Name (str): The name of the transaction.
    Transaction_Time (str): The time of the transaction.
    Transaction_Type (str): The type of the transaction.
    Transaction_Amount (str): The amount of the transaction.
    Transaction_Account (str): The account of the transaction.
    Transaction_Invoice (str): The invoice of the transaction.

    Returns:
    None"""
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
        cr_log = "[[" + Today + "_Transaction_" + Transaction_Name + "]]"
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
    """
    Capture a transaction in a markdown file and append a log to the daily tracker for transactions.

    Args:
    Transaction_Name (str): The name of the transaction.
    Transaction_Time (str): The time the transaction occurred.
    Transaction_Type (str): The type of transaction (e.g. credit, debit).
    Transaction_Amount (float): The amount of the transaction.
    Transaction_Account (str): The account the transaction occurred in.
    Transaction_Invoice (str): The invoice number for the transaction."""
    sbd = SECOND_BRAIN_DIRECTORY
    transaction_directory_location = initial_check("01A10")
    transaction_working_directory = transaction_directory_location + Today + "/"
    transaction_note_directory = sbd + transaction_working_directory
    transaction_note_path = sbd + transaction_working_directory + Today + "_Transaction_" + Transaction_Name + ".md"
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
    """
    Capture exercise file creation function is used to create a file for the given exercise name
    in the specified directory and append the exercise content to it.

    Args:
    exercise_note_path (str): Path of the exercise file
    Exercise_Name (str): Name of the exercise
    Exercise_Time (str): Time at which the exercise is performed
    Exercise_Cohort (str): Cohort of the exercise
    Exercise_Status (str): Status of the exercise (completed or in progress)

    Returns:
    None"""
    CR_FILE_CONTENT_CREATION = capture_exercise_content_creation(
        Exercise_Name,
        Exercise_Time,
        Exercise_Cohort,
        Exercise_Status,
    )
    exercise_name_check = len(Exercise_Name)
    if exercise_name_check == "0":
        print("Error! exercise_name is empty.")
    else:
        with open(exercise_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_Exercise_" + Exercise_Name + "]]"
        daily_note_trackers_exercise_pregenerate_check()
        daily_note_trackers_exercise_append(cr_log)


def capture_exercise(
    Exercise_Name,
    Exercise_Time,
    Exercise_Cohort,
    Exercise_Status,
):
    """
    This function captures an exercise by creating a file in the specified directory with the given details about the exercise.

    Args:
    Exercise_Name (str): The name of the exercise.
    Exercise_Time (str): The time at which the exercise was performed.
    Exercise_Cohort (str): The cohort in which the exercise was performed.
    Exercise_Status (str): The status of the exercise (e.g. completed, skipped, etc.).

    Returns:
    None."""
    sbd = SECOND_BRAIN_DIRECTORY
    exercise_directory_location = initial_check("01A10")
    exercise_working_directory = exercise_directory_location + Today + "/"
    exercise_note_directory = sbd + exercise_working_directory
    exercise_note_path = sbd + exercise_working_directory + Today + "_Exercise_" + Exercise_Name + ".md"
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
    """
    capture_water_intake_file_creation creates a new file or appends to an existing file at the specified
    water_intake_note_path with the given water_intake_name and the content created by capture_water_intake_content_creation.
    It also checks if the water_intake_name is empty and prints an error message if it is.
    The function also calls daily_note_trackers_water_pregenerate_check and
    daily_note_trackers_water_append to update relevant tracking files.

    Args:
    water_intake_name (str): The name of the water intake.
    water_intake_note_path (str): The file path where the water intake file will be created or appended to.
    Water_Intake_Time (str): The time at which the water intake occurred.
    Water_Intake_Amount_In_ML (int): The amount of water intake in milliliters.

    Returns:
    None"""
    CR_FILE_CONTENT_CREATION = capture_water_intake_content_creation(
        water_intake_name, Water_Intake_Time, Water_Intake_Amount_In_ML
    )
    water_intake_name_check = len(water_intake_name)
    if water_intake_name_check == "0":
        print("Error! water_intake_name is empty.")
    else:
        with open(water_intake_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_Water_Intake_" + water_intake_name + "]]"
        daily_note_trackers_water_pregenerate_check()
        daily_note_trackers_water_append(cr_log)


def capture_water_intake(
    water_intake_name,
    Water_Intake_Time,
    Water_Intake_Amount_In_ML,
):
    """
    capture_water_intake(water_intake_name, Water_Intake_Time, Water_Intake_Amount_In_ML)

    Captures and stores information about a water intake in a Markdown file.

    Args:
    water_intake_name (str): The name of the water intake.
    Water_Intake_Time (str): The time at which the water intake occurred.
    Water_Intake_Amount_In_ML (int): The amount of water consumed in milliliters."""
    sbd = SECOND_BRAIN_DIRECTORY
    water_intake_directory_location = initial_check("01A10")
    water_intake_working_directory = water_intake_directory_location + Today + "/"
    water_intake_note_directory = sbd + water_intake_working_directory
    water_intake_note_path = sbd + water_intake_working_directory + Today + "_Water_Intake_" + water_intake_name + ".md"
    cr_file_exist_check = exists(water_intake_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(water_intake_note_directory)
        capture_water_intake_file_creation(water_intake_name, water_intake_note_path, Water_Intake_Time, Water_Intake_Amount_In_ML)
    else:
        capture_water_intake_file_creation(water_intake_name, water_intake_note_path, Water_Intake_Time, Water_Intake_Amount_In_ML)


# def capture_water_intakes


# def capture mood
def capture_mood_file_creation(mood_note_path, Mood_Name, Mood_Status, Mood_Reason):
    CR_FILE_CONTENT_CREATION = capture_mood_content_creation(Mood_Name, Mood_Status, Mood_Reason)
    mood_name_check = len(Mood_Name)
    if mood_name_check == "0":
        print("Error! mood_name is empty.")
    else:
        with open(mood_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_Mood_" + Mood_Name + "]]"
        daily_note_trackers_mood_pregenerate_check()
        daily_note_trackers_mood_append(cr_log)


def capture_mood(Mood_Name, Mood_Status, Mood_Reason):
    sbd = SECOND_BRAIN_DIRECTORY
    mood_directory_location = initial_check("01A10")
    mood_working_directory = mood_directory_location + Today + "/"
    mood_note_directory = sbd + mood_working_directory
    mood_note_path = sbd + mood_working_directory + Today + "_Mood_" + Mood_Name + ".md"
    cr_file_exist_check = exists(mood_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(mood_note_directory)
        capture_mood_file_creation(mood_note_path, Mood_Name, Mood_Status, Mood_Reason)
    else:
        capture_mood_file_creation(mood_note_path, Mood_Name, Mood_Status, Mood_Reason)


# def capture_moods


# def capture_medicine
def capture_medicine_file_creation(medicine_note_path, Medicine_Name, Medicine_Time, Medicine_Type, Medicine_Taken):
    CR_FILE_CONTENT_CREATION = capture_medicine_content_creation(Medicine_Name, Medicine_Time, Medicine_Type, Medicine_Taken)
    medicine_name_check = len(Medicine_Name)
    if medicine_name_check == "0":
        print("Error! medicine_name is empty.")
    else:
        with open(medicine_note_path, 'a+') as cr_file_obj:
            cr_file_obj.write(CR_FILE_CONTENT_CREATION)
        cr_log = "[[" + Today + "_Medicine_" + Medicine_Name + "]]"
        daily_note_trackers_medicine_pregenerate_check()
        daily_note_trackers_medicine_append(cr_log)


def capture_medicine(Medicine_Name, Medicine_Time, Medicine_Type, Medicine_Taken):
    sbd = SECOND_BRAIN_DIRECTORY
    medicine_directory_location = initial_check("01A10")
    medicine_working_directory = medicine_directory_location + Today + "/"
    medicine_note_directory = sbd + medicine_working_directory
    medicine_note_path = sbd + medicine_working_directory + Today + "_Medicine_" + Medicine_Name + ".md"
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
        cr_log = "[[" + Today + "_Sleep_" + Sleep_name + "]]"
        daily_note_trackers_sleep_pregenerate_check()
        daily_note_trackers_sleep_append(cr_log)


def capture_sleep(Sleep_name, Sleep_Type, Sleep_Hours, Sleep_Time):
    sbd = SECOND_BRAIN_DIRECTORY
    sleep_directory_location = initial_check("01A10")
    sleep_working_directory = sleep_directory_location + Today + "/"
    sleep_note_directory = sbd + sleep_working_directory
    sleep_note_path = sbd + sleep_working_directory + Today + "_Sleep_" + Sleep_name + ".md"
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
        cr_log = "[[" + Today + "_Meal_" + Meal_Name + "]]"
        daily_note_trackers_meal_pregenerate_check()
        daily_note_trackers_meal_append(cr_log)


def capture_meal(Meal_Name, Meal_Time, Meal_Type, Meal_Calories, Meal_Taken):
    sbd = SECOND_BRAIN_DIRECTORY
    meal_directory_location = initial_check("01A10")
    meal_working_directory = meal_directory_location + Today + "/"
    meal_note_directory = sbd + meal_working_directory
    meal_note_path = sbd + meal_working_directory + Today + "_Meal_" + Meal_Name + ".md"
    cr_file_exist_check = exists(meal_note_directory)
    if cr_file_exist_check is False:
        os.makedirs(meal_note_directory)
        capture_meal_file_creation(meal_note_path, Meal_Name, Meal_Time, Meal_Type, Meal_Calories, Meal_Taken)
    else:
        capture_meal_file_creation(meal_note_path, Meal_Name, Meal_Time, Meal_Type, Meal_Calories, Meal_Taken)


# def capture_meals
