from uuid import UUID

import typer

"""See https://typer.tiangolo.com/tutorial/parameter-types/uuid/"""

"""
UUIC CLI options
As below, your Python code will receive a standard Python UUID object
with all its attributes and methods, and as we are using annotations
it will also have proper type checks:
"""


def main(user_id: UUID):
    """
    try
    python example_76.py d48edaa6-871a-4082-a196-4daab372d4a1 (valid) and
    python example_76.py 7479706572-72756c6573 (invalid)
    """
    print(f"USER_ID is {user_id}")
    print(f"UUID version is: {user_id.version}")


if __name__ == "__main__":
    typer.run(main)
