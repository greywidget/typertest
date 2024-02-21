import typer
from rich.console import Console

"""See https://typer.tiangolo.com/tutorial/printing/"""

# Looking at "standard error" output

err_console = Console(stderr=True)


def main():
    err_console.print("Here is something written to standard error")


if __name__ == "__main__":
    typer.run(main)
