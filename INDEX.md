# Index of the Example scripts
### Introduction
There examples are from the [excellent Typer documentation](https://typer.tiangolo.com).  

- [The simplest Typer file (no arguments)](src/example_01.py)
- [With 2 CLI arguments](src/example_02.py)
- [With CLI arguments and CLI options](src/example_03.py)
- [CLI option with a value](src/example_04.py)
- [Document your app](src/example_05.py)
### Some Rich stuff
- [A table with Rich](src/example_06.py)
- [Output to standard error](src/example_07.py)
### Exiting the program
- [Exiting a CLI program](src/example_08.py)
- [Exiting a CLI program with an Error](src/example_09.py)
- [Exiting a CLI program with ABORT](src/example_10.py)
### CLI Arguments
- [Alternative CLI argument declaration](src/example_11.py)
- [Optional CLI argument](src/example_12.py)
- [Optional CLI argument with a Static default value](src/example_13.py)
- [Optional CLI argument with a Dynamic default value](src/example_14.py)
- [CLI argument with Help](src/example_15.py)
- [CLI argument with Help and Defaults](src/example_16.py)
- [CLI argument with Help and Hidden Default](src/example_17.py)
- [CLI argument with Help and Custom String Default](src/example_18.py)
- [CLI argument with Help and Custom Help Name (`metavar`)](src/example_19.py)
- [CLI argument with Help Panels (via `rich`)](src/example_20.py)
- [CLI argument - you can hide it](src/example_21.py)
- [CLI argument - reading an environment variable](src/example_22.py)
- [CLI argument - multiple environment variables](src/example_23.py)
- [CLI argument - hide environment variable from help text](src/example_24.py)
### CLI Options
- [CLI option with Help](src/example_25.py)
- [CLI option with Help Panels (via `rich`)](src/example_26.py)
- [CLI option with Hidden Default](src/example_27.py)
- [CLI option - make it Required](src/example_28.py)
- [CLI option Prompt](src/example_29.py)
- [CLI option with Customised Prompt](src/example_30.py)
- [CLI option with Confirmation Prompt](src/example_31.py)
- [CLI option with Password (hidden) Prompt](src/example_32.py)
- [CLI option with Custom Name](src/example_33.py)
- [CLI option with Custom Name and Short Name](src/example_34.py)
- [CLI option with Short Name Only](src/example_35.py)
- [CLI option with Short Name and Default Name](src/example_36.py)
- [CLI option with multiple Short Names Together](src/example_37.py)
- [CLI option with Callback for validation](src/example_38.py)

At this point in the tutorial there were examples about TAB completion using `typer-cli`. Although I followed the instructions, I couldn't get this to work on Windows or Mac so I'm leaving it out for now. Note if you install it and run `typer --install-completion`, it will alter your `powershell` or `zsh` startup.

This section also introduced the `click Context` which you get access to by declaring a function parameter of type `typer.Context`. I expect this will be revisited with later examples.

- [CLI option - accessing the `CallbackParam` object](src/example_39.py)
- [CLI option - first version of `--version`](src/example_40.py)
- [CLI option - showing the flaw in first `--version`](src/example_41.py)
- [CLI option - a better version of `--version`](src/example_42.py)
### Commands
- [Commands - explicitly creating the application](src/example_43.py)

I noticed that `--help` for an explicit application shows `--install-completion` and `--show-completion`. I'm not currently using completion as I had issues so it might be nice if those options could be hidden.

- [Commands - a CLI application with multiple commands](src/example_44.py)
- [Command CLI Arguments](src/example_45.py)
- [Command Options (and Command CLI Arguments)](src/example_46.py)
- [Command Help](src/example_47.py)
- [Command Help - Overwriting it](src/example_48.py)
- [Command Deprecation](src/example_49.py)
- [Command Add formatting with Rich Markup](src/example_50.py)
- [Command Add formatting with Rich Markdown](src/example_51.py)
- [Command Help Panels for Commands](src/example_52.py)
- [Command Help Panels for CLI Parameters](src/example_53.py)
- [Command Help - add an Epilog](src/example_54.py)
