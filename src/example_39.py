import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/options/callback-and-context/"""

# Accessing the `Click CallbackParam` object.
# The same way you can access the `typer.Context` by declaring a function
# parameter with its value, you can declare another function parameter
# with type `typer.CallbackParam` to get the specific Click `Parameter`
# object.
# For example if you nad a callback that could be used by several CLI
# parameters, that way the callback would know which parameter each time.

# See the end of the above doc link for a short summary of the
# technical details


def name_callback(ctx: typer.Context, param: typer.CallbackParam, value: str):
    if ctx.resilient_parsing:
        return
    print(f"Validating param: {param.name}")
    if value != "Camila":
        raise typer.BadParameter("Only Camila is allowed")
    return value


def main(name: Annotated[str, typer.Option(callback=name_callback)]):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
