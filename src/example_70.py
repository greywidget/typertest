import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/number/"""

"""
CLI Parameter Types Clamping Numbers

Instead of showing an error, you might want to use the closest minimum or
maximum valid value.

You can do this with the `clamp` parameter:
"""


def main(
    id: Annotated[int, typer.Argument(min=0, max=1000)],
    rank: Annotated[int, typer.Option(max=10, clamp=True)] = 0,
    score: Annotated[float, typer.Option(min=0, max=100, clamp=True)] = 0,
):
    print(f"ID is {id}")
    print(f"--rank is {rank}")
    print(f"--score is {score}")


if __name__ == "__main__":
    typer.run(main)
