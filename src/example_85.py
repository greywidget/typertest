import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/file/"""

"""
CLI options - File
`FileTextWrite` reading

For writing text, you can use `type.FileTextWrite`

This would be for writing human text, like:
```
some settings
la cigüeña trae al niño
```

Not for writing binary `bytes`

Note that:
`typer.FileTextWrite` is just a convenience class. It's the same as using
`typer.FileText` and setting `mode="w"`.
"""


def main(config: Annotated[typer.FileTextWrite, typer.Option()]):
    config.write("Some config written by the app")
    print("Config written")


if __name__ == "__main__":
    typer.run(main)
