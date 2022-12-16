# Importing production modules // Meant for production branch
from second_brain_tools.time import Today
# Importing production modules finished


# Daily Note File Creation Content String Started
# Daily Note File Creation Content String Finished
DNM_FILE_CONTENT_CREATION = f"""---
tags :
 - daily_note/{Today}
 - {Today}
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
tags: daily_note/{Today}/journal/bullet_journal
---

# Bullet_Journal_Log


"""

# ------------------------------------#


DNC_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Connections
---

# Connections_Log

"""

# ------------------------------------#
DNE_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Events
---

# Events_Log


"""

# ------------------------------------#
DNL_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Location
---

# Location_Log


"""

# ------------------------------------#
DNR_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Reminders
---

# Reminders_Log


"""
# ------------------------------------#
# ------------------------------------#
DNR2_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Routine
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
tags: daily_note/{Today}/Tasks
---

# Tasks_Log


"""
# ------------------------------------#
DNT2_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Trackers
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
tags: daily_note/{Today}/Trackers/Exercise
---


# Exercise_Log

> Below are all the Exercise log for today.


"""
# ------------------------------------#
DNTT_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Trackers/Transaction
---

# Transaction_Log

> Below are all your Transactions you transacted Today.


"""
# ------------------------------------#
DNTL_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Trackers/Location
---


# Location_Log

> Below are all the locations you visited today.


"""
# ------------------------------------#
DNTM_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Trackers/Meal
---


# Meal_Log

> Below are all the Meals you took Today.


"""
# ------------------------------------#
DNTM2_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Trackers/Medicine
---


# Medicine_Log

> Below are all the Medicine you took Today.


"""
# ------------------------------------#
DNTM3_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Trackers/Mood
---


# Mood_Log

> Below are all the Mood you Tracked Today.


"""
# ------------------------------------#
DNTS_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Trackers/Sleep
---



# Sleep_Log

> Below are all the Naps you took Today.

"""
# ------------------------------------#
DNTS2_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Trackers/Symptoms
---


# Symptoms_Log

> Below are all the Symptoms you observed today.


"""
# ------------------------------------#
DNTW_FILE_CONTENT_CREATION = f"""---
date: {Today}
tags: daily_note/{Today}/Trackers/Water
---


# Water_Log

> Below are all the hydration logs for today.


"""


# ------------------------------------#
DNR2_HOUR_00_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_00
hour_number: 00
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_00_Log

"""


# ------------------------------------#
DNR2_HOUR_01_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_01
hour_number: 01
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_01_Log

"""


# ------------------------------------#
DNR2_HOUR_02_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_02
hour_number: 02
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_02_Log

"""


# ------------------------------------#
DNR2_HOUR_03_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_03
hour_number: 03
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_03_Log

"""


# ------------------------------------#
DNR2_HOUR_04_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_04
hour_number: 04
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_04_Log

"""


# ------------------------------------#
DNR2_HOUR_05_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_05
hour_number: 05
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_05_Log

"""


# ------------------------------------#
DNR2_HOUR_06_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_06
hour_number: 06
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_06_Log

"""


# ------------------------------------#
DNR2_HOUR_07_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_07
hour_number: 07
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_07_Log

"""


# ------------------------------------#
DNR2_HOUR_08_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_08
hour_number: 08
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_08_Log

"""


# ------------------------------------#
DNR2_HOUR_09_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_09
hour_number: 09
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_09_Log

"""


# ------------------------------------#
DNR2_HOUR_10_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_10
hour_number: 10
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_10_Log

"""


# ------------------------------------#
DNR2_HOUR_11_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_11
hour_number: 11
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_11_Log

"""


# ------------------------------------#
DNR2_HOUR_12_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_12
hour_number: 12
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_12_Log

"""


# ------------------------------------#
DNR2_HOUR_13_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_13
hour_number: 13
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_13_Log

"""


# ------------------------------------#
DNR2_HOUR_14_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_14
hour_number: 14
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_14_Log

"""


# ------------------------------------#
DNR2_HOUR_15_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_15
hour_number: 15
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_15_Log

"""


# ------------------------------------#
DNR2_HOUR_16_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_16
hour_number: 16
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_16_Log

"""


# ------------------------------------#
DNR2_HOUR_17_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_17
hour_number: 17
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_17_Log

"""


# ------------------------------------#
DNR2_HOUR_18_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_18
hour_number: 18
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_18_Log

"""


# ------------------------------------#
DNR2_HOUR_19_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour-19
hour_number: 19
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_19_Log

"""


# ------------------------------------#
DNR2_HOUR_20_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_20
hour_number: 20
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_20_Log

"""


# ------------------------------------#
DNR2_HOUR_21_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_21
hour_number: 21
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_21_Log

"""


# ------------------------------------#
DNR2_HOUR_22_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_22
hour_number: 22
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_22_Log

"""


# ------------------------------------#
DNR2_HOUR_23_FILE_CONTENT_CREATION = """---
date: {Today}
tags: daily_note/{Today}/Routine/Hour_23
hour_number: 23
pomodora_task_01: [[{Today}_Routine_Pomodora_Task_01|Pomodora_Task_1]]
pomodora_task_02: [[{Today}_Routine_Pomodora_Task_02|Pomodora_Task_2]]
---


# Hour_23_Log

"""
