from enum import Enum

import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/enum/"""

"""
CLI options - Enum Choices
Case Sensitive

You can make an `Enum` (choice) CLI parameter case-insensitive with the
`case_sensitive` parameter
"""


class NeuralNetwork(str, Enum):
    simple = "simple"
    conv = "conv"
    lstm = "lstm"


def main(
    network: Annotated[
        NeuralNetwork, typer.Option(case_sensitive=False)
    ] = NeuralNetwork.simple,
):
    """
    These Enum values are now case insensitive. Hence these both work:

    python example_80.py --network CONV
    python example_80.py --network LsTm
    """

    print(f"Training neural network of type: {network.value}")


if __name__ == "__main__":
    typer.run(main)
