import typer
from typing_extensions import Annotated

"""Another example based on https://typer.tiangolo.com/tutorial/arguments/help/"""

# You can read values from Environmental Variables. In the example below:
# 1. If an argument is passed, `name` gets that value.
# 2. If no argument is passed and the `envar` exists, `name` gets that value
# 3. Otherwise `name` gets the default value of "Unknown"
# --help shows these details


def main(
    name: Annotated[str, typer.Argument(envvar="VIRTUAL_ENV_PROMPT")] = "Unknown",
):
    print(f"Your Virtual Environment is: {name}")


if __name__ == "__main__":
    typer.run(main)
