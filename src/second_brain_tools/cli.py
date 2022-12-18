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
# // Meant for production branch
# Importing production modules
import typer
import os
from second_brain_tools.setup import setup as sbt_setup
from second_brain_tools.quick_capture import quick_capture
from second_brain_tools.misc import random_file_from_dir, view_note_with_dir
from second_brain_tools.directories import initial_check
# Importing production modules finished


# Main function, which calls typer app here
def main():
    """
    Main Function, aka CLI app.
    """
    app()
    return 0


# Typer app Started
# Defining typers Started
app = typer.Typer()
app_notes = typer.Typer()
app_daily_note = typer.Typer()
app_capture = typer.Typer()
app_config = typer.Typer()
# Defining typers Finished
# Adding typers to main app Started
app.add_typer(app_notes, name="Notes", help="Notes specific commands.")
app.add_typer(app_capture, name="Capture", help="Capture a note using predefined flows.")
app.add_typer(app_daily_note, name="Daily-Note", help="Daily Note Specific Commands.")
app.add_typer(app_config, name="Config", help="Shows you configurable options.")
# Adding typers to main app Finished
# Typer app Finished


# Starting the module
# Finishing the module


# Starting the app fx()

@app.command("Quick-Capture")
def quick_capture_cli(name: str = typer.Option(..., prompt=True), content: str = typer.Option(..., prompt=True)):
    """
    Quickly capture a note in your inbox.
    """
    quick_capture(name, content)


@app.command("Random-Note")
def random_note_cli(dir_code: str = typer.Option(..., prompt=True)):
    """
    View a random note from your vault.
    """
    rnc_dir = random_file_from_dir(dir_code)
    view_note_with_dir(rnc_dir)


# Adding app_config commands Started
@app_config.command("Setup")
def config_setup_cli():
    """
    A setup wizard to configure second_brain_tools
    """
    sbt_setup()


@app_config.command("Check")
def config_check_cli(dir_code):
    """
    A Check Wizard which validates if a directory exist with dir_code provided
    """
    ccc_dir = initial_check(dir_code)
    ccc_check = os.path.isdir(ccc_dir)
    if ccc_check is True:
        print("The directory exists")
    else:
        print("The directory does not exist")

# Adding app_config commands Finished


# Adding app_capture commands Started
@app_capture.command("Thought")
def capture_thought_cli():
    """
    Had a thought? Capture it.
    """


@app_capture.command("Link")
def capture_link_cli():
    """
    Got a url/link? Capture it.
    """


# Adding app_capture commands Finished


# Adding app_notes commands Started


@app_notes.command("Create")
def notes_create_cli():

    return


@app_notes.command("View")
def notes_view_cli():

    return


@app_notes.command("Move")
def notes_move_cli():

    return


@app_notes.command("Delete")
def notes_delete_cli():

    return


# Adding app_notes commands Finished


# Adding app_daily_note commands Started


@app_daily_note.command("Append")
def daily_note_append_cli():
    "Append your daily note MOC using sbt."
    return


@app_daily_note.command("Regenerate")
def daily_note_regenerate_cli():
    "Regenerates the daily note MOC."
    return


# Adding app_daily_note commands Finished

# Adding app commands Finished
