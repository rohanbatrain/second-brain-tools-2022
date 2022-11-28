"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -m second_brain_tools` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``second_brain_tools.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again(as a module) because
    there's no ``second_brain_tools.__main__`` in ``sys.modules``.
"""

# Importing production modules // Meant for production branch
import os
import sys
import typer
# Importing production modules finished


# Importing testing modules started // Meant for testing branch
# from second_brain_tools.dir import initial_check
# # Importing testing modules finished


# Default variable assignation started.
GIT_URL = "https://github.com/rohanbatrain/Second-Brain"
NO_VAULT = f"""A Second Brain Vault is required in order to run this script
\n You can get a copy from : {GIT_URL}"""
# Default variable assignation completed


# Main function, which calls typer app here


def main():
    """
    Main Function, aka CLI app.
    """
    app()
    return 0


# Typer app Started

app = app = typer.Typer()

# Typer app Finished

# Starting the module


@app.command()
def setup():
    """
    A setup wizard to configure second_brain_tools
    """
    check = os.path.isfile(".env")
    if check is True:
        print("File already exist,Do you want to overwrite?")
        args1 = input("Enter your choice, Y/N : ")
        if args1 == "Y":
            os.remove(".env")
            config()

    elif args1 == "N":
        print("Nothing to do, Exiting...")
        sys.exit()

    elif check is False:
        print("Do you have vault folder ready locally in your system?")
        choice_1 = input("Y/N: ")
        if choice_1 == "Y":
            config()
        elif choice_1 == "N":
            print("Do you have your vault folder in github?")
            choice_2 = input("Y/N: ")
            if choice_2 == "Y":
                print("Would you like to fetch it from the github?")
            elif choice_2 == "N":
                print("Would you like to fetch it from our github repo?")
                choice_3 = input("Y/N :")
                if choice_3 == "Y":
                    print("Sure,Getting things ready.")
                elif choice_3 == "N":
                    print(NO_VAULT)


def config():
    """
    Generates a config file named .env and appends the parameters as per user input.
    """
    print("Config file is missing/removed. \n generating one now.. \n ")
    second_brain_dir = input("Please enter your Vault dir: ")
    with open('.env', 'w', encoding="UTF.8") as dot_env:
        dot_env.write("Second_Brain_Directory = " + "\"" + second_brain_dir + "\"")
