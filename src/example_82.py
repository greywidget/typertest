from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/path/"""

"""
CLI options - Paths

You can declare a CLI parameter to be a standard Python `pathlib.Path`
This is what you would do for directory paths and file paths:
"""


def main(config: Annotated[Optional[Path], typer.Option()] = None):
    if config is None:
        print("No config file")
        raise typer.Abort()
    if config.is_file():
        text = config.read_text()
        print(f"Config file contents: {text}")
    elif config.is_dir():
        print("Config is a directory, will use all its config files")
    elif not config.exists():
        print("The config doesn't exist")


if __name__ == "__main__":
    typer.run(main)
