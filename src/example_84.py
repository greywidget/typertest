import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/file/"""

"""
CLI options - File
`FileText` reading

Apart from the `Path` CLI parameters, you can also declare some types of "Files"

*In most cases you are probably just fine using `Path`. You can read and write
data with `Path` the same way...

The difference is that these types will give you a Python `file-like object`
instead of a Python `Path`

A `file-like object` is the same type of object returned by `open()` as in:
```
with open("file.txt") as f:
    # Here f is the file-like object
    read_data = f.read()
    print(read_data)
```

But in some special use cases you might want to use these special types. For
example if you are migrating an existing application.

`FileText` reading.
`typer.FileText` gives you a file-like object for reading text, you will get
`str` data from it.
This means that even if your file has text written in a non-english language, 
e.g. a `text.txt` file with:

`la cigüeña trae al niño`

You will have a `str` with the text inside e.g.:

`content = "la cigüeña trae al niño"`

instead of having `bytes`, e.g.:

`content = b"la cig\xc3\xbce\xc3\xb1a trae al ni\xc3\xb1o"`

You will get all the correct editor support, attributes, methods, etc for the
file-like object:
"""


def main(config: Annotated[typer.FileText, typer.Option()]):
    for line in config:
        print(f"Config line: {line}")


if __name__ == "__main__":
    typer.run(main)
