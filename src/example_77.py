from datetime import datetime

import typer

"""See https://typer.tiangolo.com/tutorial/parameter-types/datetime/"""

"""
Datetime CLI options
As below, your Python code will receive a standard Python `datetime` object
with all its attributes and methods:
"""


def main(birth: datetime):
    """
    Typer will accept any string from the following formats:
    - `%Y-%m-%d`
    - `%Y-%m-%dT%H:%M:%S`
    - `%Y-%m-%d %H:%M:%S`

    Try:
    - python example_77.py 1956-01-31T10:00:00  (valid)
    - python example_77.py july-19-1989  (invalid)

    """

    print(f"Interesting day to be born: {birth}")
    print(f"Birth hour: {birth.hour}")


if __name__ == "__main__":
    typer.run(main)
