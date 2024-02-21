import typer

"""See https://typer.tiangolo.com/tutorial/first-steps/"""

# This example shows a CLI option with a value
# Add lastname as a CLI option, give it a default value of ""

# If you run --help you will see lastname appears as option --lastname
# which takes a textual value.

# So - Giving a default value makes it a CLI option which means that:
# For booleans you have a --flag and --no-flag option
# For non-booleans, you pass the value after the --flag

"""
>>>python example_04.py Craig 60 --formal
Good day Ms. Craig

>>>python example_04.py Craig 60 --formal --lastname Richards
Good day Ms. Craig Richards
"""


def main(name: str, age: int, lastname: str = "", formal: bool = False):
    if formal:
        print(f"Good day Ms. {name} {lastname}")
    else:
        print(f"Hello {name}, what's it like to be {age}?")


if __name__ == "__main__":
    typer.run(main)
