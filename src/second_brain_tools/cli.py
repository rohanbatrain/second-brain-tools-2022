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

# Importing production modules // Meant for production branch
import typer
from second_brain_tools.setup import setup as sbt_setup
# Importing production modules finished


# Importing testing modules started // Meant for testing branch
# from second_brain_tools.dir import initial_check
# Importing testing modules finished


# Main function, which calls typer app here


def main():
    """
    Main Function, aka CLI app.
    """
    app()
    return 0


# Typer app Started

app = typer.Typer()

# Typer app Finished

# Starting the module


@app.command("Setup")
def setup():
    sbt_setup()


@app.command("Notes")
def notes():
    return


@app.command("Dirs")
def dir():
    return


@app.command("Quick-Create")
def quick_create():
    return


@app.command("Obsidian-Automations")
def obsidian_automations():
    return


@app.command("Daily-Notes")
def daily_notes():
    return


@app.command("Web-Services")
def web_service():
    return
