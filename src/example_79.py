from enum import Enum

import typer

"""See https://typer.tiangolo.com/tutorial/parameter-types/enum/"""

"""
CLI options - Enum Choices

To define a CLI parameter that can take a value from a predefined set
of values you can use a standard Python `enum.Enum`
"""


class NeuralNetwork(str, Enum):
    simple = "simple"
    conv = "conv"
    lstm = "lstm"


def main(network: NeuralNetwork = NeuralNetwork.simple):
    """
    Note that the function parameter `network` will be an `Enum`, not
    a `str`

    To get the `str` value back in your function's code use `network.value`

    Try:
    - python example_79.py --network conv (valid)
    - python example_79.py --network capsule (invalid)

    """
    print(f"Training neural network of type: {network.value}")


if __name__ == "__main__":
    typer.run(main)
