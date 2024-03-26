import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/custom-types/"""

"""
Custom Types in Typer.

You can easily use your own custom types in `Typer` applications. It is achieved
by providing a way to parse input into your types. 
There are two ways to achieve this:
- Adding a type `parser`
- Expanding Click's custom types

This is an example of adding a Type Parser.
`typer.Argument` and `typer.Option` can create custom parameter types with a
`parser` callable.
"""


class CustomClass:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return f"<CustomClass: value={self.value}>"


def parse_custom_class(value: str):
    return CustomClass(value * 2)


def main(
    custom_arg: Annotated[CustomClass, typer.Argument(parser=parse_custom_class)],
    custom_opt: Annotated[CustomClass, typer.Option(parser=parse_custom_class)] = "Foo",
):
    """
    The function (or callable) that you pass to the parameter `parser` will
    receive the input value as a string and should return the parsed value with
    your own custom type
    """
    print(f"custom_arg is {custom_arg}")
    print(f"--custom-opt is {custom_opt}")


if __name__ == "__main__":
    typer.run(main)
