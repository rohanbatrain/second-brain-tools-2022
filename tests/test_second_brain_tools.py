from second_brain_tools.dir import initial_check

def test_main():
    dir_code = "01"
    assert initial_check(dir_code) == "01_Capture-System/", "01 returns 01_Capture-System/"

