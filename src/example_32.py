import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/options/password/"""

# CLI Option with Password Prompt
# (Just specify `hide_input=True`)


def main(
    name: str,
    password: Annotated[
        str, typer.Option(prompt=True, confirmation_prompt=True, hide_input=True)
    ],
):
    print(f"Hello {name}. Doing something very secure with password.")
    print(f"...just kidding, here it is, very insecure: {password}")


if __name__ == "__main__":
    typer.run(main)
