# Importing production modules // Meant for production branch
from second_brain_tools.config import Today
# Importing production modules finished


# Daily Note File Creation Content String Started
DNM_FILE_CONTENT_CREATION = f"""---
tags :
 - daily_note/{Today}
 - {Today}
date : {Today}
---

* [[{Today}_Events|Events]]
* [[{Today}_Connections|Connections]]
* [[{Today}_Tasks|Tasks]]
* [[{Today}_Routines|Routines]]
* [[{Today}_Reminders|Reminders]]
* [[{Today}_Bullet-Journal|Bullet-Journal]]
* [[{Today}_Trackers|Trackers]]

# Log

```
SBT WILL APPEND AFTER THIS CODEBLOCK.
```


"""
# Daily Note File Creation Content String Finished
