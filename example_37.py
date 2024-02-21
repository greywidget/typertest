import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/options/name/"""

# CLI Option Short Names together
# You can create multiple short names and use them together
# N.B. You can only have a single non-boolean and it must go last so
# it can receive the value so:
# `python .\example_37.py -fn Widget` is fine
# `python .\example_37.py -nf Widget` would throw an exception because
# the `Str` parameter `--name` (`-n`) must go last to receive the value
# `Widget`


def main(
    name: Annotated[str, typer.Option("--name", "-n")],
    formal: Annotated[bool, typer.Option("--formal", "-f")] = False,
):
    if formal:
        print(f"Good day Ms. {name}.")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
