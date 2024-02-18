import typer

"""Another example based on https://typer.tiangolo.com/tutorial/terminating/"""

# Exiting a CLI program with an Error
# In Powershell you can check the Exit Code by typing $LASTEXITCODE (1=Error)
#               You can also use $? where False = last operation failed
# On the Mac I think it is echo $? where 1 = Error, 0 = No Error

existing_usernames = ["rick", "morty"]


def main(username: str):
    if username == "root":
        print("The root user is reserved")
        raise typer.Exit(code=1)
    print(f"New user created: {username}")


if __name__ == "__main__":
    typer.run(main)
