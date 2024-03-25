from enum import Enum
from typing import List

import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/enum/"""

"""
CLI options - Enum Choices
List of Enum values

A CLI parameter can also take a list of `Enum` values:
"""


class Food(str, Enum):
    food_1 = "Eggs"
    food_2 = "Bacon"
    food_3 = "Cheese"


def main(groceries: Annotated[List[Food], typer.Option()] = [Food.food_1, Food.food_3]):
    """
    python main.py --help
    python main.py   (try with defaults)
    python main.py --groceries Eggs
    python main.py --groceries Eggs --groceries Cheese
    """
    print(f"Buying groceries: {', '.join([f.value for f in groceries])}")


if __name__ == "__main__":
    typer.run(main)
