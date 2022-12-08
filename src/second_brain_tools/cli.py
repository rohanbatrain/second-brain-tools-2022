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

# Importing testing modules started // Meant for testing branch
# from second_brain_tools.dir import initial_check
# Importing testing modules finished

# Importing production modules // Meant for production branch
import typer
from second_brain_tools.setup import setup as sbt_setup
# Importing production modules finished

# Defining default variables Started
test_crs = "Command ran successfully."
# Defining default variables Finished

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
app_dirs = typer.Typer()
app_daily_note = typer.Typer()
# Defining typers Finished

# Adding typers to main app Started
app.add_typer(app_notes, name="Notes", help="Notes specific commands.")
app.add_typer(app_dirs, name="Dirs", help="Directories specific commands.")
app.add_typer(app_daily_note, name="Daily-Note", help="Daily Note Specific Commands.")
# Adding typers to main app Finished

# Typer app Finished

# Starting the module

# Adding app commands started


@app.command("Setup")
def setup():
    """
    A setup wizard to configure second_brain_tools
    """
    sbt_setup()


@app.command("Quick-Create")
def quick_create():
    """
    Quickly create a note in your second brain inbox.
    """


# Adding app_notes commands Started


@app_notes.command("Create")
def notes_create():

    return


@app_notes.command("View")
def notes_view():

    return


@app_notes.command("Move")
def notes_move():

    return


@app_notes.command("Delete")
def notes_delete():

    return


# Adding app_notes commands Finished

# Adding app_dirs commands Started

@app_dirs.command("Create")
def dirs_create():

    return


@app_dirs.command("Rename")
def dirs_rename():

    return


@app_dirs.command("Move")
def dirs_move():

    return


@app_dirs.command("Delete")
def dirs_delete():

    return
# Adding app_dirs commands Finished

# Adding app_daily_note commands Started


@app_daily_note.command("Create")
def daily_note_create():

    return


@app_daily_note.command("Recreate")
def daily_note_recreate():
    """Deletes the content of the daily note (today) and start over."""
    return

# Adding app_daily_note commands Finished

# Adding app commands Finished
