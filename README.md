# Voice Assistant for Linux

Say hi to VAL (Voice Assistant for Linux)!

## Description

A virtual assistant for Linux for controlling the operating system graphical user interface by using voice commands.

## Requirements

1. Linux kernel
1. For Python >= 3.10
1. PIP3

- Python libraries
    > $ `pip3 install SpeechRecognition`
    > $ `pip3 install yaml-1.3`

- ArchLinux
	> $ `sudo pacman -S festival festival-english festival-us python-pyaudio`

## Installation

1. Clone this repository.
    > $ `git clone https://github.com/henrikbeck95/voice_assistant_linux.git $HOME/Documents/`

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