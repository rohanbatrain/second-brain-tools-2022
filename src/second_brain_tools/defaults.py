# Importing production modules // Meant for production branch
from second_brain_tools.time import Today, CURRENT_TIME  # noqa: F401

# Importing production modules finished

# Default String Started // Should be transfered to config once project is completed.
INVALID_FILE_NAME_ERROR = "Error, The name you provided is invalid"
NOTE_EXTENTION = ".md"
NO_MARKDOWN_FILE = "No markdown files found in the directory"
NOTE_CREATED_SUCCESFULLY = "Horray! Note Created Successfully."

# Default String Finished

# Daily Note File Creation Content String Started
# Daily Note File Creation Content String Finished
DNM_FILE_CONTENT_CREATION = f"""---
tags :/daily_note/{Today}
date : {Today}
---

* [[{Today}_Events|Events]]
* [[{Today}_Connections|Connections]]
* [[{Today}_Tasks|Tasks]]
* [[{Today}_Routine|Routine]]
* [[{Today}_Reminders|Reminders]]
* [[{Today}_Bullet-Journal|Bullet-Journal]]
* [[{Today}_Trackers|Trackers]]

# Log

```
SBT WILL APPEND AFTER THIS CODEBLOCK.
```


"""

# ------------------------------------#

DNBJ_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/journal/bullet_journal/{Today}
---

# Bullet_Journal_Log


"""

# ------------------------------------#


DNC_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Connections/{Today}
---

# Connections_Log

"""

# ------------------------------------#
DNE_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Events/{Today}
---

# Events_Log


"""

# ------------------------------------#
DNL_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Location/{Today}
---

# Location_Log


"""

# ------------------------------------#
DNR_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Reminders/{Today}
---

# Reminders_Log


"""
# ------------------------------------#
# ------------------------------------#
DNR2_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/{Today}
---

# Routine_Hours

* [[{Today}_Routine_Hour00|Hour_00]]
* [[{Today}_Routine_Hour01|Hour_01]]
* [[{Today}_Routine_Hour02|Hour_02]]
* [[{Today}_Routine_Hour03|Hour_03]]
* [[{Today}_Routine_Hour04|Hour_04]]
* [[{Today}_Routine_Hour05|Hour_05]]
* [[{Today}_Routine_Hour06|Hour_06]]
* [[{Today}_Routine_Hour07|Hour_07]]
* [[{Today}_Routine_Hour08|Hour_08]]
* [[{Today}_Routine_Hour09|Hour_09]]
* [[{Today}_Routine_Hour10|Hour_10]]
* [[{Today}_Routine_Hour11|Hour_11]]
* [[{Today}_Routine_Hour12|Hour_12]]
* [[{Today}_Routine_Hour13|Hour_13]]
* [[{Today}_Routine_Hour14|Hour_14]]
* [[{Today}_Routine_Hour15|Hour_15]]
* [[{Today}_Routine_Hour16|Hour_16]]
* [[{Today}_Routine_Hour17|Hour_17]]
* [[{Today}_Routine_Hour18|Hour_18]]
* [[{Today}_Routine_Hour19|Hour_19]]
* [[{Today}_Routine_Hour20|Hour_20]]
* [[{Today}_Routine_Hour21|Hour_21]]
* [[{Today}_Routine_Hour22|Hour_22]]
* [[{Today}_Routine_Hour23|Hour_23]]


# Routine_Log


"""
# ------------------------------------#
DNT_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Tasks/{Today}
---

# Tasks_Log


"""
# ------------------------------------#
DNT2_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Trackers/{Today}
---

# Trackers_Links

* [[{Today}_Trackers_Transaction|Transaction]]
* [[{Today}_Trackers_Sleep|Sleep]]
* [[{Today}_Trackers_Meal|Meal]]
* [[{Today}_Trackers_Medicine|Medicine]]
* [[{Today}_Trackers_Mood|Mood]]
* [[{Today}_Trackers_Water|Water]]
* [[{Today}_Trackers_Exercise|Exercise]]
* [[{Today}_Trackers_Symptoms|Symptoms]
* [[{Today}_Trackers_Location|Location]]


# Trackers_Log


"""
# ------------------------------------#
DNTE_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Trackers/Exercise/{Today}
---


# Exercise_Log

> Below are all the Exercise log for today.


"""
# ------------------------------------#
DNTT_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Trackers/Transaction/{Today}
---

# Transaction_Log

> Below are all your Transactions you transacted Today.


"""
# ------------------------------------#
DNTT2_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Trackers/Thoughts/{Today}
---

# Thoughts_Log

> Below are all your Thoughts you had Today.


"""

# ------------------------------------#
DNTL_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Trackers/Location/{Today}
---


# Location_Log

> Below are all the locations you visited today.


"""
# ------------------------------------#
DNTL2_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Link/{Today}
---

# Link_Log


"""
# ------------------------------------#
DNTM_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Trackers/Meal/{Today}
---


# Meal_Log

> Below are all the Meals you took Today.


"""
# ------------------------------------#
DNTM2_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Trackers/Medicine/{Today}
---


# Medicine_Log

> Below are all the Medicine you took Today.


"""
# ------------------------------------#
DNTM3_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Trackers/Mood/{Today}
---


# Mood_Log

> Below are all the Mood you Tracked Today.


"""
# ------------------------------------#
DNTS_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Trackers/Sleep/{Today}
---



# Sleep_Log

> Below are all the Naps you took Today.

"""
# ------------------------------------#
DNTS2_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Trackers/Symptoms/{Today}
---


# Symptoms_Log

> Below are all the Symptoms you observed today.


"""
# ------------------------------------#
DNTW_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Trackers/Water/{Today}
---


# Water_Log

> Below are all the hydration logs for today.


"""


# ------------------------------------#
DNR2_HOUR_00_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_00/{Today}
hour_number: 00
pomodora_task_01: [[{Today}_Routine_Hour-00_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-00_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_00_Log

"""


# ------------------------------------#
DNR2_HOUR_01_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_01/{Today}
hour_number: 01
pomodora_task_01: [[{Today}_Routine_Hour-01_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-01_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_01_Log

"""


# ------------------------------------#
DNR2_HOUR_02_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_02/{Today}
hour_number: 02
pomodora_task_01: [[{Today}_Routine_Hour-02_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-02_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_02_Log

"""


# ------------------------------------#
DNR2_HOUR_03_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_03/{Today}
hour_number: 03
pomodora_task_01: [[{Today}_Routine_Hour-03_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-03_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_03_Log

"""


# ------------------------------------#
DNR2_HOUR_04_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_04/{Today}
hour_number: 04
pomodora_task_01: [[{Today}_Routine_Hour-04_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-04_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_04_Log

"""


# ------------------------------------#
DNR2_HOUR_05_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_05/{Today}
hour_number: 05
pomodora_task_01: [[{Today}_Routine_Hour-05_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-05_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_05_Log

"""


# ------------------------------------#
DNR2_HOUR_06_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_06/{Today}
hour_number: 06
pomodora_task_01: [[{Today}_Routine_Hour-06_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-06_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_06_Log

"""


# ------------------------------------#
DNR2_HOUR_07_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_07/{Today}
hour_number: 07
pomodora_task_01: [[{Today}_Routine_Hour-07_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-07_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_07_Log

"""


# ------------------------------------#
DNR2_HOUR_08_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_08/{Today}
hour_number: 08
pomodora_task_01: [[{Today}_Routine_Hour-08_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-08_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_08_Log

"""


# ------------------------------------#
DNR2_HOUR_09_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_09/{Today}
hour_number: 09
pomodora_task_01: [[{Today}_Routine_Hour-09_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-09_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_09_Log

"""


# ------------------------------------#
DNR2_HOUR_10_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_10/{Today}
hour_number: 10
pomodora_task_01: [[{Today}_Routine_Hour-10_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-10_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_10_Log

"""


# ------------------------------------#
DNR2_HOUR_11_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_11/{Today}
hour_number: 11
pomodora_task_01: [[{Today}_Routine_Hour-11_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-11_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_11_Log

"""


# ------------------------------------#
DNR2_HOUR_12_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_12/{Today}
hour_number: 12
pomodora_task_01: [[{Today}_Routine_Hour-12_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-12_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_12_Log

"""


# ------------------------------------#
DNR2_HOUR_13_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_13/{Today}
hour_number: 13
pomodora_task_01: [[{Today}_Routine_Hour-13_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-13_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_13_Log

"""


# ------------------------------------#
DNR2_HOUR_14_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_14/{Today}
hour_number: 14
pomodora_task_01: [[{Today}_Routine_Hour-14_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-14_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_14_Log

"""


# ------------------------------------#
DNR2_HOUR_15_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_15/{Today}
hour_number: 15
pomodora_task_01: [[{Today}_Routine_Hour-15_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-15_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_15_Log

"""


# ------------------------------------#
DNR2_HOUR_16_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_16/{Today}
hour_number: 16
pomodora_task_01: [[{Today}_Routine_Hour-16_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-16_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_16_Log

"""


# ------------------------------------#
DNR2_HOUR_17_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_17/{Today}
hour_number: 17
pomodora_task_01: [[{Today}_Routine_Hour-17_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-17_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_17_Log

"""


# ------------------------------------#
DNR2_HOUR_18_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_18/{Today}
hour_number: 18
pomodora_task_01: [[{Today}_Routine_Hour-18_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-18_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_18_Log

"""


# ------------------------------------#
DNR2_HOUR_19_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour-19/{Today}
hour_number: 19
pomodora_task_01: [[{Today}_Routine_Hour-19_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-19_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_19_Log

"""


# ------------------------------------#
DNR2_HOUR_20_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_20/{Today}
hour_number: 20
pomodora_task_01: [[{Today}_Routine_Hour-20_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-20_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_20_Log

"""


# ------------------------------------#
DNR2_HOUR_21_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_21/{Today}
hour_number: 21
pomodora_task_01: [[{Today}_Routine_Hour-21_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-21_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_21_Log

"""


# ------------------------------------#
DNR2_HOUR_22_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_22/{Today}
hour_number: 22
pomodora_task_01: [[{Today}_Routine_Hour-22_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-22_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_22_Log

"""


# ------------------------------------#
DNR2_HOUR_23_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/Routine/Hour_23/{Today}
hour_number: 23
pomodora_task_01: [[{Today}_Routine_Hour-23_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Hour-23_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_23_Log

"""

# Capture.py


def capture_event_content_creation(event_name, event_type, event_location, event_summary, event_status):
    """ """
    CE_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/event/{Today}/{event_name}
event_type: {event_type}
event_name: {event_name}
event_location: {event_location}
event_summary: {event_summary}
event_status: {event_status}
---

# Event_Log

"""
    return CE_FILE_CONTENT_CREATION


def capture_task_content_creation(
    Task_Name,
    Task_Status,
    Task_Priority,
    Task_Labels,
    Task_Dependencies,
    Task_Parent_Task,
    TASK_SUB_TASK,
):
    CT_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/tasks/{Today}/{Task_Name}
task_name: {Task_Name}
task_status: {Task_Status}
task_priority: {Task_Priority}
task_labels: {Task_Labels}
task_dependencies: [[{Task_Dependencies}]]
task_parent_task: [[{Task_Parent_Task}]]
task_sub_task: [[{TASK_SUB_TASK}]]
---

# Task_Log


"""
    return CT_FILE_CONTENT_CREATION


def capture_thought_content_creation(
    Thought_Name,
    Thought_Summary,
    Thought_Content,
):
    CT2_FILE_CONTENT_CREATION = f"""---
tags: daily_note/thoughts/{Today}/{Thought_Name}
date: {Today}
time: {CURRENT_TIME}
thought_name: {Thought_Name}
thought_summary: {Thought_Summary}
---

# Thought_Log

{Thought_Content}


    """
    return CT2_FILE_CONTENT_CREATION


def capture_reminder_content_creation(
    Reminder_Name,
    Reminder_Priority,
    Reminder_Labels,
    Reminder_Time,
):
    CR_FILE_CONTENT_CREATION = f"""---
date: {Today}
time: {CURRENT_TIME}
tags: daily_note/Reminders/{Today}/{Reminder_Name}
reminder_name: {Reminder_Name}
reminder_priority: {Reminder_Priority}
reminder_labels: {Reminder_Labels}
reminder_time_to_remind: {Reminder_Time}
---

# Reminder_Log


    """
    return CR_FILE_CONTENT_CREATION


def capture_bullet_journal_content_creation():
    CBJ_FILE_CONTENT_CREATION = f"""---
tags: daily_note/Bullet_Journal/{Today}
date: {Today}
time: {CURRENT_TIME}
---

# Bullet_Journal


    """
    return CBJ_FILE_CONTENT_CREATION


def capture_transaction_content_creation(
    Transaction_Name,
    Transaction_Time,
    Transaction_Type,
    Transaction_Amount,
    Transaction_Account,
    Transaction_Invoice,
):
    CTCC_FILE_CONTENT_CREATION = f"""---
tags: daily_note/transactions/{Transaction_Type}/{Today}
time: {CURRENT_TIME}
date: {Today}
transaction_name: {Transaction_Name}
transaction_time: {Transaction_Time}
transaction_type: {Transaction_Type}
transaction_amount: {Transaction_Amount}
transaction_account: {Transaction_Account}
transaction_invoice: {Transaction_Invoice}
---

# Transaction_Log

    """
    return CTCC_FILE_CONTENT_CREATION


def capture_sleep_content_creation(Sleep_name, Sleep_Type, Sleep_Hours, Sleep_Time):
    CSCC_FILE_CONTENT_CREATION = f"""---
tags: daily_note/sleep/{Sleep_Type}/{Today}
date: {Today}
time: {CURRENT_TIME}
sleep_name: {Sleep_name}
sleep_type: {Sleep_Type}
sleep_hours: {Sleep_Hours}
sleep_time: {Sleep_Time}
---

# Sleep_Log

    """
    return CSCC_FILE_CONTENT_CREATION


def capture_meal_content_creation(Meal_Name, Meal_Time, Meal_Type, Meal_Calories, Meal_Taken):
    CMCC_FILE_CONTENT_CREATION = f"""---
tags: daily_note/meal/{Meal_Type}/{Today}
date: {Today}
time: {Meal_Time}
meal_name: {Meal_Name}
meal_type: {Meal_Type}
meal_calories: {Meal_Calories}
meal_taken: {Meal_Taken}
---

# Meal_Log

    """
    return CMCC_FILE_CONTENT_CREATION


def capture_medicine_content_creation(Medicine_Name, Medicine_Time, Medicine_Type, Medicine_Taken):
    CM2CC_FILE_CONTENT_CREATION = f"""---
tags: daily_note/medicine/{Medicine_Name}/{Today}
date: {Today}
time: {CURRENT_TIME}
medicine_name: {Medicine_Name}
medicine_time: {Medicine_Time}
medicine_type: {Medicine_Type}
medicine_side_effect : "write if you observed any side effects"
medicine_taken: {Medicine_Taken}
---

# Medicine_Log

    """
    return CM2CC_FILE_CONTENT_CREATION


def capture_mood_content_creation(
    Mood_Name,
    Mood_Status,
    Mood_Reason
):
    CTCC_FILE_CONTENT_CREATION = f"""---
tags: daily_note/mood/{Mood_Status}/{Today}
date: {Today}
time: {CURRENT_TIME}
name: {Mood_Name}
mood_status: {Mood_Status}
mood_reason: {Mood_Reason}
---

# Mood_Log

    """
    return CTCC_FILE_CONTENT_CREATION


def capture_water_intake_content_creation(
    Water_Intake_Name,
    Water_Intake_Time,
    Water_Intake_Amount_In_ML
):
    CWICC_FILE_CONTENT_CREATION = f"""---
tags: daily_note/water_intake/{Today}
date: {Today}
time: {CURRENT_TIME}
name: {Water_Intake_Name}
water_intake_time: {Water_Intake_Time}
water_intake_ml: {Water_Intake_Amount_In_ML}
---

# Water_Log

"""
    return CWICC_FILE_CONTENT_CREATION


def capture_exercise_content_creation(
    Exercise_Name,
    Exercise_Time,
    Exercise_Cohort,
    Exercise_Status,
):
    CECC_CONTENT_CREATION = f"""---
tags: daily_note/exercise//{Today}
date: {Today}
time: {CURRENT_TIME}
exercise_name: {Exercise_Name}
exercise_time: {Exercise_Time}
exercise_cohort: {Exercise_Cohort}
exercise_status: {Exercise_Status}
---

# Exercise_Log

"""
    return CECC_CONTENT_CREATION


def capture_link_content_creation(Link_Name, URL, Link_Domain_Name):

    CLCC_CONTENT_CREATION = f"""---
tags: daily_note/links/{Link_Domain_Name}/{Today}
name: {Link_Name}
date: {Today}
time: {CURRENT_TIME}
domain: {Link_Domain_Name}
url: {URL}
---

# Link_Log

"""
    return CLCC_CONTENT_CREATION


def capture_symptoms_content_creation(
    Symptom_Name,
    Symptom_Status,
):
    CSCC_CONTENT_CREATION = f"""---
tags: daily_note/symptoms/{Symptom_Name}/{Today}
date: {Today}
time: {CURRENT_TIME}
name: {Symptom_Name}
symptom_status: {Symptom_Status}
---

# Symptom_Log

"""
    return CSCC_CONTENT_CREATION


# Capture/Routines Started
def capture_routine_hour_00_pomodora_1_content_creation(
    CR_HOUR_00_POMODORA_1_TASK_NAME,
    CR_HOUR_00_POMODORA_1_TASK_STATUS,
    CR_HOUR_00_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_00_POMODORA_1_TASK_LABELS,
    CR_HOUR_00_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_00_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_00_POMODORA_1_TASK_SUB_TASK,
):
    CRH00P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_00/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_00_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_00_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_00_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_00_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_00_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_00_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_00_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH00P1_FILE_CONTENT_CREATION


def capture_routine_hour_00_pomodora_2_content_creation(
    CR_HOUR_00_POMODORA_2_TASK_NAME,
    CR_HOUR_00_POMODORA_2_TASK_STATUS,
    CR_HOUR_00_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_00_POMODORA_2_TASK_LABELS,
    CR_HOUR_00_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_00_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_00_POMODORA_2_TASK_SUB_TASK,
):
    CRH00P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_00/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_00_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_00_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_00_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_00_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_00_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_00_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_00_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH00P2_FILE_CONTENT_CREATION


def capture_routine_hour_01_pomodora_1_content_creation(
    CR_HOUR_01_POMODORA_1_TASK_NAME,
    CR_HOUR_01_POMODORA_1_TASK_STATUS,
    CR_HOUR_01_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_01_POMODORA_1_TASK_LABELS,
    CR_HOUR_01_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_01_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_01_POMODORA_1_TASK_SUB_TASK,
):
    CRH01P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_01/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_01_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_01_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_01_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_01_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_01_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_01_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_01_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH01P1_FILE_CONTENT_CREATION


def capture_routine_hour_01_pomodora_2_content_creation(
    CR_HOUR_01_POMODORA_2_TASK_NAME,
    CR_HOUR_01_POMODORA_2_TASK_STATUS,
    CR_HOUR_01_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_01_POMODORA_2_TASK_LABELS,
    CR_HOUR_01_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_01_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_01_POMODORA_2_TASK_SUB_TASK,
):
    CRH01P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_01/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_01_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_01_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_01_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_01_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_01_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_01_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_01_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH01P2_FILE_CONTENT_CREATION


def capture_routine_hour_02_pomodora_1_content_creation(
    CR_HOUR_02_POMODORA_1_TASK_NAME,
    CR_HOUR_02_POMODORA_1_TASK_STATUS,
    CR_HOUR_02_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_02_POMODORA_1_TASK_LABELS,
    CR_HOUR_02_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_02_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_02_POMODORA_1_TASK_SUB_TASK,
):
    CRH02P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_02/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_02_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_02_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_02_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_02_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_02_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_02_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_02_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH02P1_FILE_CONTENT_CREATION


def capture_routine_hour_02_pomodora_2_content_creation(
    CR_HOUR_02_POMODORA_2_TASK_NAME,
    CR_HOUR_02_POMODORA_2_TASK_STATUS,
    CR_HOUR_02_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_02_POMODORA_2_TASK_LABELS,
    CR_HOUR_02_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_02_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_02_POMODORA_2_TASK_SUB_TASK,
):
    CRH02P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_02/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_02_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_02_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_02_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_02_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_02_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_02_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_02_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH02P2_FILE_CONTENT_CREATION


def capture_routine_hour_03_pomodora_1_content_creation(
    CR_HOUR_03_POMODORA_1_TASK_NAME,
    CR_HOUR_03_POMODORA_1_TASK_STATUS,
    CR_HOUR_03_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_03_POMODORA_1_TASK_LABELS,
    CR_HOUR_03_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_03_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_03_POMODORA_1_TASK_SUB_TASK,
):
    CRH03P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_03/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_03_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_03_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_03_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_03_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_03_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_03_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_03_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH03P1_FILE_CONTENT_CREATION


def capture_routine_hour_03_pomodora_2_content_creation(
    CR_HOUR_03_POMODORA_2_TASK_NAME,
    CR_HOUR_03_POMODORA_2_TASK_STATUS,
    CR_HOUR_03_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_03_POMODORA_2_TASK_LABELS,
    CR_HOUR_03_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_03_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_03_POMODORA_2_TASK_SUB_TASK,
):
    CRH03P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_03/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_03_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_03_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_03_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_03_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_03_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_03_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_03_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH03P2_FILE_CONTENT_CREATION


def capture_routine_hour_04_pomodora_1_content_creation(
    CR_HOUR_04_POMODORA_1_TASK_NAME,
    CR_HOUR_04_POMODORA_1_TASK_STATUS,
    CR_HOUR_04_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_04_POMODORA_1_TASK_LABELS,
    CR_HOUR_04_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_04_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_04_POMODORA_1_TASK_SUB_TASK,
):
    CRH04P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_04/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_04_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_04_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_04_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_04_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_04_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_04_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_04_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH04P1_FILE_CONTENT_CREATION


def capture_routine_hour_04_pomodora_2_content_creation(
    CR_HOUR_04_POMODORA_2_TASK_NAME,
    CR_HOUR_04_POMODORA_2_TASK_STATUS,
    CR_HOUR_04_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_04_POMODORA_2_TASK_LABELS,
    CR_HOUR_04_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_04_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_04_POMODORA_2_TASK_SUB_TASK,
):
    CRH04P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_04/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_04_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_04_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_04_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_04_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_04_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_04_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_04_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH04P2_FILE_CONTENT_CREATION


def capture_routine_hour_05_pomodora_1_content_creation(
    CR_HOUR_05_POMODORA_1_TASK_NAME,
    CR_HOUR_05_POMODORA_1_TASK_STATUS,
    CR_HOUR_05_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_05_POMODORA_1_TASK_LABELS,
    CR_HOUR_05_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_05_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_05_POMODORA_1_TASK_SUB_TASK,
):
    CRH05P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_05/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_05_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_05_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_05_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_05_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_05_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_05_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_05_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH05P1_FILE_CONTENT_CREATION


def capture_routine_hour_05_pomodora_2_content_creation(
    CR_HOUR_05_POMODORA_2_TASK_NAME,
    CR_HOUR_05_POMODORA_2_TASK_STATUS,
    CR_HOUR_05_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_05_POMODORA_2_TASK_LABELS,
    CR_HOUR_05_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_05_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_05_POMODORA_2_TASK_SUB_TASK,
):
    CRH05P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_05/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_05_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_05_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_05_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_05_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_05_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_05_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_05_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH05P2_FILE_CONTENT_CREATION


def capture_routine_hour_06_pomodora_1_content_creation(
    CR_HOUR_06_POMODORA_1_TASK_NAME,
    CR_HOUR_06_POMODORA_1_TASK_STATUS,
    CR_HOUR_06_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_06_POMODORA_1_TASK_LABELS,
    CR_HOUR_06_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_06_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_06_POMODORA_1_TASK_SUB_TASK,
):
    CRH06P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_06/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_06_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_06_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_06_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_06_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_06_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_06_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_06_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH06P1_FILE_CONTENT_CREATION


def capture_routine_hour_06_pomodora_2_content_creation(
    CR_HOUR_06_POMODORA_2_TASK_NAME,
    CR_HOUR_06_POMODORA_2_TASK_STATUS,
    CR_HOUR_06_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_06_POMODORA_2_TASK_LABELS,
    CR_HOUR_06_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_06_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_06_POMODORA_2_TASK_SUB_TASK,
):
    CRH06P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_06/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_06_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_06_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_06_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_06_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_06_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_06_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_06_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH06P2_FILE_CONTENT_CREATION


def capture_routine_hour_07_pomodora_1_content_creation(
    CR_HOUR_07_POMODORA_1_TASK_NAME,
    CR_HOUR_07_POMODORA_1_TASK_STATUS,
    CR_HOUR_07_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_07_POMODORA_1_TASK_LABELS,
    CR_HOUR_07_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_07_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_07_POMODORA_1_TASK_SUB_TASK,
):
    CRH07P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_07/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_07_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_07_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_07_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_07_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_07_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_07_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_07_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH07P1_FILE_CONTENT_CREATION


def capture_routine_hour_07_pomodora_2_content_creation(
    CR_HOUR_07_POMODORA_2_TASK_NAME,
    CR_HOUR_07_POMODORA_2_TASK_STATUS,
    CR_HOUR_07_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_07_POMODORA_2_TASK_LABELS,
    CR_HOUR_07_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_07_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_07_POMODORA_2_TASK_SUB_TASK,
):
    CRH07P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_07/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_07_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_07_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_07_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_07_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_07_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_07_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_07_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH07P2_FILE_CONTENT_CREATION


def capture_routine_hour_08_pomodora_1_content_creation(
    CR_HOUR_08_POMODORA_1_TASK_NAME,
    CR_HOUR_08_POMODORA_1_TASK_STATUS,
    CR_HOUR_08_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_08_POMODORA_1_TASK_LABELS,
    CR_HOUR_08_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_08_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_08_POMODORA_1_TASK_SUB_TASK,
):
    CRH08P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_08/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_08_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_08_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_08_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_08_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_08_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_08_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_08_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH08P1_FILE_CONTENT_CREATION


def capture_routine_hour_08_pomodora_2_content_creation(
    CR_HOUR_08_POMODORA_2_TASK_NAME,
    CR_HOUR_08_POMODORA_2_TASK_STATUS,
    CR_HOUR_08_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_08_POMODORA_2_TASK_LABELS,
    CR_HOUR_08_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_08_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_08_POMODORA_2_TASK_SUB_TASK,
):
    CRH08P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_08/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_08_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_08_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_08_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_08_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_08_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_08_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_08_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH08P2_FILE_CONTENT_CREATION


def capture_routine_hour_09_pomodora_1_content_creation(
    CR_HOUR_09_POMODORA_1_TASK_NAME,
    CR_HOUR_09_POMODORA_1_TASK_STATUS,
    CR_HOUR_09_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_09_POMODORA_1_TASK_LABELS,
    CR_HOUR_09_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_09_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_09_POMODORA_1_TASK_SUB_TASK,
):
    CRH09P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_09/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_09_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_09_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_09_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_09_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_09_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_09_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_09_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH09P1_FILE_CONTENT_CREATION


def capture_routine_hour_09_pomodora_2_content_creation(
    CR_HOUR_09_POMODORA_2_TASK_NAME,
    CR_HOUR_09_POMODORA_2_TASK_STATUS,
    CR_HOUR_09_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_09_POMODORA_2_TASK_LABELS,
    CR_HOUR_09_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_09_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_09_POMODORA_2_TASK_SUB_TASK,
):
    CRH09P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_09/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_09_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_09_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_09_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_09_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_09_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_09_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_09_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH09P2_FILE_CONTENT_CREATION


def capture_routine_hour_10_pomodora_1_content_creation(
    CR_HOUR_10_POMODORA_1_TASK_NAME,
    CR_HOUR_10_POMODORA_1_TASK_STATUS,
    CR_HOUR_10_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_10_POMODORA_1_TASK_LABELS,
    CR_HOUR_10_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_10_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_10_POMODORA_1_TASK_SUB_TASK,
):
    CRH10P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_10/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_10_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_10_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_10_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_10_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_10_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_10_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_10_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH10P1_FILE_CONTENT_CREATION


def capture_routine_hour_10_pomodora_2_content_creation(
    CR_HOUR_10_POMODORA_2_TASK_NAME,
    CR_HOUR_10_POMODORA_2_TASK_STATUS,
    CR_HOUR_10_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_10_POMODORA_2_TASK_LABELS,
    CR_HOUR_10_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_10_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_10_POMODORA_2_TASK_SUB_TASK,
):
    CRH10P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_10/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_10_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_10_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_10_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_10_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_10_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_10_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_10_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH10P2_FILE_CONTENT_CREATION


def capture_routine_hour_11_pomodora_1_content_creation(
    CR_HOUR_11_POMODORA_1_TASK_NAME,
    CR_HOUR_11_POMODORA_1_TASK_STATUS,
    CR_HOUR_11_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_11_POMODORA_1_TASK_LABELS,
    CR_HOUR_11_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_11_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_11_POMODORA_1_TASK_SUB_TASK,
):
    CRH11P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_11/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_11_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_11_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_11_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_11_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_11_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_11_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_11_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH11P1_FILE_CONTENT_CREATION


def capture_routine_hour_11_pomodora_2_content_creation(
    CR_HOUR_11_POMODORA_2_TASK_NAME,
    CR_HOUR_11_POMODORA_2_TASK_STATUS,
    CR_HOUR_11_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_11_POMODORA_2_TASK_LABELS,
    CR_HOUR_11_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_11_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_11_POMODORA_2_TASK_SUB_TASK,
):
    CRH11P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_11/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_11_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_11_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_11_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_11_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_11_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_11_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_11_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH11P2_FILE_CONTENT_CREATION


def capture_routine_hour_12_pomodora_1_content_creation(
    CR_HOUR_12_POMODORA_1_TASK_NAME,
    CR_HOUR_12_POMODORA_1_TASK_STATUS,
    CR_HOUR_12_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_12_POMODORA_1_TASK_LABELS,
    CR_HOUR_12_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_12_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_12_POMODORA_1_TASK_SUB_TASK,
):
    CRH12P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_12/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_12_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_12_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_12_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_12_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_12_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_12_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_12_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH12P1_FILE_CONTENT_CREATION


def capture_routine_hour_12_pomodora_2_content_creation(
    CR_HOUR_12_POMODORA_2_TASK_NAME,
    CR_HOUR_12_POMODORA_2_TASK_STATUS,
    CR_HOUR_12_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_12_POMODORA_2_TASK_LABELS,
    CR_HOUR_12_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_12_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_12_POMODORA_2_TASK_SUB_TASK,
):
    CRH12P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_12/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_12_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_12_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_12_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_12_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_12_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_12_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_12_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH12P2_FILE_CONTENT_CREATION


def capture_routine_hour_13_pomodora_1_content_creation(
    CR_HOUR_13_POMODORA_1_TASK_NAME,
    CR_HOUR_13_POMODORA_1_TASK_STATUS,
    CR_HOUR_13_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_13_POMODORA_1_TASK_LABELS,
    CR_HOUR_13_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_13_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_13_POMODORA_1_TASK_SUB_TASK,
):
    CRH13P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_13/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_13_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_13_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_13_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_13_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_13_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_13_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_13_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH13P1_FILE_CONTENT_CREATION


def capture_routine_hour_13_pomodora_2_content_creation(
    CR_HOUR_13_POMODORA_2_TASK_NAME,
    CR_HOUR_13_POMODORA_2_TASK_STATUS,
    CR_HOUR_13_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_13_POMODORA_2_TASK_LABELS,
    CR_HOUR_13_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_13_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_13_POMODORA_2_TASK_SUB_TASK,
):
    CRH13P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_13/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_13_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_13_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_13_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_13_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_13_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_13_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_13_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH13P2_FILE_CONTENT_CREATION


def capture_routine_hour_14_pomodora_1_content_creation(
    CR_HOUR_14_POMODORA_1_TASK_NAME,
    CR_HOUR_14_POMODORA_1_TASK_STATUS,
    CR_HOUR_14_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_14_POMODORA_1_TASK_LABELS,
    CR_HOUR_14_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_14_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_14_POMODORA_1_TASK_SUB_TASK,
):
    CRH14P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_14/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_14_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_14_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_14_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_14_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_14_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_14_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_14_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH14P1_FILE_CONTENT_CREATION


def capture_routine_hour_14_pomodora_2_content_creation(
    CR_HOUR_14_POMODORA_2_TASK_NAME,
    CR_HOUR_14_POMODORA_2_TASK_STATUS,
    CR_HOUR_14_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_14_POMODORA_2_TASK_LABELS,
    CR_HOUR_14_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_14_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_14_POMODORA_2_TASK_SUB_TASK,
):
    CRH14P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_14/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_14_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_14_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_14_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_14_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_14_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_14_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_14_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH14P2_FILE_CONTENT_CREATION


def capture_routine_hour_15_pomodora_1_content_creation(
    CR_HOUR_15_POMODORA_1_TASK_NAME,
    CR_HOUR_15_POMODORA_1_TASK_STATUS,
    CR_HOUR_15_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_15_POMODORA_1_TASK_LABELS,
    CR_HOUR_15_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_15_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_15_POMODORA_1_TASK_SUB_TASK,
):
    CRH15P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_15/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_15_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_15_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_15_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_15_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_15_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_15_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_15_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH15P1_FILE_CONTENT_CREATION


def capture_routine_hour_15_pomodora_2_content_creation(
    CR_HOUR_15_POMODORA_2_TASK_NAME,
    CR_HOUR_15_POMODORA_2_TASK_STATUS,
    CR_HOUR_15_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_15_POMODORA_2_TASK_LABELS,
    CR_HOUR_15_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_15_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_15_POMODORA_2_TASK_SUB_TASK,
):
    CRH15P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_15/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_15_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_15_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_15_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_15_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_15_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_15_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_15_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH15P2_FILE_CONTENT_CREATION


def capture_routine_hour_16_pomodora_1_content_creation(
    CR_HOUR_16_POMODORA_1_TASK_NAME,
    CR_HOUR_16_POMODORA_1_TASK_STATUS,
    CR_HOUR_16_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_16_POMODORA_1_TASK_LABELS,
    CR_HOUR_16_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_16_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_16_POMODORA_1_TASK_SUB_TASK,
):
    CRH16P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_16/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_16_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_16_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_16_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_16_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_16_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_16_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_16_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH16P1_FILE_CONTENT_CREATION


def capture_routine_hour_16_pomodora_2_content_creation(
    CR_HOUR_16_POMODORA_2_TASK_NAME,
    CR_HOUR_16_POMODORA_2_TASK_STATUS,
    CR_HOUR_16_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_16_POMODORA_2_TASK_LABELS,
    CR_HOUR_16_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_16_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_16_POMODORA_2_TASK_SUB_TASK,
):
    CRH16P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_16/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_16_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_16_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_16_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_16_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_16_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_16_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_16_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH16P2_FILE_CONTENT_CREATION


def capture_routine_hour_17_pomodora_1_content_creation(
    CR_HOUR_17_POMODORA_1_TASK_NAME,
    CR_HOUR_17_POMODORA_1_TASK_STATUS,
    CR_HOUR_17_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_17_POMODORA_1_TASK_LABELS,
    CR_HOUR_17_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_17_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_17_POMODORA_1_TASK_SUB_TASK,
):
    CRH17P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_17/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_17_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_17_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_17_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_17_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_17_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_17_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_17_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH17P1_FILE_CONTENT_CREATION


def capture_routine_hour_17_pomodora_2_content_creation(
    CR_HOUR_17_POMODORA_2_TASK_NAME,
    CR_HOUR_17_POMODORA_2_TASK_STATUS,
    CR_HOUR_17_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_17_POMODORA_2_TASK_LABELS,
    CR_HOUR_17_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_17_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_17_POMODORA_2_TASK_SUB_TASK,
):
    CRH17P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_17/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_17_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_17_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_17_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_17_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_17_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_17_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_17_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH17P2_FILE_CONTENT_CREATION


def capture_routine_hour_18_pomodora_1_content_creation(
    CR_HOUR_18_POMODORA_1_TASK_NAME,
    CR_HOUR_18_POMODORA_1_TASK_STATUS,
    CR_HOUR_18_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_18_POMODORA_1_TASK_LABELS,
    CR_HOUR_18_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_18_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_18_POMODORA_1_TASK_SUB_TASK,
):
    CRH18P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_18/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_18_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_18_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_18_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_18_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_18_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_18_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_18_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH18P1_FILE_CONTENT_CREATION


def capture_routine_hour_18_pomodora_2_content_creation(
    CR_HOUR_18_POMODORA_2_TASK_NAME,
    CR_HOUR_18_POMODORA_2_TASK_STATUS,
    CR_HOUR_18_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_18_POMODORA_2_TASK_LABELS,
    CR_HOUR_18_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_18_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_18_POMODORA_2_TASK_SUB_TASK,
):
    CRH18P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_18/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_18_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_18_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_18_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_18_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_18_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_18_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_18_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH18P2_FILE_CONTENT_CREATION


def capture_routine_hour_19_pomodora_1_content_creation(
    CR_HOUR_19_POMODORA_1_TASK_NAME,
    CR_HOUR_19_POMODORA_1_TASK_STATUS,
    CR_HOUR_19_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_19_POMODORA_1_TASK_LABELS,
    CR_HOUR_19_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_19_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_19_POMODORA_1_TASK_SUB_TASK,
):
    CRH19P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_19/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_19_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_19_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_19_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_19_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_19_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_19_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_19_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH19P1_FILE_CONTENT_CREATION


def capture_routine_hour_19_pomodora_2_content_creation(
    CR_HOUR_19_POMODORA_2_TASK_NAME,
    CR_HOUR_19_POMODORA_2_TASK_STATUS,
    CR_HOUR_19_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_19_POMODORA_2_TASK_LABELS,
    CR_HOUR_19_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_19_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_19_POMODORA_2_TASK_SUB_TASK,
):
    CRH19P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_19/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_19_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_19_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_19_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_19_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_19_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_19_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_19_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH19P2_FILE_CONTENT_CREATION


def capture_routine_hour_20_pomodora_1_content_creation(
    CR_HOUR_20_POMODORA_1_TASK_NAME,
    CR_HOUR_20_POMODORA_1_TASK_STATUS,
    CR_HOUR_20_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_20_POMODORA_1_TASK_LABELS,
    CR_HOUR_20_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_20_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_20_POMODORA_1_TASK_SUB_TASK,
):
    CRH20P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_20/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_20_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_20_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_20_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_20_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_20_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_20_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_20_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH20P1_FILE_CONTENT_CREATION


def capture_routine_hour_20_pomodora_2_content_creation(
    CR_HOUR_20_POMODORA_2_TASK_NAME,
    CR_HOUR_20_POMODORA_2_TASK_STATUS,
    CR_HOUR_20_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_20_POMODORA_2_TASK_LABELS,
    CR_HOUR_20_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_20_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_20_POMODORA_2_TASK_SUB_TASK,
):
    CRH20P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_20/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_20_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_20_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_20_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_20_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_20_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_20_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_20_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH20P2_FILE_CONTENT_CREATION


def capture_routine_hour_21_pomodora_1_content_creation(
    CR_HOUR_21_POMODORA_1_TASK_NAME,
    CR_HOUR_21_POMODORA_1_TASK_STATUS,
    CR_HOUR_21_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_21_POMODORA_1_TASK_LABELS,
    CR_HOUR_21_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_21_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_21_POMODORA_1_TASK_SUB_TASK,
):
    CRH21P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_21/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_21_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_21_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_21_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_21_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_21_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_21_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_21_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH21P1_FILE_CONTENT_CREATION


def capture_routine_hour_21_pomodora_2_content_creation(
    CR_HOUR_21_POMODORA_2_TASK_NAME,
    CR_HOUR_21_POMODORA_2_TASK_STATUS,
    CR_HOUR_21_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_21_POMODORA_2_TASK_LABELS,
    CR_HOUR_21_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_21_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_21_POMODORA_2_TASK_SUB_TASK,
):
    CRH21P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_21/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_21_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_21_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_21_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_21_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_21_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_21_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_21_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH21P2_FILE_CONTENT_CREATION


def capture_routine_hour_22_pomodora_1_content_creation(
    CR_HOUR_22_POMODORA_1_TASK_NAME,
    CR_HOUR_22_POMODORA_1_TASK_STATUS,
    CR_HOUR_22_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_22_POMODORA_1_TASK_LABELS,
    CR_HOUR_22_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_22_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_22_POMODORA_1_TASK_SUB_TASK,
):
    CRH22P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_22/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_22_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_22_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_22_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_22_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_22_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_22_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_22_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH22P1_FILE_CONTENT_CREATION


def capture_routine_hour_22_pomodora_2_content_creation(
    CR_HOUR_22_POMODORA_2_TASK_NAME,
    CR_HOUR_22_POMODORA_2_TASK_STATUS,
    CR_HOUR_22_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_22_POMODORA_2_TASK_LABELS,
    CR_HOUR_22_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_22_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_22_POMODORA_2_TASK_SUB_TASK,
):
    CRH22P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_22/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_22_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_22_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_22_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_22_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_22_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_22_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_22_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH22P2_FILE_CONTENT_CREATION


def capture_routine_hour_23_pomodora_1_content_creation(
    CR_HOUR_23_POMODORA_1_TASK_NAME,
    CR_HOUR_23_POMODORA_1_TASK_STATUS,
    CR_HOUR_23_POMODORA_1_TASK_PRIORITY,
    CR_HOUR_23_POMODORA_1_TASK_LABELS,
    CR_HOUR_23_POMODORA_1_TASK_DEPENDENCIES,
    CR_HOUR_23_POMODORA_1_TASK_PARENT_TASK,
    CR_HOUR_23_POMODORA_1_TASK_SUB_TASK,
):
    CRH23P1_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_23/Task_01/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_23_POMODORA_1_TASK_NAME}
    pomodora_task_status: {CR_HOUR_23_POMODORA_1_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_23_POMODORA_1_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_23_POMODORA_1_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_23_POMODORA_1_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_23_POMODORA_1_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_23_POMODORA_1_TASK_SUB_TASK}
    ---


# POMODORA_1_LOG


"""
    return CRH23P1_FILE_CONTENT_CREATION


def capture_routine_hour_23_pomodora_2_content_creation(
    CR_HOUR_23_POMODORA_2_TASK_NAME,
    CR_HOUR_23_POMODORA_2_TASK_STATUS,
    CR_HOUR_23_POMODORA_2_TASK_PRIORITY,
    CR_HOUR_23_POMODORA_2_TASK_LABELS,
    CR_HOUR_23_POMODORA_2_TASK_DEPENDENCIES,
    CR_HOUR_23_POMODORA_2_TASK_PARENT_TASK,
    CR_HOUR_23_POMODORA_2_TASK_SUB_TASK,
):
    CRH23P2_FILE_CONTENT_CREATION = f"""---
    date: {Today}
    tags: daily_note/Routine/Hour_23/Task_02/{Today}
    time: {CURRENT_TIME}
    pomodora_task_name: {CR_HOUR_23_POMODORA_2_TASK_NAME}
    pomodora_task_status: {CR_HOUR_23_POMODORA_2_TASK_STATUS}
    pomodora_task_priority: {CR_HOUR_23_POMODORA_2_TASK_PRIORITY}
    pomodora_task_labels: {CR_HOUR_23_POMODORA_2_TASK_LABELS}
    pomodora_task_dependencies: {CR_HOUR_23_POMODORA_2_TASK_DEPENDENCIES}
    pomodora_task_parent_task: {CR_HOUR_23_POMODORA_2_TASK_PARENT_TASK}
    pomodora_task_sub_task: {CR_HOUR_23_POMODORA_2_TASK_SUB_TASK}
    ---


# POMODORA_2_LOG


"""
    return CRH23P2_FILE_CONTENT_CREATION
