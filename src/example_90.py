import click
import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/custom-types/"""

"""
Custom Types in Typer.

This is an example using the Click Custom Type.

If you already have a Click Custom Type yoe can use it in `typer.Argument()`
and `typer.Option()` with the `click_type` parameter.
"""


class CustomClass:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return f"<CustomClass: value={self.value}>"


class CustomClassParser(click.ParamType):
    name = "CustomClass"

    def convert(self, value, param, ctx):
        return CustomClass(value * 3)


def main(
    custom_arg: Annotated[CustomClass, typer.Argument(click_type=CustomClassParser())],
    custom_opt: Annotated[
        CustomClass, typer.Option(click_type=CustomClassParser())
    ] = "Foo",
):
    print(f"custom_arg is {custom_arg}")
    print(f"--custom-opt is {custom_opt}")


if __name__ == "__main__":
    typer.run(main)
