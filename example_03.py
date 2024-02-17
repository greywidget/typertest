"""Another example based on https://typer.tiangolo.com/tutorial/"""

# This time with Arguments and Options
# CLI options begin with -- so they are named, therefore order for these
# is not important

# By Default:
# - A CLI argument is required
# - A CLI option is optional

# Also
# - CLI arguments depend on the sequence order
# - CLI options start with -- and don't depend on the order

# Note that for this boolean flag, Type automatically creates a
# --formal and --no-formal option as shown if you run with the --help option

import typer


def main(name: str, age: int, formal: bool = False):
    if formal:
        print(f"Good day Ms. {name}")
    else:
        print(f"Hello {name}, what's it like to be {age}?")


if __name__ == "__main__":
    typer.run(main)
