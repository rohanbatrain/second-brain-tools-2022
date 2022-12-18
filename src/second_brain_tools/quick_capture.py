from second_brain_tools.config import SECOND_BRAIN_DIRECTORY
from second_brain_tools.directories import initial_check
from second_brain_tools.defaults import NOTE_EXTENTION, NOTE_CREATED_SUCCESFULLY, INVALID_FILE_NAME_ERROR
from second_brain_tools.misc import file_name_check, file_creation


def quick_capture(qc_note_name, qc_note_content):
    fn_check = file_name_check(qc_note_name)
    if fn_check is True:
        #  Proceed
        qc_note_dir = initial_check("01A1")
        qc_note_location = SECOND_BRAIN_DIRECTORY + qc_note_dir + qc_note_name + NOTE_EXTENTION
        file_creation(qc_note_location, qc_note_content)
        print(NOTE_CREATED_SUCCESFULLY)
    elif fn_check is False:
        print(INVALID_FILE_NAME_ERROR)
    return fn_check
