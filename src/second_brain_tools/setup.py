# Importing production modules // Meant for production branch
import os
import sys
# Importing production modules finished


# Default variable assignation started.
GIT_URL = "https://github.com/rohanbatrain/Second-Brain"
NO_VAULT = f"""A Second Brain Vault is required in order to run this script
\n You can get a copy from : {GIT_URL}"""
# Default variable assignation completed


def setup():
    """
    A setup wizard to configure second_brain_tools
    """
    check = os.path.isfile(".env")

    if check is True:
        setup_true()

    elif check is False:
        setup_false()


def setup_true():
    print("File already exist,Do you want to overwrite?")
    choice = input("Enter your choice, Y/N : ")
    if choice == "Y":
        os.remove(".env")
        config()

    elif choice == "N":
        print("Nothing to do, Exiting...")
        sys.exit()


def setup_false():
    print("Do you have vault folder ready locally in your system?")
    choice = input("Y/N: ")
    if choice == "Y":
        config()
    elif choice == "N":
        print("Do you have your vault folder in github?")
        choice_2 = input("Y/N: ")
        if choice_2 == "Y":
            print("Would you like to fetch it from your github?")
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
