"""See https://typer.tiangolo.com/tutorial/first-steps/"""

# Let's add a CLI argument (or 2)

import typer


def main(name: str, age: int):
    print(f"Hello {name}, what's it like to be {age}?")


if __name__ == "__main__":
    typer.run(main)
