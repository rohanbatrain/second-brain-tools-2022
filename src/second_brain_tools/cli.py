"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -m second_brain_tools` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``second_brain_tools.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``second_brain_tools.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""

# Importing modules
import os


# Default Variable
GIT_URL = f"https://github.com/rohanbatrain/Second-Brain"
NO_VAULT= f"""A Second Brain Vault is required in order to run this script
\n You can get a copy from : {GIT_URL}"""

def main():
    """
    """
    #setup()
    return 0

## Starting the module

def setup():
    check=os.path.isfile(".env")
    if check is True:
        print("File already exist,Do you want to overwrite?")
    args1=input("Enter your choice, Y/N : ")
    if args1 == "Y":
        os.remove(".env")
        config()

    elif args1 == "N":
        print ("Nothing to do, Exiting...")
        exit()
    elif check is False:
        print("Do you have vault folder ready locally in your system?")
    choice_1 = input("Y/N: ")
    if choice_1 == "Y":
        config()
    elif choice_1 == "N":
        print("Do you have your vault folder in github?")
        choice_2 = input("Y/N: ")
        if choice_2 =="Y":
            print ("Would you like to fetch it from the github?")
        elif choice_2 =="N":
            print (NO_VAULT)

def config():
    print("Config file is missing/removed. \n generating one now.. \n ")
    SECOND_BRAIN_DIR= input("Please enter your Vault dir: ")
    with open ('.env','w', encoding="UTF.8") as dot_env:
        dot_env.write ("Second_Brain_Directory = " + "\"" + SECOND_BRAIN_DIR + "\"")
