import typer
from typing_extensions import Annotated

"""Another example based on https://typer.tiangolo.com/tutorial/options/prompt/"""

# CLI Option with Confirmation Prompt


def main(
    project_name: Annotated[str, typer.Option(prompt=True, confirmation_prompt=True)],
):
    print(f"Deleting project {project_name}")


if __name__ == "__main__":
    typer.run(main)
