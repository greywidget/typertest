import items
import typer
import users

"""See https://typer.tiangolo.com/tutorial/subcommands/add-typer/"""

"""
Typer SubCommands - Command Groups

This example uses:
- items.py
- users.py
- app1.py (this file, which ties them together)

Lastly we create this file which ties them together:
- import the other Python modules (`users.py` and `items.py`)
- Create the main `typer.Typer()` application
- Use `app.add_typer()` to include the `app` from `items.py` and `users.py`,
  each of those 2 was also created with `typer.Typer()`
- Define a `name` with the command that will be used for each of these 
  "sub-Typers" to group their own commands.

 Now our CLI program has 2 commands:
 - `users`: with all of the commands (subcommands) in the `app` from `users.py`
 - `items`: with all of the commands (subcommands) in the `app` from `items.py`

 See how composable this is.
 Each `typer.Typer()` can be a CLI app by itself as well as being added 
 as a command group to another Typer app.
 """


app = typer.Typer()
app.add_typer(users.app, name="users")
app.add_typer(items.app, name="items")

if __name__ == "__main__":
    app()
