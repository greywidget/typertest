import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/number/"""

"""
CLI Parameter Types Number

You can define numeric validations with `max` and `min` values for `int` and
`float` CLI parameters:
"""


def main(
    id: Annotated[int, typer.Argument(min=0, max=1000)],
    age: Annotated[int, typer.Option(min=18)] = 20,
    score: Annotated[float, typer.Option(max=100)] = 0,
):
    print(f"ID is {id}")
    print(f"--age is {age}")
    print(f"--score is {score}")


if __name__ == "__main__":
    typer.run(main)
