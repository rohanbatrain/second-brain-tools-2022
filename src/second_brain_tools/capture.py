import os
from os.path import exists
from rich import print
from second_brain_tools.time import Today
from second_brain_tools.config import SECOND_BRAIN_DIRECTORY
from second_brain_tools.directories import initial_check
from second_brain_tools.url import get_domain, get_last_section_of_url

# importing content creation
from second_brain_tools.defaults import (
    capture_event_content_creation,
    capture_task_content_creation,
    capture_thought_content_creation,
    capture_reminder_content_creation,
    capture_bullet_journal_content_creation,
    capture_link_content_creation,
)

# importing content creation

# importing pregenerate_checks
from second_brain_tools.daily_note import (
    daily_note_events_pregenerate_check,
    daily_note_tasks_pregenerate_check,
    daily_note_reminders_pregenerate_check,
    daily_note_trackers_link_pregenerate_check,
    daily_note_bullet_journal_pregenerate_check,
    daily_note_trackers_thought_pregenerate_check,
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
)

# importing appends


# def capture_event
def capture_event_file_creation(event_note_path, event_name, event_type, event_location, event_summary):
    """_summary_

    Args:
        event_note_path (_type_): _description_
        event_name (_type_): _description_
        event_type (_type_): _description_
        event_location (_type_): _description_
        event_summary (_type_): _description_
    """
    CE_FILE_CONTENT_CREATION = capture_event_content_creation(event_name, event_type, event_location, event_summary)
    event_name_check = len(event_name)
    if event_name_check == "0":
        print("Error! event_name is empty.")
    else:
        with open(event_note_path, 'a+') as ce_file_obj:
            ce_file_obj.write(CE_FILE_CONTENT_CREATION)
        ce_log = "[[" + Today + "_" + event_name + "]]"
        daily_note_events_pregenerate_check()
        daily_note_events_append(ce_log)


def capture_event(event_name, event_type, event_location, event_summary):
    """_summary_

    Args:
        event_name (_type_): _description_
        event_type (_type_): _description_
        event_location (_type_): _description_
        event_summary (_type_): _description_
    """
    sbd = SECOND_BRAIN_DIRECTORY
    event_directory_location = initial_check("01C1D")
    event_working_directory = event_directory_location + Today + "/"
    event_note_directory = sbd + event_working_directory
    event_note_path = sbd + event_working_directory + Today + "_" + event_name + ".md"
    ce_file_exist_check = exists(event_note_directory)
    if ce_file_exist_check is False:
        os.makedirs(event_note_directory)
        capture_event_file_creation(event_note_path, event_name, event_type, event_location, event_summary)
    else:
        capture_event_file_creation(event_note_path, event_name, event_type, event_location, event_summary)


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
    task_directory_location = initial_check("01C1H")
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
    thought_content,
):
    CT2_FILE_CONTENT_CREATION = capture_thought_content_creation(
        thought_name,
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


def capture_thought(thought_name, thought_content):
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
            thought_content,
        )
    else:
        capture_thought_file_creation(
            thought_note_path,
            thought_name,
            thought_content,
        )


# Capture_Link_Main
def capture_link(url):
    domain = get_domain(url)
    link_name = get_last_section_of_url(url)
    if domain == "reddit.com":
        capture_link_reddit(link_name, url)
    elif domain == "linkedin.com":
        capture_link_linkedin(link_name, url)


# def capture_link_reddit
def capture_link_reddit_file_creation(
    link_note_path,
    link_name,
    link_content,
):
    """ """
    CL_FILE_CONTENT_CREATION = capture_link_content_creation(
        link_name,
        link_content,
    )
    link_name_check = len(link_name)
    if link_name_check == "0":
        print("Error! link_name is empty.")
    else:
        with open(link_note_path, 'a+') as cl_file_obj:
            cl_file_obj.write(CL_FILE_CONTENT_CREATION)
        cl_log = "[[" + Today + "_Reddit_" + link_name + "]]"
        daily_note_trackers_link_pregenerate_check()
        daily_note_trackers_link_append(cl_log)


def capture_link_reddit(
    link_name,
    link_content,
):
    sbd = SECOND_BRAIN_DIRECTORY
    link_directory_location = initial_check("01A2A1")
    link_working_directory = link_directory_location + Today + "/"
    link_note_directory = sbd + link_working_directory
    link_note_path = sbd + link_working_directory + Today + "_Reddit_" + link_name + ".md"
    cl_file_exist_check = exists(link_note_directory)
    if cl_file_exist_check is False:
        os.makedirs(link_note_directory)
        capture_link_reddit_file_creation(
            link_note_path,
            link_name,
            link_content,
        )
    else:
        capture_link_reddit_file_creation(
            link_note_path,
            link_name,
            link_content,
        )


# def capture_link_linkedin
def capture_link_linkedin_file_creation(
    link_note_path,
    link_name,
    link_content,
):
    """ """
    CL_FILE_CONTENT_CREATION = capture_link_content_creation(
        link_name,
        link_content,
    )
    link_name_check = len(link_name)
    if link_name_check == "0":
        print("Error! link_name is empty.")
    else:
        with open(link_note_path, 'a+') as cl_file_obj:
            cl_file_obj.write(CL_FILE_CONTENT_CREATION)
        cl_log = "[[" + Today + "_" + link_name + "]]"
        daily_note_trackers_link_pregenerate_check()
        daily_note_trackers_link_append(cl_log)


def capture_link_linkedin(
    link_name,
    link_content,
):
    sbd = SECOND_BRAIN_DIRECTORY
    link_directory_location = initial_check("01A2")
    link_working_directory = link_directory_location + Today + "/"
    link_note_directory = sbd + link_working_directory
    link_note_path = sbd + link_working_directory + Today + "_" + link_name + ".md"
    cl_file_exist_check = exists(link_note_directory)
    if cl_file_exist_check is False:
        os.makedirs(link_note_directory)
        capture_link_linkedin_file_creation(
            link_note_path,
            link_name,
            link_content,
        )
    else:
        capture_link_linkedin_file_creation(
            link_note_path,
            link_name,
            link_content,
        )


# # def capture_link
# def capture_link_file_creation(
#     link_note_path,
#     link_name,
#     link_content,
# ):
#     """ """
#     CL_FILE_CONTENT_CREATION = capture_link_content_creation(link_name, link_content,)
#     link_name_check = len(link_name)
#     if link_name_check == "0":
#         print("Error! link_name is empty.")
#     else:
#         with open(link_note_path, 'a+') as cl_file_obj:
#             cl_file_obj.write(CL_FILE_CONTENT_CREATION)
#         cl_log = "[[" + Today + "_" + link_name + "]]"
#         daily_note_trackers_link_pregenerate_check()
#         daily_note_trackers_link_append(cl_log)


# def capture_link(
#     link_name,
#     link_content,
# ):
#     sbd = SECOND_BRAIN_DIRECTORY
#     link_directory_location = initial_check("01A2")
#     link_working_directory = link_directory_location + Today + "/"
#     link_note_directory = sbd + link_working_directory
#     link_note_path = sbd + link_working_directory + Today + "_" + link_name + ".md"
#     cl_file_exist_check = exists(link_note_directory)
#     if cl_file_exist_check is False:
#         os.makedirs(link_note_directory)
#         capture_link_file_creation(link_note_path, link_name, link_content,)
#     else:
#         capture_link_file_creation(link_note_path, link_name, link_content,)

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


def capture_bullet_journal(bullet_journal_type, bullet_journal_location, bullet_journal_summary):
    sbd = SECOND_BRAIN_DIRECTORY
    bullet_journal_directory_location = initial_check("01C1B")
    bullet_journal_working_directory = bullet_journal_directory_location + Today + "/"
    bullet_journal_note_directory = sbd + bullet_journal_working_directory
    bullet_journal_note_path = sbd + bullet_journal_working_directory + Today + "_" + "Bullet_Journal" + ".md"
    cbj_file_exist_check = exists(bullet_journal_note_directory)
    if cbj_file_exist_check is False:
        os.makedirs(bullet_journal_note_directory)
        capture_bullet_journal_file_creation(bullet_journal_note_path, bullet_journal_type, bullet_journal_location, bullet_journal_summary)
    else:
        capture_bullet_journal_file_creation(bullet_journal_note_path, bullet_journal_type, bullet_journal_location, bullet_journal_summary)


# def capture_bullet_journal
