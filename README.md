# fa_watches

Get your FA Watches.

## Installation

Both methods were made and tested on Windows 10 and **Python 3.7.2**.
The [2nd Version](#transfer) requires [Selenium](https://pypi.org/project/selenium/), [Firefox](https://www.mozilla.org/firefox/all/) as well as Firefox' [geckodriver](https://github.com/mozilla/geckodriver/releases/latest).

1. Install Selenium as you would install any other Python module, `pip install selenium`.
2. Install Firefox.
3. Download and extract Firefox' geckodriver into the python installation folder (usually `C:\Program Files\Python37\`)

## Usage

### [watches.py](watches.py)

1. Download the file (or copy-paste it, idc)
2. Put your FA username in the `USERNAME` variable ([line 6](watches.py#L6))
3. Execute it (`python3 watches.py`)
4. You'll get a file with your username containing all the accounts you were watching.

I plan to make it a bit more clean and enable you to auto-watch the accounts from a new account, in case you were switching accounts.
I gotta see about that tho...

### [transfer.py](transfer.py)

1. Download the file (or copy-paste it)
2. Put your FurAffinity Credentials in [line 66](transfer.py#66).
3. Execute the script (`python transfer.py`)
4. Log in when you land on the Login Page. The Script will pre-fill the values, if you supplied them.

#### Disclaimer

Your credentials never leave your PC. You enter them in the script and they will be used to log in, but that's it. If you want to make sure, check the Source Code, it's open source after all. If you still don't feel well with putting your Credentials somewhere else than FAs Login Page, don't use the script ¯\\\_(ツ)_/¯

## License

None, do as you please. I don't care lol

If you do a project/script based on these scripts, feel free to credit me for it, I'd appreciate it. But it's not necessary.
