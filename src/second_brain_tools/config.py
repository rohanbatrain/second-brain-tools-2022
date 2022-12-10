# Importing production modules // Meant for production branch
import os
from dotenv import load_dotenv
# Importing production modules finished

load_dotenv(".sbt_config")

# Default strings from env import Started
Second_Brain_Directory = os.getenv("Second_Brain_Directory")
# Default strings from env import Finished
