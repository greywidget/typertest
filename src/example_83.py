from pathlib import Path

import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/path/"""

"""
CLI options - Path validations

You can perform several validations for `Path` CLI parameters:

- `exists`: If set to true, the file or directory needs to exist for this
    value to be valid. If this is not required and a file does indeed not
    exist, then all further checks are silently skipped. 
- `file_okay`: controls if a file is a possible value.
- `dir_okay`: controls if a directory is a possible value.
- `writable`: if true, a writable check is performed.
- `readable`: if true, a readable check is performed.
- `resolve_path`: if this is true, then the path is fully resolved before the
    value is passed onwards. This means that it's absolute and symlinks are
    resolved.

*Note that it will not expand a tilde-prefix (~/Documents), as this is 
supposed to be something that is done by the shell only.
"""


def main(
    config: Annotated[
        Path,
        typer.Option(
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
        ),
    ],
):
    text = config.read_text()
    print(f"Config file contents: {text}")


if __name__ == "__main__":
    typer.run(main)
