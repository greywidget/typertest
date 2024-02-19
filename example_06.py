import typer
from rich.console import Console
from rich.table import Table

"""Another example based on https://typer.tiangolo.com/tutorial/printing/"""

# This example has some basic "rich" stuff

console = Console()


def main():
    table = Table("Name", "Item")
    table.add_row("Rich", "Portal Gun")
    table.add_row("Morty", "Plumbus")
    console.print(table)


if __name__ == "__main__":
    typer.run(main)
