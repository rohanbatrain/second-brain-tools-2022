from second_brain_tools.dir import initial_check
from second_brain_tools.dir import DIR_NOT_FOUND

# Defining default variables
DNT = DIR_NOT_FOUND
lorem_ipsum = "3122323-somelongrandomloremipsum"

# dir.py Started

# Initial Check Started

# Checking that Existing Directories are returned with correct code. <Started>


def test_01_initial_check():
    dir_code = "01"
    dir_path = "01_Capture-System/"
    assert initial_check(dir_code) == dir_path


def test_01A_initial_check():
    dir_code = "01A"
    dir_path = "01_Capture-System/01A_Inbox/"
    assert initial_check(dir_code) == dir_path


def test_01A1_initial_check():
    dir_code = "01A1"
    dir_path = "01_Capture-System/01A_Inbox/01A1_Quick-Capture/"
    assert initial_check(dir_code) == dir_path


def test_01A2_initial_check():
    dir_code = "01A2"
    dir_path = "01_Capture-System/01A_Inbox/01A2_Link-Capture/"
    assert initial_check(dir_code) == dir_path


def test_01A2A_initial_check():
    dir_code = "01A2A"
    dir_path = "01_Capture-System/01A_Inbox/01A2_Link-Capture/01A2A_Social-Networking/"
    assert initial_check(dir_code) == dir_path


def test_01A2A1_initial_check():
    dir_code = "01A2A1"
    dir_path = "01_Capture-System/01A_Inbox/01A2_Link-Capture/01A2A_Social-Networking/01A2A1_Reddit/"
    assert initial_check(dir_code) == dir_path


def test_01A2B_initial_check():
    dir_code = "01A2B"
    dir_path = "01_Capture-System/01A_Inbox/01A2_Link-Capture/01A2B_Professional-Networking/"
    assert initial_check(dir_code) == dir_path


def test_01A2B1_initial_check():
    dir_code = "01A2B1"
    dir_path = "01_Capture-System/01A_Inbox/01A2_Link-Capture/01A2B_Professional-Networking/01A2B1_LinkedIn/"
    assert initial_check(dir_code) == dir_path


def test_01A3_initial_check():
    dir_code = "01A3"
    dir_path = "01_Capture-System/01A_Inbox/01A3_Thought-Capture/"
    assert initial_check(dir_code) == dir_path


def test_01A4_initial_check():
    dir_code = "01A4"
    dir_path = "01_Capture-System/01A_Inbox/01A4_API-Capture/"
    assert initial_check(dir_code) == dir_path


def test_01B_initial_check():
    dir_code = "01B"
    dir_path = "01_Capture-System/01B_Processed/"
    assert initial_check(dir_code) == dir_path


def test_01C_initial_check():
    dir_code = "01C"
    dir_path = "01_Capture-System/01C_Periodic-Notes/"
    assert initial_check(dir_code) == dir_path


def test_01C1_initial_check():
    dir_code = "01C1"
    dir_path = "01_Capture-System/01C_Periodic-Notes/01C1_Reminders/"
    assert initial_check(dir_code) == dir_path


def test_02_initial_check():
    dir_code = "02"
    dir_path = "02_Production-System/"
    assert initial_check(dir_code) == dir_path


def test_02A_initial_check():
    dir_code = "02A"
    dir_path = "02_Production-System/02A_Youtube/"
    assert initial_check(dir_code) == dir_path


def test_02A1_initial_check():
    dir_code = "02A1"
    dir_path = "02_Production-System/02A_Youtube/02A1_Videos/"
    assert initial_check(dir_code) == dir_path


def test_02A2_initial_check():
    dir_code = "02A2"
    dir_path = "02_Production-System/02A_Youtube/02A2_Shorts/"
    assert initial_check(dir_code) == dir_path


def test_02A3_initial_check():
    dir_code = "02A3"
    dir_path = "02_Production-System/02A_Youtube/02A3_Stories/"
    assert initial_check(dir_code) == dir_path


def test_02B_initial_check():
    dir_code = "02B"
    dir_path = "02_Production-System/02B_Medium/"
    assert initial_check(dir_code) == dir_path


def test_02B1_initial_check():
    dir_code = "02B1"
    dir_path = "02_Production-System/02B_Medium/02B1_Articles/"
    assert initial_check(dir_code) == dir_path


def test_03_initial_check():
    dir_code = "03"
    dir_path = "03_Knowledge-Base/"
    assert initial_check(dir_code) == dir_path


def test_03A_initial_check():
    dir_code = "03A"
    dir_path = "03_Knowledge-Base/03A_Science/"
    assert initial_check(dir_code) == dir_path


def test_03A1_initial_check():
    dir_code = "03A1"
    dir_path = "03_Knowledge-Base/03A_Science/03A1_Chemistry/"
    assert initial_check(dir_code) == dir_path


def test_03A2_initial_check():
    dir_code = "03A2"
    dir_path = "03_Knowledge-Base/03A_Science/03A2_Computer-Science/"
    assert initial_check(dir_code) == dir_path


def test_03A3_initial_check():
    dir_code = "03A3"
    dir_path = "03_Knowledge-Base/03A_Science/03A3_Mathematics/"
    assert initial_check(dir_code) == dir_path


def test_03A4_initial_check():
    dir_code = "03A4"
    dir_path = "03_Knowledge-Base/03A_Science/03A4_Physics/"
    assert initial_check(dir_code) == dir_path


def test_03B_initial_check():
    dir_code = "03B"
    dir_path = "03_Knowledge-Base/03B_Languages/"
    assert initial_check(dir_code) == dir_path


def test_03B1_initial_check():
    dir_code = "03B1"
    dir_path = "03_Knowledge-Base/03B_Languages/03B1_Hindi/"
    assert initial_check(dir_code) == dir_path


def test_03B10_initial_check():
    dir_code = "03B10"
    dir_path = "03_Knowledge-Base/03B_Languages/03B10_Spanish/"
    assert initial_check(dir_code) == dir_path


def test_03B2_initial_check():
    dir_code = "03B2"
    dir_path = "03_Knowledge-Base/03B_Languages/03B2_English/"
    assert initial_check(dir_code) == dir_path


def test_03B3_initial_check():
    dir_code = "03B3"
    dir_path = "03_Knowledge-Base/03B_Languages/03B3_Sanskrit/"
    assert initial_check(dir_code) == dir_path


def test_03B4_initial_check():
    dir_code = "03B4"
    dir_path = "03_Knowledge-Base/03B_Languages/03B4_Japanese/"
    assert initial_check(dir_code) == dir_path


def test_03B5_initial_check():
    dir_code = "03B5"
    dir_path = "03_Knowledge-Base/03B_Languages/03B5_Bengali/"
    assert initial_check(dir_code) == dir_path


def test_03B6_initial_check():
    dir_code = "03B6"
    dir_path = "03_Knowledge-Base/03B_Languages/03B6_Korean/"
    assert initial_check(dir_code) == dir_path


def test_03B7_initial_check():
    dir_code = "03B7"
    dir_path = "03_Knowledge-Base/03B_Languages/03B7_Punjabi/"
    assert initial_check(dir_code) == dir_path


def test_03B8_initial_check():
    dir_code = "03B8"
    dir_path = "03_Knowledge-Base/03B_Languages/03B8_Russian/"
    assert initial_check(dir_code) == dir_path


def test_03B9_initial_check():
    dir_code = "03B9"
    dir_path = "03_Knowledge-Base/03B_Languages/03B9_French/"
    assert initial_check(dir_code) == dir_path


def test_03C_initial_check():
    dir_code = "03C"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/"
    assert initial_check(dir_code) == dir_path


def test_03C1_initial_check():
    dir_code = "03C1"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/"
    assert initial_check(dir_code) == dir_path


def test_03C1A_initial_check():
    dir_code = "03C1A"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/"
    assert initial_check(dir_code) == dir_path


def test_03C1A1_initial_check():
    dir_code = "03C1A1"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A1_Bash/"
    assert initial_check(dir_code) == dir_path


def test_03C1A10_initial_check():
    dir_code = "03C1A10"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A10_C-Sharp/"
    assert initial_check(dir_code) == dir_path


def test_03C1A11_initial_check():
    dir_code = "03C1A11"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A11_PHP/"
    assert initial_check(dir_code) == dir_path


def test_03C1A12_initial_check():
    dir_code = "03C1A12"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A12_Groovy/"
    assert initial_check(dir_code) == dir_path


def test_03C1A13_initial_check():
    dir_code = "03C1A13"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A13_Ruby/"
    assert initial_check(dir_code) == dir_path


def test_03C1A14_initial_check():
    dir_code = "03C1A14"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A14_Rust/"
    assert initial_check(dir_code) == dir_path


def test_03C1A15_initial_check():
    dir_code = "03C1A15"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A15_Kotlin/"
    assert initial_check(dir_code) == dir_path


def test_03C1A16_initial_check():
    dir_code = "03C1A16"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A16_Golang/"
    assert initial_check(dir_code) == dir_path


def test_03C1A17_initial_check():
    dir_code = "03C1A17"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A17_Perl/"
    assert initial_check(dir_code) == dir_path


def test_03C1A18_initial_check():
    dir_code = "03C1A18"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A18_Visual-Basic-Dot-Net/"
    assert initial_check(dir_code) == dir_path


def test_03C1A2_initial_check():
    dir_code = "03C1A2"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A2_Python/"
    assert initial_check(dir_code) == dir_path


def test_03C1A3_initial_check():
    dir_code = "03C1A3"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A3_C-Lang/"
    assert initial_check(dir_code) == dir_path


def test_03C1A4_initial_check():
    dir_code = "03C1A4"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A4_Javascript/"
    assert initial_check(dir_code) == dir_path


def test_03C1A5_initial_check():
    dir_code = "03C1A5"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A5_Dart/"
    assert initial_check(dir_code) == dir_path


def test_03C1A6_initial_check():
    dir_code = "03C1A6"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A6_Flutter/"
    assert initial_check(dir_code) == dir_path


def test_03C1A7_initial_check():
    dir_code = "03C1A7"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A7_C++/"
    assert initial_check(dir_code) == dir_path


def test_03C1A8_initial_check():
    dir_code = "03C1A8"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A8_TypeScript/"
    assert initial_check(dir_code) == dir_path


def test_03C1A9_initial_check():
    dir_code = "03C1A9"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1A_Programming-Languages/03C1A9_Java/"
    assert initial_check(dir_code) == dir_path


def test_03C1B_initial_check():
    dir_code = "03C1B"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1B_Programming-Projects/"
    assert initial_check(dir_code) == dir_path


def test_03C1B1_initial_check():
    dir_code = "03C1B1"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1B_Programming-Projects/Project-1/"
    assert initial_check(dir_code) == dir_path


def test_03C1C_initial_check():
    dir_code = "03C1C"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1C_Query-Languages/"
    assert initial_check(dir_code) == dir_path


def test_03C1C1_initial_check():
    dir_code = "03C1C1"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C1_Programming/03C1C_Query-Languages/03C1C1_SQL/"
    assert initial_check(dir_code) == dir_path


def test_03C2_initial_check():
    dir_code = "03C2"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C2_Machine-Learning/"
    assert initial_check(dir_code) == dir_path


def test_03C2A_initial_check():
    dir_code = "03C2A"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C2_Machine-Learning/03C2A_Reinforcement-Learning/"
    assert initial_check(dir_code) == dir_path


def test_03C2B_initial_check():
    dir_code = "03C2B"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C2_Machine-Learning/03C2B_Deep-Learning/"
    assert initial_check(dir_code) == dir_path


def test_03C3_initial_check():
    dir_code = "03C3"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/"
    assert initial_check(dir_code) == dir_path


def test_03C3A_initial_check():
    dir_code = "03C3A"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/"
    assert initial_check(dir_code) == dir_path


def test_03C3A1_initial_check():
    dir_code = "03C3A1"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/03C3A1__Unreal-Engine/"
    assert initial_check(dir_code) == dir_path


def test_03C3A2_initial_check():
    dir_code = "03C3A2"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/03C3A2__Blender/"
    assert initial_check(dir_code) == dir_path


def test_03C3A3_initial_check():
    dir_code = "03C3A3"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/03C3A3__Unity/"
    assert initial_check(dir_code) == dir_path


def test_03C3A4_initial_check():
    dir_code = "03C3A4"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3A_Application/03C3A4__MariaDB/"
    assert initial_check(dir_code) == dir_path


def test_03C3B_initial_check():
    dir_code = "03C3B"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3B_Operating-System/"
    assert initial_check(dir_code) == dir_path


def test_03C3B1_initial_check():
    dir_code = "03C3B1"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C3_Software/03C3B_Operating-System/03C3B1_Linux/"
    assert initial_check(dir_code) == dir_path


def test_03C4_initial_check():
    dir_code = "03C4"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C4_System-Administration/"
    assert initial_check(dir_code) == dir_path


def test_03C4A_initial_check():
    dir_code = "03C4A"
    dir_path = "03_Knowledge-Base/03C_IT-Skills/03C4_System-Administration/03C4A_Web-Servers/"
    assert initial_check(dir_code) == dir_path


def test_03D_initial_check():
    dir_code = "03D"
    dir_path = "03_Knowledge-Base/03D_Theology/"
    assert initial_check(dir_code) == dir_path


def test_03D1_initial_check():
    dir_code = "03D1"
    dir_path = "03_Knowledge-Base/03D_Theology/03D1_Hinduism/"
    assert initial_check(dir_code) == dir_path


def test_03D2_initial_check():
    dir_code = "03D2"
    dir_path = "03_Knowledge-Base/03D_Theology/03D2_Sikhism/"
    assert initial_check(dir_code) == dir_path


def test_03D3_initial_check():
    dir_code = "03D3"
    dir_path = "03_Knowledge-Base/03D_Theology/03D3_Buddhism/"
    assert initial_check(dir_code) == dir_path


def test_03D4_initial_check():
    dir_code = "03D4"
    dir_path = "03_Knowledge-Base/03D_Theology/03D4_Islam/"
    assert initial_check(dir_code) == dir_path


def test_03D5_initial_check():
    dir_code = "03D5"
    dir_path = "03_Knowledge-Base/03D_Theology/03D5_Christianity/"
    assert initial_check(dir_code) == dir_path


def test_04_initial_check():
    dir_code = "04"
    dir_path = "04_Evergreen/"
    assert initial_check(dir_code) == dir_path


def test_04A_initial_check():
    dir_code = "04A"
    dir_path = "04_Evergreen/04A_Network/"
    assert initial_check(dir_code) == dir_path


def test_04A1_initial_check():
    dir_code = "04A1"
    dir_path = "04_Evergreen/04A_Network/04A1_Bros/"
    assert initial_check(dir_code) == dir_path


def test_04A2_initial_check():
    dir_code = "04A2"
    dir_path = "04_Evergreen/04A_Network/04A2_Class-Room/"
    assert initial_check(dir_code) == dir_path


def test_04A3_initial_check():
    dir_code = "04A3"
    dir_path = "04_Evergreen/04A_Network/04A3_Social-Media/"
    assert initial_check(dir_code) == dir_path


def test_04A4_initial_check():
    dir_code = "04A4"
    dir_path = "04_Evergreen/04A_Network/04A4_Friends/"
    assert initial_check(dir_code) == dir_path


def test_04A5_initial_check():
    dir_code = "04A5"
    dir_path = "04_Evergreen/04A_Network/04A5_Family/"
    assert initial_check(dir_code) == dir_path


def test_04A6_initial_check():
    dir_code = "04A6"
    dir_path = "04_Evergreen/04A_Network/04A6_Corporate/"
    assert initial_check(dir_code) == dir_path


def test_04A7_initial_check():
    dir_code = "04A7"
    dir_path = "04_Evergreen/04A_Network/04A7_Relatives/"
    assert initial_check(dir_code) == dir_path


def test_04A99_initial_check():
    dir_code = "04A99"
    dir_path = "04_Evergreen/04A_Network/04A99_Miscellaneous/"
    assert initial_check(dir_code) == dir_path


def test_04B_initial_check():
    dir_code = "04B"
    dir_path = "04_Evergreen/04B_Events/"
    assert initial_check(dir_code) == dir_path


def test_04B1_initial_check():
    dir_code = "04B1"
    dir_path = "04_Evergreen/04B_Events/04B1_Incidents/"
    assert initial_check(dir_code) == dir_path


def test_04B2_initial_check():
    dir_code = "04B2"
    dir_path = "04_Evergreen/04B_Events/04B2_Planned-Events/"
    assert initial_check(dir_code) == dir_path


def test_04C_initial_check():
    dir_code = "04C"
    dir_path = "04_Evergreen/04C_Locations/"
    assert initial_check(dir_code) == dir_path


def test_04C1_initial_check():
    dir_code = "04C1"
    dir_path = "04_Evergreen/04C_Locations/04C1_School/"
    assert initial_check(dir_code) == dir_path


def test_05_initial_check():
    dir_code = "05"
    dir_path = "05_Projects/"
    assert initial_check(dir_code) == dir_path


def test_05A_initial_check():
    dir_code = "05A"
    dir_path = "05_Projects/05A_Brands/"
    assert initial_check(dir_code) == dir_path


def test_05B_initial_check():
    dir_code = "05B"
    dir_path = "05_Projects/05B_Startup/"
    assert initial_check(dir_code) == dir_path


def test_05C_initial_check():
    dir_code = "05C"
    dir_path = "05_Projects/05C_Business/"
    assert initial_check(dir_code) == dir_path


def test_05D_initial_check():
    dir_code = "05D"
    dir_path = "05_Projects/05D_Story-Writing/"
    assert initial_check(dir_code) == dir_path


def test_05E_initial_check():
    dir_code = "05E"
    dir_path = "05_Projects/05E_Competitions/"
    assert initial_check(dir_code) == dir_path


def test_06_initial_check():
    dir_code = "06"
    dir_path = "06_Personal/"
    assert initial_check(dir_code) == dir_path


def test_06A_initial_check():
    dir_code = "06A"
    dir_path = "06_Personal/06A_Brand/"
    assert initial_check(dir_code) == dir_path


def test_06A1_initial_check():
    dir_code = "06A1"
    dir_path = "06_Personal/06A_Brand/06A1_Brand-1/"
    assert initial_check(dir_code) == dir_path


def test_06B_initial_check():
    dir_code = "06B"
    dir_path = "06_Personal/06B_Projects/"
    assert initial_check(dir_code) == dir_path


def test_06B1_initial_check():
    dir_code = "06B1"
    dir_path = "06_Personal/06B_Projects/06B1_Home-Lab/"
    assert initial_check(dir_code) == dir_path


def test_06C_initial_check():
    dir_code = "06C"
    dir_path = "06_Personal/06C_Workspace-Log/"
    assert initial_check(dir_code) == dir_path


def test_06C1_initial_check():
    dir_code = "06C1"
    dir_path = "06_Personal/06C_Workspace-Log/06C1_Laptop-Workspace/"
    assert initial_check(dir_code) == dir_path


def test_06C2_initial_check():
    dir_code = "06C2"
    dir_path = "06_Personal/06C_Workspace-Log/06C2_Web-Presence/"
    assert initial_check(dir_code) == dir_path


def test_06D_initial_check():
    dir_code = "06D"
    dir_path = "06_Personal/06D_Recommendation-List/"
    assert initial_check(dir_code) == dir_path


def test_06D1_initial_check():
    dir_code = "06D1"
    dir_path = "06_Personal/06D_Recommendation-List/06D1_Movies/"
    assert initial_check(dir_code) == dir_path


def test_06D2_initial_check():
    dir_code = "06D2"
    dir_path = "06_Personal/06D_Recommendation-List/06D2_Music/"
    assert initial_check(dir_code) == dir_path


def test_06D3_initial_check():
    dir_code = "06D3"
    dir_path = "06_Personal/06D_Recommendation-List/06D3_Books/"
    assert initial_check(dir_code) == dir_path


def test_07_initial_check():
    dir_code = "07"
    dir_path = "07_Attachments-and-Templates/"
    assert initial_check(dir_code) == dir_path


def test_07A_initial_check():
    dir_code = "07A"
    dir_path = "07_Attachments-and-Templates/07A_Attachments/"
    assert initial_check(dir_code) == dir_path


def test_07B_initial_check():
    dir_code = "07B"
    dir_path = "07_Attachments-and-Templates/07B_Templates/"
    assert initial_check(dir_code) == dir_path


def test_07B1_initial_check():
    dir_code = "07B1"
    dir_path = "07_Attachments-and-Templates/07B_Templates/07B1_Periodic-Notes/"
    assert initial_check(dir_code) == dir_path


def test_08_initial_check():
    dir_code = "08"
    dir_path = "08_Archive/"
    assert initial_check(dir_code) == dir_path

# Checking that Existing Directories are returned with correct code. <Ended>

# Checking with some regular expressions which matches with our internal regex. <Started>


def test_passing_wrong_but_regex_code_1():
    dir_code = f"01{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_10():
    dir_code = f"01A4{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_100():
    dir_code = f"05C{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_101():
    dir_code = f"05D{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_102():
    dir_code = f"05E{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_103():
    dir_code = f"06{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_104():
    dir_code = f"06A{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_105():
    dir_code = f"06A1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_106():
    dir_code = f"06B{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_107():
    dir_code = f"06B1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_108():
    dir_code = f"06C{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_109():
    dir_code = f"06C1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_11():
    dir_code = f"01B{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_110():
    dir_code = f"06C2{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_111():
    dir_code = f"06D{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_112():
    dir_code = f"06D1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_113():
    dir_code = f"06D2{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_114():
    dir_code = f"06D3{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_115():
    dir_code = f"07{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_116():
    dir_code = f"07A{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_117():
    dir_code = f"07B{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_118():
    dir_code = f"07B1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_119():
    dir_code = f"08{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_12():
    dir_code = f"01C{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_13():
    dir_code = f"01C1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_14():
    dir_code = f"02{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_15():
    dir_code = f"02A{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_16():
    dir_code = f"02A1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_17():
    dir_code = f"02A2{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_18():
    dir_code = f"02A3{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_19():
    dir_code = f"02B{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_2():
    dir_code = f"01A{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_20():
    dir_code = f"02B1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_21():
    dir_code = f"03{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_22():
    dir_code = f"03A{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_23():
    dir_code = f"03A1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_24():
    dir_code = f"03A2{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_25():
    dir_code = f"03A3{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_26():
    dir_code = f"03A4{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_27():
    dir_code = f"03B{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_28():
    dir_code = f"03B1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_29():
    dir_code = f"03B10{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_3():
    dir_code = f"01A1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_30():
    dir_code = f"03B2{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_31():
    dir_code = f"03B3{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_32():
    dir_code = f"03B4{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_33():
    dir_code = f"03B5{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_34():
    dir_code = f"03B6{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_35():
    dir_code = f"03B7{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_36():
    dir_code = f"03B8{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_37():
    dir_code = f"03B9{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_38():
    dir_code = f"03C{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_39():
    dir_code = f"03C1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_4():
    dir_code = f"01A2{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_40():
    dir_code = f"03C1A{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_41():
    dir_code = f"03C1A1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_42():
    dir_code = f"03C1A10{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_43():
    dir_code = f"03C1A11{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_44():
    dir_code = f"03C1A12{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_45():
    dir_code = f"03C1A13{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_46():
    dir_code = f"03C1A14{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_47():
    dir_code = f"03C1A15{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_48():
    dir_code = f"03C1A16{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_49():
    dir_code = f"03C1A17{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_5():
    dir_code = f"01A2A{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_50():
    dir_code = f"03C1A18{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_51():
    dir_code = f"03C1A2{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_52():
    dir_code = f"03C1A3{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_53():
    dir_code = f"03C1A4{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_54():
    dir_code = f"03C1A5{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_55():
    dir_code = f"03C1A6{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_56():
    dir_code = f"03C1A7{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_57():
    dir_code = f"03C1A8{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_58():
    dir_code = f"03C1A9{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_59():
    dir_code = f"03C1B{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_6():
    dir_code = f"01A2A1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_60():
    dir_code = f"03C1B1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_61():
    dir_code = f"03C1C{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_62():
    dir_code = f"03C1C1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_63():
    dir_code = f"03C2{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_64():
    dir_code = f"03C2A{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_65():
    dir_code = f"03C2B{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_66():
    dir_code = f"03C3{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_67():
    dir_code = f"03C3A{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_68():
    dir_code = f"03C3A1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_69():
    dir_code = f"03C3A2{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_7():
    dir_code = f"01A2B{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_70():
    dir_code = f"03C3A3{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_71():
    dir_code = f"03C3A4{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_72():
    dir_code = f"03C3B{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_73():
    dir_code = f"03C3B1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_74():
    dir_code = f"03C4{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_75():
    dir_code = f"03C4A{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_76():
    dir_code = f"03D{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_77():
    dir_code = f"03D1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_78():
    dir_code = f"03D2{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_79():
    dir_code = f"03D3{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_8():
    dir_code = f"01A2B1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_80():
    dir_code = f"03D4{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_81():
    dir_code = f"03D5{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_82():
    dir_code = f"04{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_83():
    dir_code = f"04A{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_84():
    dir_code = f"04A1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_85():
    dir_code = f"04A2{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_86():
    dir_code = f"04A3{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_87():
    dir_code = f"04A4{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_88():
    dir_code = f"04A5{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_89():
    dir_code = f"04A6{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_9():
    dir_code = f"01A3{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_90():
    dir_code = f"04A7{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_91():
    dir_code = f"04A99{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_92():
    dir_code = f"04B{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_93():
    dir_code = f"04B1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_94():
    dir_code = f"04B2{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_95():
    dir_code = f"04C{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_96():
    dir_code = f"04C1{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_97():
    dir_code = f"05{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_98():
    dir_code = f"05A{lorem_ipsum}"

    assert initial_check(dir_code) == DNT


def test_passing_wrong_but_regex_code_99():
    dir_code = f"05B{lorem_ipsum}"

    assert initial_check(dir_code) == DNT

# Checking with some regular expressions which matches with our internal regex. <Ended>

# Initial Check Ended

# dir.py Ended
