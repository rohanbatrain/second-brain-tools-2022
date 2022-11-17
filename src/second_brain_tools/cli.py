"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -m second_brain_tools` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``second_brain_tools.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``second_brain_tools.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""

# Importing modules
import os



def main():
    """
    """

    setup()
    return 0

## Starting the module 

def setup():
  check=os.path.isfile(".env")
  if check == True:
    print("File already exist,Do you want to overwrite?")
    args1=input("Enter your choice, Y/N : ")
    if args1 == "Y":
      os.remove(".env")
      Second_Brain_Directory_input = input("Please enter your Vault dir: ")
      with open ('.env','w') as dot_env:
        dot_env.write ("Second_Brain_Directory = " + "\"" + Second_Brain_Directory_input + "\"")

    elif args1 == "N":
      print ("Nothing to do, Exiting...")
      exit()
      
  elif check == False:
    print("Config file is missing, generating one now..")
    Second_Brain_Directory_input = input("Please enter your Vault dir: ")
    with open ('.env','w') as dot_env:
        dot_env.write ("Second_Brain_Directory = " + "\"" + Second_Brain_Directory_input + "\"")
