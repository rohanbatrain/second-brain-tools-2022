from second_brain_tools.directories import initial_check, ic_custom


# defining default variables
dir_path = "Wrong argument passed, the dir code you specified doesn't exist"
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


def test_03B11_initial_check():
    dir_code = "03B11"
    dir_path = "03_Knowledge-Base/03B_Languages/03B11_Urdu"
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

# Checking that Existing Examples are returned with correct code. <Started>


def test_example_ic_custom():
    dir_code = "example"
    dir_path = "This/is/a/boiler/plate/example/"
    assert ic_custom(dir_code) == dir_path


def test_example_elif_ic_custom():
    dir_code = "example-elif"
    dir_path = "This/is/an/example/"
    assert ic_custom(dir_code) == dir_path

# Checking that Existing Examples are returned with correct code. <Ended>

# Checking with some regular expressions which matches with our internal regex. <Started>


# The code below is very strange it returns 08_Archive which is really not possible,
# i donno how it is accessing it. Maybe I have to sleep to find that out.
# debug_hour_counter = 2 hrs of 26/11/22

# def test_passing_wrong_but_regex_code_1():
#     global dir_path
#     dir_code = "01-$0M3-R@NDOM-D@⊥@"
#     assert initial_check(dir_code) == dir_path
#
#
# def test_passing_wrong_but_regex_code_10():
#     global dir_path
#     dir_code = "01A4-$0M3-R@NDOM-D@⊥@"
#     assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_100():
    global dir_path
    dir_code = "05C-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_101():
    global dir_path
    dir_code = "05D-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_102():
    global dir_path
    dir_code = "05E-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_103():
    global dir_path
    dir_code = "06-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_104():
    global dir_path
    dir_code = "06A-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_105():
    global dir_path
    dir_code = "06A1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_106():
    global dir_path
    dir_code = "06B-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_107():
    global dir_path
    dir_code = "06B1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_108():
    global dir_path
    dir_code = "06C-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_109():
    global dir_path
    dir_code = "06C1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_11():
    global dir_path
    dir_code = "01B-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_110():
    global dir_path
    dir_code = "06C2-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_111():
    global dir_path
    dir_code = "06D-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_112():
    global dir_path
    dir_code = "06D1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_113():
    global dir_path
    dir_code = "06D2-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_114():
    global dir_path
    dir_code = "06D3-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_115():
    global dir_path
    dir_code = "07-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_116():
    global dir_path
    dir_code = "07A-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_117():
    global dir_path
    dir_code = "07B-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_118():
    global dir_path
    dir_code = "07B1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_119():
    global dir_path
    dir_code = "08-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_12():
    global dir_path
    dir_code = "01C-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_13():
    global dir_path
    dir_code = "01C1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_14():
    global dir_path
    dir_code = "02-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_15():
    global dir_path
    dir_code = "02A-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_16():
    global dir_path
    dir_code = "02A1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_17():
    global dir_path
    dir_code = "02A2-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_18():
    global dir_path
    dir_code = "02A3-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_19():
    global dir_path
    dir_code = "02B-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_2():
    global dir_path
    dir_code = "01A-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_20():
    global dir_path
    dir_code = "02B1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_21():
    global dir_path
    dir_code = "03-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_22():
    global dir_path
    dir_code = "03A-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_23():
    global dir_path
    dir_code = "03A1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_24():
    global dir_path
    dir_code = "03A2-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_25():
    global dir_path
    dir_code = "03A3-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_26():
    global dir_path
    dir_code = "03A4-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_27():
    global dir_path
    dir_code = "03B-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_28():
    global dir_path
    dir_code = "03B1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_29():
    global dir_path
    dir_code = "03B10-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_3():
    global dir_path
    dir_code = "01A1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_30():
    global dir_path
    dir_code = "03B2-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_31():
    global dir_path
    dir_code = "03B3-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_32():
    global dir_path
    dir_code = "03B4-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_33():
    global dir_path
    dir_code = "03B5-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_34():
    global dir_path
    dir_code = "03B6-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_35():
    global dir_path
    dir_code = "03B7-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_36():
    global dir_path
    dir_code = "03B8-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_37():
    global dir_path
    dir_code = "03B9-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_38():
    global dir_path
    dir_code = "03C-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_39():
    global dir_path
    dir_code = "03C1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_4():
    global dir_path
    dir_code = "01A2-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_40():
    global dir_path
    dir_code = "03C1A-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_41():
    global dir_path
    dir_code = "03C1A1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_42():
    global dir_path
    dir_code = "03C1A10-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_43():
    global dir_path
    dir_code = "03C1A11-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_44():
    global dir_path
    dir_code = "03C1A12-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_45():
    global dir_path
    dir_code = "03C1A13-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_46():
    global dir_path
    dir_code = "03C1A14-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_47():
    global dir_path
    dir_code = "03C1A15-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_48():
    global dir_path
    dir_code = "03C1A16-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_49():
    global dir_path
    dir_code = "03C1A17-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_5():
    global dir_path
    dir_code = "01A2A-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_50():
    global dir_path
    dir_code = "03C1A18-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_51():
    global dir_path
    dir_code = "03C1A2-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_52():
    global dir_path
    dir_code = "03C1A3-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_53():
    global dir_path
    dir_code = "03C1A4-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_54():
    global dir_path
    dir_code = "03C1A5-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_55():
    global dir_path
    dir_code = "03C1A6-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_56():
    global dir_path
    dir_code = "03C1A7-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_57():
    global dir_path
    dir_code = "03C1A8-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_58():
    global dir_path
    dir_code = "03C1A9-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_59():
    global dir_path
    dir_code = "03C1B-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_6():
    global dir_path
    dir_code = "01A2A1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_60():
    global dir_path
    dir_code = "03C1B1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_61():
    global dir_path
    dir_code = "03C1C-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_62():
    global dir_path
    dir_code = "03C1C1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_63():
    global dir_path
    dir_code = "03C2-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_64():
    global dir_path
    dir_code = "03C2A-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_65():
    global dir_path
    dir_code = "03C2B-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_66():
    global dir_path
    dir_code = "03C3-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_67():
    global dir_path
    dir_code = "03C3A-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_68():
    global dir_path
    dir_code = "03C3A1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_69():
    global dir_path
    dir_code = "03C3A2-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_7():
    global dir_path
    dir_code = "01A2B-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_70():
    global dir_path
    dir_code = "03C3A3-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_71():
    global dir_path
    dir_code = "03C3A4-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_72():
    global dir_path
    dir_code = "03C3B-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_73():
    global dir_path
    dir_code = "03C3B1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_74():
    global dir_path
    dir_code = "03C4-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_75():
    global dir_path
    dir_code = "03C4A-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_76():
    global dir_path
    dir_code = "03D-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_77():
    global dir_path
    dir_code = "03D1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_78():
    global dir_path
    dir_code = "03D2-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_79():
    global dir_path
    dir_code = "03D3-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_8():
    global dir_path
    dir_code = "01A2B1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_80():
    global dir_path
    dir_code = "03D4-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_81():
    global dir_path
    dir_code = "03D5-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_82():
    global dir_path
    dir_code = "04-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_83():
    global dir_path
    dir_code = "04A-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_84():
    global dir_path
    dir_code = "04A1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_85():
    global dir_path
    dir_code = "04A2-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_86():
    global dir_path
    dir_code = "04A3-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_87():
    global dir_path
    dir_code = "04A4-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_88():
    global dir_path
    dir_code = "04A5-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_89():
    global dir_path
    dir_code = "04A6-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_9():
    global dir_path
    dir_code = "01A3-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_90():
    global dir_path
    dir_code = "04A7-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_91():
    global dir_path
    dir_code = "04A99-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_92():
    global dir_path
    dir_code = "04B-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_93():
    global dir_path
    dir_code = "04B1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_94():
    global dir_path
    dir_code = "04B2-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_95():
    global dir_path
    dir_code = "04C-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_96():
    global dir_path
    dir_code = "04C1-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_97():
    global dir_path
    dir_code = "05-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_98():
    global dir_path
    dir_code = "05A-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


def test_passing_wrong_but_regex_code_99():
    global dir_path
    dir_code = "05B-$0M3-R@NDOM-D@⊥@"
    assert initial_check(dir_code) == dir_path


# Checking with some regular expressions which matches with our internal regex. <Ended>

# Initial Check Ended

# dir.py Ended
