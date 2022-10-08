# spam_man

cheap customizable spammer.

requires keyboard and guizero

Yeah, the main (gui) window will freeze while in use, that is fine don't close it.

The only way to stop the script is to close the terminal window. (Just a warning)

To run it, get Python, then clone the code for this repo or click "Download ZIP" under the "Code" button. Run the .py file after installing dependencies.

## Installation

### Main dependencies

#### Windows/Arch Linux/Manjaro/Endeavor OS/Garuda Linux

```cmd
pip install guizero keyboard
```

#### MacOS/Non-Arch Linux

```bash
pip3 install guizero keyboard
```

Linux users will need to install tk **AND** run the script as root (ex. `sudo python main.py`).

### tk (For Linux users)

#### Debian/Ubuntu

```bash
sudo apt install tk
```

#### Arch Linux

```bash
sudo pacman -S tk
```

#### Fedora

```bash
sudo dnf install tk
```
