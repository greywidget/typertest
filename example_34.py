import typer
from typing_extensions import Annotated

"""Another example based on https://typer.tiangolo.com/tutorial/options/name/"""

# CLI Option Short Names

"""
The excellent Typer documentation has a few notes around this. See the link
above. Here is a summary

- Short Names comprise of a dash and a single letter e.g `-n`
- Multiple Short Names can be grouped with a single dash e.g -np (== -pn)
- If you have a CLI option with a value (as opposed to a boolean) it can
  be grouped but the one with the value must be the last so it can receive
  the value e.g. in

     tar -xvf myproject.tar.gz

     x and v are booleans. f is a filename and takes the value myproject.tar.gz

- To define a short name, add it into `typer.Option` along with the default
   name or a custom name.
- If you just put the short name, that is all that will be available
"""


def main(user_name: Annotated[str, typer.Option("--name", "-n")]):
    """
    Overwrite the CLI option name and also add a short name
    """

    print(f"Hello {user_name}")


if __name__ == "__main__":
    typer.run(main)
