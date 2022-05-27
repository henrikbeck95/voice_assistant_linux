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

<!--
- Python libraries
    > $ `pip3 install SpeechRecognition`

    > $ `pip3 install yaml-1.3`
-->

- ArchLinux
	> $ `sudo pacman -S festival festival-english festival-us python-pyaudio`

## Installation

1. Clone this repository.
    > $ `git clone https://github.com/henrikbeck95/voice_assistant_linux.git $HOME/Documents/`

<!--
1. PyPi repository
    > $ `pip3 install voice-assistant-linux`
-->

1. Run VAL (use Anaconda Python virtual environment)
    > $ `$(which python3) $HOME/Documents/voice_assistant_linux/src/main.py`.

## Usage

- Go into Val project folder
	> $ `cd $HOME/Documents/voice_assistant_linux/`

- Run Python3
	> $ `python3 ./src/`

## Uninstallation

- Remove the Val project folder
	> $ `rm -fr $HOME/Documents/voice_assistant_linux/`