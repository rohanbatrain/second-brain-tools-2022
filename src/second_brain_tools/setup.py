# Importing production modules // Meant for production branch
import os
import sys
from git.repo.base import Repo
# Importing production modules finished


# Default variable assignation started.
DEFAULT_GIT_URL = "https://github.com/rohanbatrain/Second-Brain"
NO_VAULT = f"""A Second Brain Vault is required in order to run this script
\n You can get a copy from : {DEFAULT_GIT_URL}"""
# Default variable assignation completed


# Default Warnings assignation started
Warning_WAP = "Wrong argument passed"
Warning_EOF = "Nothing to do, Exiting..."
# Default Warnings assignation finished

# Default Message assignation Started
Msg_dir_clone_prompt = "Please enter the directory, where you want to clone the vault: "
# Default Message assignation finished


def setup():
    """
    A setup wizard to configure second_brain_tools
    """
    check = os.path.isfile(".sbt_config")

    if check is True:
        setup_true()

    elif check is False:
        setup_false()


def setup_true():
    print("File already exist,Do you want to overwrite?")
    choice = input("Enter your choice, Y/N : ")
    if choice == "Y":
        os.remove(".sbt_config")
        setup_false()

    elif choice == "N":
        print(Warning_EOF)
        sys.exit()

    else:
        print(Warning_WAP)
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
            choice_3 = input("Y/N :")
            if choice_3 == "Y":
                print("Sure, Getting things ready.")
                user_git_repo = input("Please enter your github vault url: ")
                git_repo_clone(user_git_repo)
            elif choice_3 == "N":
                print(NO_VAULT)

        elif choice_2 == "N":
            print("Would you like to fetch it from our github repo?")
            choice_3 = input("Y/N :")
            if choice_3 == "Y":
                print("Sure, Getting things ready.")
                git_repo_clone(DEFAULT_GIT_URL)
            elif choice_3 == "N":
                print(NO_VAULT)
    else:
        print(Warning_WAP)
        sys.exit()


def git_repo_clone(git_url):
    second_brain_dir = input(Msg_dir_clone_prompt)
    Repo.clone_from(git_url, second_brain_dir)
    sbt_config_generation(second_brain_dir)


def config():
    """
    Generates a config file named .sbt_config and appends the parameters as per user input.
    """
    print("Config file is missing/removed. \n generating one now.. \n ")
    second_brain_dir = input("Please enter your Vault dir.: ")
    sbt_config_generation(second_brain_dir)


def sbt_config_generation(second_brain_dir):
    with open('.sbt_config', 'a') as dot_env:
        dot_env.write("# ic_custom_regex_started \n")
        dot_env.write(" \n")
        dot_env.write("# ic_custom_regex_ended \n")
        dot_env.write("Second_Brain_Directory = " + "\"" + second_brain_dir + "\"")
