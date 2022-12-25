# Importing production modules
import typer
import os
from second_brain_tools.setup import setup as sbt_setup
from second_brain_tools.quick_capture import quick_capture
from second_brain_tools.misc import random_file_from_dir
from second_brain_tools.directories import initial_check
from second_brain_tools.daily_note import (
    daily_note_bullet_journal_append,
    daily_note_bullet_journal_pregenerate_check,
    daily_note_moc_append,
    daily_note_moc_pregenerate_check,
)
from second_brain_tools.capture import (
    capture_link,
    capture_thought,
    capture_event,
    capture_task,
    capture_reminder,
    capture_meal,
    capture_sleep,
    capture_medicine,
    capture_mood,
    capture_water_intake,
    capture_exercise,
    capture_transaction,
    capture_symptom,
)
from second_brain_tools.notes import create_note, delete_note, move_note, view_note

# Importing production modules finished

# importing modules that are needed by other modules
from rich.console import List, Capture, Console  # noqa: F401
from rich.markdown import Markdown  # noqa: F401
from rich import print


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


# Starting the app fx()
@app.command("Quick-Capture")
def quick_capture_cli(name: str = typer.Option(..., prompt=True), content: str = typer.Option(..., prompt=True)):
    """
    Quickly capture a note in your inbox.
    """
    quick_capture(name, content)


@app.command("Bullet-Journal")
def daily_note_bullet_journal_cli(content: str = typer.Option(..., prompt=True)):
    """
    Capture a bullet point to your journal.
    """
    daily_note_bullet_journal_pregenerate_check()
    daily_note_bullet_journal_append(content)
    return


@app.command("Random-Note")
def random_note_cli(dir_code: str = typer.Option("04A", prompt=False)):
    """
    View a random note from your vault.
    """
    random_file_from_dir(dir_code)


# Adding app_config commands Started
@app_config.command("Setup")
def config_setup_cli():
    """
    A setup wizard to configure second_brain_tools.
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
def capture_thought_cli(
    name: str = typer.Option(..., prompt=True),
    summary: str = typer.Option(..., prompt=True),
    content: str = typer.Option(..., prompt=True),
):
    """
    Got a thought, capture it!
    """
    capture_thought(name, summary, content)


@app_capture.command("Link")
def capture_link_cli(
    url: str = typer.Option(..., prompt=True),
):
    """
    Got a url/link? Capture it.
    """
    capture_link(url)


@app_capture.command("Event")
def capture_event_cli(
    name: str = typer.Option(..., prompt=True),
    Type: str = typer.Option(..., prompt=True),
    location: str = typer.Option(..., prompt=True),
    summary: str = typer.Option(..., prompt=True),
    status: str = typer.Option(..., prompt=True),
):
    """
    Capture an event
    """
    capture_event(name, Type, location, summary, status)


@app_capture.command("Task")
def capture_task_cli(
    name: str = typer.Option(..., prompt=True),
    status: str = typer.Option(..., prompt=True),
    priority: str = typer.Option(..., prompt=True),
    labels: str = typer.Option(..., prompt=True),
    dependencies: str = typer.Option("NULL", prompt=True),
    parent_task: str = typer.Option("NULL", prompt=True),
    sub_task: str = typer.Option("NULL", prompt=True),
):
    """
    Capture a todo task
    """
    capture_task(name, status, priority, labels, dependencies, parent_task, sub_task)


@app_capture.command("Reminder")
def capture_reminder_cli(
    name: str = typer.Option(..., prompt=True),
    priority: str = typer.Option(..., prompt=True),
    labels: str = typer.Option(..., prompt=True),
    time_to_remind: str = typer.Option(..., prompt=True),
):
    """
    Capture a reminder.
    """
    capture_reminder(name, priority, labels, time_to_remind)


@app_capture.command("Meal")
def capture_meal_cli(
    name: str = typer.Option(..., prompt=True),
    time: str = typer.Option(..., prompt=True),
    Type: str = typer.Option(..., prompt=True),
    calories: str = typer.Option(..., prompt=True),
    taken: str = typer.Option(..., prompt=True)
):
    """
    Capture a meal.
    """
    capture_meal(name, time, Type, calories, taken)


@app_capture.command("Sleep")
def capture_sleep_cli(
    Name: str = typer.Option(..., prompt=True),
    Type: str = typer.Option(..., prompt=True),
    Hours: str = typer.Option(..., prompt=True),
    Time: str = typer.Option(..., prompt=True),
):
    """
    Capture a nap.
    """
    capture_sleep(Name, Type, Hours, Time)


@app_capture.command("Medicine")
def capture_medicine_cli(
    name: str = typer.Option(..., prompt=True),
    time: str = typer.Option(..., prompt=True),
    Type: str = typer.Option(..., prompt=True),
    taken: str = typer.Option(..., prompt=True),
):
    """
    Capture your medicine.
    """
    capture_medicine(name, time, Type, taken)


@app_capture.command("Mood")
def capture_mood_cli(
    name: str = typer.Option(..., prompt=True),
    status: str = typer.Option(..., prompt=True),
    reason: str = typer.Option(..., prompt=True),
):
    """
    Capture your mood.
    """
    capture_mood(name, status, reason)


@app_capture.command("Water-Intake")
def capture_water_intake_cli(
    name: str = typer.Option(..., prompt=True),
    time: str = typer.Option(..., prompt=True),
    amount: str = typer.Option(..., prompt=True),
):
    """
    Capture your water intake.
    """
    capture_water_intake(name, time, amount)


@app_capture.command("Exercise")
def capture_exercise_cli(
    name: str = typer.Option(..., prompt=True),
    time: str = typer.Option(..., prompt=True),
    cohort: str = typer.Option(..., prompt=True),
    status: str = typer.Option(..., prompt=True),
):
    """
    Capture your exercise/workouts.
    """
    capture_exercise(name, time, cohort, status)


@app_capture.command("Transaction")
def capture_transaction_cli(
    name: str = typer.Option(..., prompt=True),
    time: str = typer.Option(..., prompt=True),
    type: str = typer.Option(..., prompt=True),
    amount: str = typer.Option(..., prompt=True),
    account: str = typer.Option(..., prompt=True),
    invoice_url: str = typer.Option(..., prompt=True),
):
    """
    Capture a transaction.
    """
    capture_transaction(name, time, type, amount, account, invoice_url)


@app_capture.command("Symptom")
def capture_symptom_cli(
    name: str = typer.Option(..., prompt=True),
    status: str = typer.Option(..., prompt=True),
):
    """
    Capture a symptom.
    """
    capture_symptom(name, status)


# Adding app_capture commands Finished


# Adding app_notes commands Started
@app_notes.command("Create")
def notes_create_cli(
    dir_code: str = typer.Option(..., prompt=True),
    note_name: str = typer.Option(..., prompt=True),
    note_body: str = typer.Option(..., prompt=True),
):
    """
    Create a note in your desired directory.
    """
    create_note(dir_code, note_name, note_body)
    return


@app_notes.command("View")
def notes_view_cli(
    dir_code: str = typer.Option(..., prompt=True),
    note_name: str = typer.Option(..., prompt=True),
):
    """
    View a note in your desired directory.
    """
    view_note(dir_code, note_name)
    return


@app_notes.command("Move")
def notes_move_cli(
    old_dir_code: str = typer.Option(..., prompt=True),
    new_dir_code: str = typer.Option(..., prompt=True),
    note_name: str = typer.Option(..., prompt=True),
):
    """
    Move a note from/to your desired directory.
    """
    move_note(old_dir_code, new_dir_code, note_name)
    return


@app_notes.command("Delete")
def notes_delete_cli(
    dir_code: str = typer.Option(..., prompt=True),
    note_name: str = typer.Option(..., prompt=True),
):
    """
    Deleted a note from your desired directory.
    """
    delete_note(dir_code, note_name)
    return


# Adding app_notes commands Finished


# Adding app_daily_note commands Started


@app_daily_note.command("Append")
def daily_note_append_cli(
    content: str = typer.Option(..., prompt=True),
):
    "Append your daily note MOC using sbt."
    daily_note_moc_pregenerate_check()
    daily_note_moc_append(content)
    return

# daily_note_bullet_journal_append
# Adding app_daily_note commands Finished
# Adding app commands Finished
