import typer

"""Another example based on https://typer.tiangolo.com/tutorial/terminating/"""

# Exiting a CLI program with an Error
# Special ABORT exception

existing_usernames = ["rick", "morty"]


def main(username: str):
    if username == "root":
        print("The root user is reserved")
        raise typer.Abort()
    print(f"New user created: {username}")


if __name__ == "__main__":
    typer.run(main)
