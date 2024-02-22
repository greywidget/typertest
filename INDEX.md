# Index of the Example scripts
### Introduction
There examples are from the [excellent Typer documentation](https://typer.tiangolo.com).  

- [The simplest Typer file (no arguments)](example_01.py)
- [With 2 CLI arguments](example_02.py)
- [With CLI arguments and CLI options](example_03.py)
- [CLI option with a value](example_04.py)
- [Document your app](example_05.py)
### Some Rich stuff
- [A table with Rich](example_06.py)
- [Output to standard error](example_07.py)
### Exiting the program
- [Exiting a CLI program](example_08.py)
- [Exiting a CLI program with an Error](example_09.py)
- [Exiting a CLI program with ABORT](example_10.py)
### CLI Arguments
- [Alternative CLI argument declaration](example_11.py)
- [Optional CLI argument](example_12.py)
- [Optional CLI argument with a Static default value](example_13.py)
- [Optional CLI argument with a Dynamic default value](example_14.py)
- [CLI argument with Help](example_15.py)
- [CLI argument with Help and Defaults](example_16.py)
- [CLI argument with Help and Hidden Default](example_17.py)
- [CLI argument with Help and Custom String Default](example_18.py)
- [CLI argument with Help and Custom Help Name (`metavar`)](example_19.py)
- [CLI argument with Help Panels (via `rich`)](example_20.py)
- [CLI argument - you can hide it](example_21.py)
- [CLI argument - reading an environment variable](example_22.py)
- [CLI argument - multiple environment variables](example_23.py)
- [CLI argument - hide environment variable from help text](example_24.py)
### CLI Options
- [CLI option with Help](example_25.py)
- [CLI option with Help Panels (via `rich`)](example_26.py)
- [CLI option with Hidden Default](example_27.py)
- [CLI option - make it Required](example_28.py)
- [CLI option Prompt](example_29.py)
- [CLI option with Customised Prompt](example_30.py)
- [CLI option with Confirmation Prompt](example_31.py)
- [CLI option with Password (hidden) Prompt](example_32.py)
- [CLI option with Custom Name](example_33.py)
- [CLI option with Custom Name and Short Name](example_34.py)
- [CLI option with Short Name Only](example_35.py)
- [CLI option with Short Name and Default Name](example_36.py)
- [CLI option with multiple Short Names Together](example_37.py)
- [CLI option with Callback for validation](example_38.py)

At this point in the tutorial there were examples about TAB completion using `typer-cli`. Although I followed the instructions, I couldn't get this to work on Windows or Mac so I'm leaving it out for now. Note if you install it and run `typer --install-completion`, it will alter your `powershell` or `zsh` startup.

This section also introduced the `click Context` which you get access to by declaring a function parameter of type `typer.Context`. I expect this will be revisited with later examples.

- [CLI option - accessing the `CallbackParam` object](example_39.py)
- [CLI option - first version of `--version`](example_40.py)
- [CLI option - showing the flaw in first `--version`](example_41.py)
- [CLI option - a better version of `--version`](example_42.py)
### Commands
- [Commands - explicitly creating the application](example_43.py)

I noticed that `--help` for an explicit application shows `--install-completion` and `--show-completion`. I'm not currently using completion as I had issues so it might be nice if those options could be hidden.

- [Commands - a CLI application with multiple commands](example_44.py)
- [Command CLI Arguments](example_45.py)
- [Command Options (and Command CLI Arguments)](example_46.py)
- [Command Help](example_47.py)
- [Command Help - Overwriting it](example_48.py)
- [Command Deprecation](example_49.py)
- [Command Add formatting with Rich Markup](example_50.py)
- [Command Add formatting with Rich Markdown](example_51.py)
