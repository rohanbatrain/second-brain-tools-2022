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
* [[{Today}_routine|routine]]
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
