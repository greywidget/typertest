from datetime import datetime

import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/datetime/"""

"""
Datetime CLI options

Custom date format
You can also customise the formats received for the `datetime` with the
`formats` parameter.

`formats` receives a list of strings with the date formats that would be
passed to `datetime.strptime()`
"""


def main(
    launch_date: Annotated[
        datetime,
        typer.Argument(
            formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y"]
        ),
    ],
):
    """
    Suppose you want to accept an ISO formatted datetime, but for some
    crazy reason you also want to accept a format with:
    - first the month
    - then the day
    - then the year
    - separated by `/`

    Try:
    - python example_78.py 1969-10-29 (iso format)
    - python example_78.py 10/29/1969  (additional odd format)

    """

    print(f"Launch will be at: {launch_date}")


if __name__ == "__main__":
    typer.run(main)
