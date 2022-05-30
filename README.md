# Voice Assistant for Linux

Say hi to VAL (Voice Assistant for Linux)!

## Description

A virtual assistant for Linux for controlling the operating system graphical user interface by using voice commands.

- Project task list status
    1. [x] Human voice recognition.
    1. [x] Human voice transcription.
    1. [x] Detects voice commands from a defined list and executes it.
    1. [x] Debug mode.
    1. [x] Works on i3 tiling window manager.
    1. [ ] Works on Gnome desktop environment.
    1. [ ] Works on KDE Plasma desktop environment.
    1. [ ] Works on XFCE desktop environment.
    1. [ ] Infinite while loop should be implement.

- Warning
    1. The software run only at once. This should be fixed by implementing the infinity while loop. The problem here is to define a strategy to invoke only the voice command after the user say 'Val'. Furthermore the source code must be returned to wait the 'Val' to be called again.

## Requirements

1. [ ] Linux kernel.
1. [ ] Python >= 3.10 (only because the match case and 'f' strings).
1. [ ] PIP3.

- ArchLinux
	> $ `sudo pacman -S festival festival-english festival-us python-pyaudio`

<!--
- Debian
	> $ `sudo apt-get install festival`

- Fedora
	> $ `sudo dnf install festival`

- Ubuntu
	> $ `sudo apt-get install festival`
-->

## Installation

### Development mode

1. Install Python libraries
    > $ `pip3 install SpeechRecognition`

    > $ `pip3 install yaml-1.3`

    > $ `pip3 install setuptools`

    > $ `pip3 install wheel`

    > $ `pip3 install twine`

    > $ `pip3 install voice-assistant-linux`

1. Clone this repository.
    > $ `git clone https://github.com/henrikbeck95/voice_assistant_linux.git`

1. Build the package for PyPi
    > $ `python3 setup.py sdist bdist_wheel`

1. Upload the package to PyPi repository
    > $ `twine upload dist/*`

<!--
cp ./src/speaking.sh ./build/lib/src/speaking.sh

cp ./src/settings.yml ./build/lib/src/settings.yml

cp ./src/libs/shell-script-library ./build/lib/src/libs/shell-script-library
-->

### Normal usage mode

1. Install from PyPi repository
    > $ `pip3 install voice-assistant-linux`

## Usage

### Development mode

1. Run it.
    > $ `python3 ./src/__init__.py`

<!--
### Normal usage mode

1. Run it.
    > $ `voice-assistant-linux`
-->

## Uninstallation

### Development mode

- Remove the Val project folder
	> $ `rm -fr ./voice_assistant_linux/`

<!--
### Normal usage mode

1. Uninstall it.
    > $ `pip3 unistall voice-assistant-linux`
-->