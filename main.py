# importing modules and functions.  
import click 
import os
from dotenv import load_dotenv

# Calling all the default functions
load_dotenv()

# Default Variables 
Second_Brain_Dir= os.getenv("Second_Brain_Directory")


@click.command()
def home_screen():
    ''' 
    Second Brain Tools is a toolset made to interact with Second-Brain through command line
    '''

    return 