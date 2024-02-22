import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/arguments/optional/"""

# Optional CLI Arguments
# Remember that by default:
# - CLI options are optional
# - CLI arguments are required
# But this can be changed with this Alternative CLI Argument declaration
# In this first example, let's keep the CLI Argument as required
# (but using the alternative declaration)


def main(name: Annotated[str, typer.Argument()]):
    """
    Note that `name` is still required, we've simply used an alternative
    declaration to explicitly state that `name` is a CLI argument.
    """

    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
