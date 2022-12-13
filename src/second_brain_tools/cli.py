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
# // Meant for testing branch
# Importing testing modules started
# Importing testing modules finished

# // Meant for production branch
# Importing production modules
import typer
from second_brain_tools.setup import setup as sbt_setup
# from second_brain_tools.config import DNM_APPEND_TYPE, GLOBAL_APPEND_TYPE
# from second_brain_tools.append import plain_text_append
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
app_capture = typer.Typer()
# Defining typers Finished

# Adding typers to main app Started
app.add_typer(app_notes, name="Notes", help="Notes specific commands.")
app.add_typer(app_capture, name="Capture", help="Capture a note using predefined flows.")
app.add_typer(app_daily_note, name="Daily-Note", help="Daily Note Specific Commands.")
# Adding typers to main app Finished

# Typer app Finished

# Starting the module

# Adding app testing commands Started


# @app.command("test")
# def test():
#     """
#     A temporary command to test debugging.
#     """

# Adding app testing commands Finished

# Adding app commands started


@app.command("Setup")
def setup():
    """
    A setup wizard to configure second_brain_tools
    """
    sbt_setup()


@app.command("Quick-Capture")
def quick_capture():
    """
    Quickly capture a note in your inbox.
    """


@app.command("Random-Note")
def random_note():
    """
    View a random note from your vault.
    """
    # knowledge or evergreen note.
    # pass --knowledge-base , --evergreen to explicitely choose.
    # default evergreen notes.


# Adding app_capture commands Started
@app_capture.command("Thought")
def capture_thought():
    """
    Had a thought? Capture it.
    """


@app_capture.command("Link")
def capture_link():
    """
    Got a url/link? Capture it.
    """


# Adding app_capture commands Finished


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


# Adding app_daily_note commands Started


@app_daily_note.command("Generate")
def daily_note_generate():
    "Generate your daily note MOC using sbt."
    return


@app_daily_note.command("Append")
def daily_note_append():
    "Append your daily note MOC using sbt."
    return


@app_daily_note.command("Regenerate")
def daily_note_regenerate():
    "Regenerates the daily note MOC."
    return

# Adding app_daily_note commands Finished

# Adding app commands Finished
