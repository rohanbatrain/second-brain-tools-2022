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
    with open('.sbt_config', 'a+') as dot_env:
        dot_env.write("######## Default Variables Assignation Started \n")
        dot_env.write("DIR_NOT_FOUND = \"Wrong argument passed, the dir code you specified doesn't exist\"\n")
        dot_env.write("FILE_ALREADY_EXIST = \"Error, File already exist\"\n")
        dot_env.write("SECOND_BRAIN_DIRECTORY = " + "\"" + second_brain_dir + "\"\n")
        dot_env.write("######## Default Variables Assignation Finished\n\n")
        dot_env.write("######## Append Options Started \n\n")
        dot_env.write("# Include Time, Supported options True/False \n\n")
        dot_env.write("# Include Time at the end of bullet, numeric list?\n\n")
        dot_env.write("LIST_TIME_INCLUDE = \n\n")
        dot_env.write("# Include Time at the start of Plain Text?\n\n")
        dot_env.write("PLAIN_TEXT_TIME_INCLUDE = \n\n")
        dot_env.write("# What Text to append in before/after the content? ")
        dot_env.write("Please don't leave spaces at the end of the string below, ")
        dot_env.write("Time would be automatically added at the end of the line below with two spaces.\n\n")
        dot_env.write("TIME_APPEND_TEXT = This log was added at ->\n\n")
        dot_env.write("# Append Type Supported Options are \n\n")
        dot_env.write("# -> Paragraph\n")
        dot_env.write("# -> Plain_Text\n")
        dot_env.write("# -> Bullet_List\n")
        dot_env.write("# -> Table\n\n")
        dot_env.write("# Set a global default to append functions. If a type is not passed explicitely in the function then this variable would be invoked.\n")  # noqa: E501
        dot_env.write("GLOBAL_APPEND_TYPE = Table\n\n")
        dot_env.write("# For Daily Notes \n")
        dot_env.write("DNM_APPEND_TYPE = \n")
        dot_env.write("DNBJ_APPEND_TYPE = \n")
        dot_env.write("DNC_APPEND_TYPE = \n")
        dot_env.write("DNE_APPEND_TYPE = \n")
        dot_env.write("DNL_APPEND_TYPE = \n")
        dot_env.write("DNR_APPEND_TYPE = \n")
        dot_env.write("DNR2_APPEND_TYPE = \n")
        dot_env.write("DNT_APPEND_TYPE = \n")
        dot_env.write("DNT2_APPEND_TYPE = \n")
        dot_env.write("DNTE_APPEND_TYPE = \n")
        dot_env.write("DNTT_APPEND_TYPE = \n")
        dot_env.write("DNTL_APPEND_TYPE = \n")
        dot_env.write("DNTM_APPEND_TYPE = \n")
        dot_env.write("DNTM2_APPEND_TYPE = \n")
        dot_env.write("DNTM3_APPEND_TYPE = \n")
        dot_env.write("DNTS_APPEND_TYPE = \n")
        dot_env.write("DNTS2_APPEND_TYPE = \n")
        dot_env.write("DNTW_APPEND_TYPE = \n\n")
        dot_env.write("######## Append Options Finished \n\n")
        dot_env.write("######## Default Example Directories Defining Started #######\n")
        dot_env.write("example = \"This/is/an/example/\"\n")
        dot_env.write("example_elif = \"This/is/an/example/\"\n")
        dot_env.write("######## Default Example Directories Defining Finished #######\n\n")
        dot_env.write("######## Default Directories Defining Started #######\n")
        dot_env.write("_01 = \"01_Capture-System/\"\n")
        dot_env.write("_02 = \"02_Production-System/\"\n")
        dot_env.write("_03 = \"03_Knowledge-Base/\"\n")
        dot_env.write("_04 = \"04_Evergreen/\"\n")
        dot_env.write("_05 = \"05_Projects/\"\n")
        dot_env.write("_06 = \"06_Personal/\"\n")
        dot_env.write("_07 = \"07_Attachments-and-Templates/\"\n")
        dot_env.write("_08 = \"08_Archive/\"\n")
        dot_env.write("_01A = \"01_Capture-System/01A_Inbox/\"\n")
        dot_env.write("_01B = \"01_Capture-System/01B_Processed/\"\n")
        dot_env.write("_01B1 = \"01_Capture-System/01B_Processed/01B1_Completed_Tasks/\"\n")
        dot_env.write("_01B2 = \"01_Capture-System/01B_Processed/01B2_Completed-Routine-Tasks/\"\n")
        dot_env.write("_01B3 = \"01_Capture-System/01B_Processed/01B3_Lists/\"\n")
        dot_env.write("_01C = \"01_Capture-System/01C_Periodic-Notes/\"\n")
        dot_env.write("_01A1 = \"01_Capture-System/01A_Inbox/01A1_Quick-Capture/\"\n")
        dot_env.write("_01A2 = \"01_Capture-System/01A_Inbox/01A2_Link-Capture/\"\n")
        dot_env.write("_01A3 = \"01_Capture-System/01A_Inbox/01A3_Thought-Capture/\"\n")
        dot_env.write("_01A4 = \"01_Capture-System/01A_Inbox/01A4_API-Capture/\"\n")
        dot_env.write("_01A5 = \"01_Capture-System/01A_Inbox/01A5_Shared-Vaults/\"\n")
        dot_env.write("_01A6 = \"01_Capture-System/01A_Inbox/01A6_Tasks/\"\n")
        dot_env.write("_01A7 = \"01_Capture-System/01A_Inbox/01A7_Log-Capture/\"\n")
        dot_env.write("_01A8 = \"01_Capture-System/01A_Inbox/01A8_Recommendation_Capture/\"\n")
        dot_env.write("_01A9 = \"01_Capture-System/01A_Inbox/01A9_Routine_Tasks/\"\n")
        dot_env.write("_01A10 = \"01_Capture-System/01A_Inbox/01A10_Reminders/\"\n")
        dot_env.write("_01A2A = \"01_Capture-System/01A_Inbox/01A2_Link-Capture/01A2A_Social-Networking/\"\n")
        dot_env.write("_01A2B = \"01_Capture-System/01A_Inbox/01A2_Link-Capture/01A2B_Professional-Networking/\"\n")
        dot_env.write("_01A2A1 = \"01_Capture-System/01A_Inbox/01A2_Link-Capture/01A2A_Social-Networking/01A2A1_Reddit/\"\n")
        dot_env.write("_01A2B1 = \"01_Capture-System/01A_Inbox/01A2_Link-Capture/01A2B_Professional-Networking/01A2B1_LinkedIn/\"\n")
        dot_env.write("_01A8A = \"01_Capture-System/01A_Inbox/01A8_Recommendation_Capture/01A8A_Books/\"\n")
        dot_env.write("_01A8B = \"01_Capture-System/01A_Inbox/01A8_Recommendation_Capture/01A8B_Movies/\"\n")
        dot_env.write("_01A8C = \"01_Capture-System/01A_Inbox/01A8_Recommendation_Capture/01A8C_Music/\"\n")
        dot_env.write("_01A8D = \"01_Capture-System/01A_Inbox/01A8_Recommendation_Capture/01A8D_Web-Series/\"\n")
        dot_env.write("_01B = \"01_Capture-System/01B_Processed/\"\n")
        dot_env.write("_01C = \"01_Capture-System/01C_Periodic-Notes/\"\n")
        dot_env.write("_01B3A = \"01_Capture-System/01B_Processed/01B3_Lists/01B3A_Playlists/\"\n")
        dot_env.write("_01B3B = \"01_Capture-System/01B_Processed/01B3_Lists/01B3B_Wishlists/\"\n")
        dot_env.write("_01C1 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/\"\n")
        dot_env.write("_01C1A = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1A_MOC/\"\n")
        dot_env.write("_01C1B = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1B_Bullet-Journal/\"\n")
        dot_env.write("_01C1B1 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1B_Journal/01C1B1_Bullet-Journal\"\n")
        dot_env.write("_01C1C = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1C_Connections/\"\n")
        dot_env.write("_01C1D = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1D_Events/\"\n")
        dot_env.write("_01C1E = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1E_Location/\"\n")
        # should use location yaml in one main location file instead of this -> dot_env.write("_01C1E1 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1E_Location/01C1E1_Morning/\"\n")  # noqa: E501
        # should use location yaml in one main location file instead of this -> dot_env.write("_01C1E2 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1E_Location/01C1E2_Noon/\"\n")  # noqa: E501
        # should use location yaml in one main location file instead of this -> dot_env.write("_01C1E3 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1E_Location/01C1E3_Evening/\"\n")  # noqa: E501
        # should use location yaml in one main location file instead of this -> dot_env.write("_01C1E4 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1E_Location/01C1E4_Night/\"\n")  # noqa: E501
        dot_env.write("_01C1F = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1F_Reminders/\"\n")
        dot_env.write("_01C1G = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1G_routine/\"\n")
        dot_env.write("_01C1H = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1H_Tasks/\"\n")
        dot_env.write("_01C1I = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1I_Trackers/\"\n")
        dot_env.write("_01C1I1 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1I_Trackers/01C1I1_Transaction/\"\n")
        dot_env.write("_01C1I2 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1I_Trackers/01C1I2_Sleep/\"\n")
        dot_env.write("_01C1I3 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1I_Trackers/01C1I3_Meal/\"\n")
        dot_env.write("_01C1I4 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1I_Trackers/01C1I4_Medicine/\"\n")
        dot_env.write("_01C1I5 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1I_Trackers/01C1I5_Mood/\"\n")
        dot_env.write("_01C1I6 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1I_Trackers/01C1I6_Water/\"\n")
        dot_env.write("_01C1I7 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1I_Trackers/01C1I7_Exercise/\"\n")
        dot_env.write("_01C1I8 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1I_Trackers/01C1I8_Symptoms/\"\n")
        dot_env.write("_01C1I9 = \"01_Capture-System/01C_Periodic-Notes/01C1_Daily_Note/01C1I_Trackers/01C1I9_Location/\"\n")
        dot_env.write("_02A = \"02_Production-System/02A_Youtube/\"\n")
        dot_env.write("_02B = \"02_Production-System/02B_Medium/\"\n")
        dot_env.write("_02A1 = \"02_Production-System/02A_Youtube/02A1_Videos/\"\n")
        dot_env.write("_02A2 = \"02_Production-System/02A_Youtube/02A2_Shorts/\"\n")
        dot_env.write("_02A3 = \"02_Production-System/02A_Youtube/02A3_Stories/\"\n")
        dot_env.write("_02B1 = \"02_Production-System/02B_Medium/02B1_Articles/\"\n")
        dot_env.write("_03A = \"03_Knowledge-Base/03A_Science/\"\n")
        dot_env.write("_03B = \"03_Knowledge-Base/03B_Languages/\"\n")
        dot_env.write("_03C = \"03_Knowledge-Base/03C_IT-Skills/\"\n")
        dot_env.write("_03D = \"03_Knowledge-Base/03D_Theology/\"\n")
        dot_env.write("_03A1 = \"03_Knowledge-Base/03A_Science/03A1_Chemistry/\"\n")
        dot_env.write("_03A2 = \"03_Knowledge-Base/03A_Science/03A2_Computer-Science/\"\n")
        dot_env.write("_03A3 = \"03_Knowledge-Base/03A_Science/03A3_Mathematics/\"\n")
        dot_env.write("_03A4 = \"03_Knowledge-Base/03A_Science/03A4_Physics/\"\n")
        dot_env.write("_03B1 = \"03_Knowledge-Base/03B_Languages/03B1_Hindi/\"\n")
        dot_env.write("_03B2 = \"03_Knowledge-Base/03B_Languages/03B2_English/\"\n")
        dot_env.write("_03B3 = \"03_Knowledge-Base/03B_Languages/03B3_Sanskrit/\"\n")
        dot_env.write("_03B4 = \"03_Knowledge-Base/03B_Languages/03B4_Japanese/\"\n")
        dot_env.write("_03B5 = \"03_Knowledge-Base/03B_Languages/03B5_Bengali/\"\n")
        dot_env.write("_03B6 = \"03_Knowledge-Base/03B_Languages/03B6_Korean/\"\n")
        dot_env.write("_03B7 = \"03_Knowledge-Base/03B_Languages/03B7_Punjabi/\"\n")
        dot_env.write("_03B8 = \"03_Knowledge-Base/03B_Languages/03B8_Russian/\"\n")
        dot_env.write("_03B9 = \"03_Knowledge-Base/03B_Languages/03B9_French/\"\n")
        dot_env.write("_03B10 = \"03_Knowledge-Base/03B_Languages/03B10_Spanish/\"\n")
        dot_env.write("_03B11 = \"03_Knowledge-Base/03B_Languages/03B11_Urdu/\"\n")
        dot_env.write("_03C1 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/\"\n")
        dot_env.write("_03C2 = \"03_Knowledge-Base/03C_IT-Skills/03C2_Machine-Learning/\"\n")
        dot_env.write("_03C3 = \"03_Knowledge-Base/03C_IT-Skills/03C3_Software/\"\n")
        dot_env.write("_03C4 = \"03_Knowledge-Base/03C_IT-Skills/03C4_System-Administration/\"\n")
        dot_env.write("_03C1A = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/\"\n")
        dot_env.write("_03C1B = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1B_Programming-Projects/\"\n")
        dot_env.write("_03C1C = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1C_Query-Languages/\"\n")
        dot_env.write("_03C1A1 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A1_Bash/\"\n")
        dot_env.write("_03C1A2 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A2_Python/\"\n")
        dot_env.write("_03C1A3 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A3_C-Lang/\"\n")
        dot_env.write("_03C1A4 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A4_Javascript/\"\n")
        dot_env.write("_03C1A5 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A5_Dart/\"\n")
        dot_env.write("_03C1A6 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A6_Flutter/\"\n")
        dot_env.write("_03C1A7 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A7_C++/\"\n")
        dot_env.write("_03C1A8 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A8_TypeScript/\"\n")
        dot_env.write("_03C1A9 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A9_Java/\"\n")
        dot_env.write("_03C1A10 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A10_C-Sharp/\"\n")
        dot_env.write("_03C1A11 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A11_PHP/\"\n")
        dot_env.write("_03C1A12 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A12_Groovy/\"\n")
        dot_env.write("_03C1A13 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A13_Ruby/\"\n")
        dot_env.write("_03C1A14 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A14_Rust/\"\n")
        dot_env.write("_03C1A15 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A15_Kotlin/\"\n")
        dot_env.write("_03C1A16 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A16_Golang/\"\n")
        dot_env.write("_03C1A17 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A17_Perl/\"\n")
        dot_env.write("_03C1A18 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A18_Visual-Basic-Dot-Net/\"\n")  # noqa: E501
        dot_env.write("_03C1B1 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1B_Programming-Projects/Project-1/\"\n")
        dot_env.write("_03C1C1 = \"03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1C_Query-Languages/03C1C1_SQL/\"\n")
        dot_env.write("_03C2A = \"03_Knowledge-Base/03C_IT-Skills/03C2_Machine-Learning/03C2A_Reinforcement-Learning/\"\n")
        dot_env.write("_03C2B = \"03_Knowledge-Base/03C_IT-Skills/03C2_Machine-Learning/03C2B_Deep-Learning/\"\n")
        dot_env.write("_03C3A = \"03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/\"\n")
        dot_env.write("_03C3B = \"03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3B_Operating-System/\"\n")
        dot_env.write("_03C3A1 = \"03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/03C3A1__Unreal-Engine/\"\n")
        dot_env.write("_03C3A2 = \"03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/03C3A2__Blender/\"\n")
        dot_env.write("_03C3A3 = \"03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/03C3A3__Unity/\"\n")
        dot_env.write("_03C3A4 = \"03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/03C3A4__MariaDB/\"\n")
        dot_env.write("_03C3B1 = \"03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3B_Operating-System/03C3B1_Linux/\"\n")
        dot_env.write("_03C4A = \"03_Knowledge-Base/03C_IT-Skills/03C4_System-Administration/03C4A_Web-Servers/\"\n")
        dot_env.write("_03D1 = \"03_Knowledge-Base/03D_Theology/03D1_Hinduism/\"\n")
        dot_env.write("_03D2 = \"03_Knowledge-Base/03D_Theology/03D2_Sikhism/\"\n")
        dot_env.write("_03D3 = \"03_Knowledge-Base/03D_Theology/03D3_Buddhism/\"\n")
        dot_env.write("_03D4 = \"03_Knowledge-Base/03D_Theology/03D4_Islam/\"\n")
        dot_env.write("_03D5 = \"03_Knowledge-Base/03D_Theology/03D5_Christianity/\"\n")
        dot_env.write("_04A = \"04_Evergreen/04A_Network/\"\n")
        dot_env.write("_04B = \"04_Evergreen/04B_Events/\"\n")
        dot_env.write("_04C = \"04_Evergreen/04C_Locations/\"\n")
        dot_env.write("_04D = \"04_Evergreen/04D_Bullet-Journal/\"\n")
        dot_env.write("_04A1 = \"04_Evergreen/04A_Network/04A1_Bros/\"\n")
        dot_env.write("_04A2 = \"04_Evergreen/04A_Network/04A2_Class-Room/\"\n")
        dot_env.write("_04A3 = \"04_Evergreen/04A_Network/04A3_Social-Media/\"\n")
        dot_env.write("_04A4 = \"04_Evergreen/04A_Network/04A4_Friends/\"\n")
        dot_env.write("_04A5 = \"04_Evergreen/04A_Network/04A5_Family/\"\n")
        dot_env.write("_04A6 = \"04_Evergreen/04A_Network/04A6_Corporate/\"\n")
        dot_env.write("_04A7 = \"04_Evergreen/04A_Network/04A7_Relatives/\"\n")
        dot_env.write("_04A99 = \"04_Evergreen/04A_Network/04A99_Miscellaneous/\"\n")
        dot_env.write("_04B1 = \"04_Evergreen/04B_Events/04B1_Incidents/\"\n")
        dot_env.write("_04B2 = \"04_Evergreen/04B_Events/04B2_Planned-Events/\"\n")
        dot_env.write("_04C1 = \"04_Evergreen/04C_Locations/04C1_School/\"\n")
        dot_env.write("_05A = \"05_Projects/05A_Brands/\"\n")
        dot_env.write("_05B = \"05_Projects/05B_Startup/\"\n")
        dot_env.write("_05C = \"05_Projects/05C_Business/\"\n")
        dot_env.write("_05D = \"05_Projects/05D_Story-Writing/\"\n")
        dot_env.write("_05E = \"05_Projects/05E_Competitions/\"\n")
        dot_env.write("_06A = \"06_Personal/06A_Brand/\"\n")
        dot_env.write("_06B = \"06_Personal/06B_Projects/\"\n")
        # dot_env.write("_06C = \"06_Personal/06C_Workspace-Log/\"\n")
        # dot_env.write("_06D = \"06_Personal/06D_Recommendation-List/\"\n")
        # dot_env.write("_06E = \"06_Personal/06E_Transaction-Tracking/\"\n")
        dot_env.write("_06A1 = \"06_Personal/06A_Brand/06A1_Brand-1/\"\n")
        dot_env.write("_06B1 = \"06_Personal/06B_Projects/06B1_Home-Lab/\"\n")
        # dot_env.write("_06C1 = \"06_Personal/06C_Workspace-Log/06C1_Laptop-Workspace/\"\n")
        # dot_env.write("_06C2 = \"06_Personal/06C_Workspace-Log/06C2_Web-Presence/\"\n")
        # dot_env.write("_06D1 = \"06_Personal/06D_Recommendation-List/06D1_Movies/\"\n")
        # dot_env.write("_06D2 = \"06_Personal/06D_Recommendation-List/06D2_Music/\"\n")
        # dot_env.write("_06D3 = \"06_Personal/06D_Recommendation-List/06D3_Books/\"\n")
        dot_env.write("_07A = \"07_Attachments-and-Templates/07A_Attachments/\"\n")
        dot_env.write("_07A1 = \"07_Attachments-and-Templates/07A_Attachments/07A1_Memories/\"\n")
        dot_env.write("_07A2 = \"07_Attachments-and-Templates/07A_Attachments/07A2_Shared-Vaults/\"\n")
        dot_env.write("_07B = \"07_Attachments-and-Templates/07B_Templates/\"\n")
        dot_env.write("_07B1 = \"07_Attachments-and-Templates/07B_Templates/07B1_Periodic-Notes/\"\n\n")
        dot_env.write("######## Default Directories Defining Finished ###### \n\n")
