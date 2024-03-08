import typer

"""See https://typer.tiangolo.com/tutorial/parameter-types/"""

"""
CLI Parameter Types Intro

You can use several data types for the CLI options and CLI arguments, and you
can add data validation requirements too.

DATA CONVERSION
When you declare a CLI parameter with some type `Typer` will convert the data
received in the command line to that data type.

Try calling this program with:
`python example_68.py Camila --age 15 --height-meters 1.70 --female`

Also try calling it with an incorrect type:
`python example_68.py Camila --age 15.7`
"""


app = typer.Typer()


def main(name: str, age: int = 20, height_meters: float = 1.89, female: bool = True):
    print(f"NAME is {name}, of type: {type(name)}")
    print(f"--age is {age}, of type: {type(age)}")
    print(f"--height-meters is {height_meters}, of type: {type(height_meters)}")
    print(f"--female is {female}, of type: {type(female)}")


if __name__ == "__main__":
    typer.run(main)
