import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/file/"""

"""
You can use several configuration parameters for these types (classes) in
`typer.Option()` and `typer.Argument()`:

- `mode`: controls the "mode" you open the file with. By default, `Typer` will
    configure the `mode` for you:
    - `typer.FileText`: `mode="r"` to read text.
    - `typer.FileTextWrite`: `mode="w"` to write text.
    - `typer.FileBinaryRead`: `mode="rb"` to read binary data.
    - `typer.FileBinaryWrite`: `mode="wb"` to write binary data.

- `encoding`: to force a specific encoding, e.g. `"utf-8"`

- `lazy`: delay I/O operations. Automatic by default.
    By default, when writing files, Click will generate a file-like object that
    is not yet the actual file. Once you start writing, it will go, open the 
    file and start writing to it, but not before. This is mainly useful to
    avoid creating the file until you start writing to it. It's normally safe
    to leave this automatic. But you can overwrite it setting `lazy=False`. By
    default it's `lazy=True` for writing and `lazy=False` for reading.

- `atomic`: if true, all writes will actually go to a temporal file and then
    moved to the destination file after completing. This is useful with files
    modified frequently by several users/programs.

`typer.FileTextWrite` is actually just a convenience class. It's the same as
using `typer.FileText` with `mode="w"`.

Customise `mode`
You can override the `mode` from the defaults above. For example, you could use
`mode="a"` to write "appending" to the same file:
"""


def main(config: Annotated[typer.FileText, typer.Option(mode="a")]):
    config.write("This is a single line\n")
    print("Config line written")


if __name__ == "__main__":
    typer.run(main)
