# Voice Assistant for Linux

Say hi to VAL (Voice Assistant for Linux)

## Description

Virtual assistant from voice commands to control operating system graphical user interface.

## Setup environment

### Virtual environment

- ASDF
	```bash
	#!/usr/bin/env sh

	#Add Python plugin to ASDF
	asdf plugin-add python
	#asdf list all python | less

	#Install Python Anaconda3 2021.11 version
	asdf install python anaconda3-2021.11
	asdf global python anaconda3-2021.11

	#Fix cURL path 
	echo -e '#!/usr/bin/env bash              
	# asdf-plugin: python anaconda3-2021.11
	#exec /home/henrikbeck95/.asdf/bin/asdf exec "curl" "$@"
	exec /usr/bin/curl exec "curl" "$@"
	' > $HOME/.asdf/shims/curl

	#Install Python 3.10.4 version
	asdf install python 3.10.4

	#Install Python 3.7.13 version
	asdf install python 3.7.13
	asdf global python 3.7.13

	#Install Python 3.6-dev version
	asdf global python anaconda3-2021.11
	asdf install python 3.6-dev
	asdf global python 3.6-dev
	#python -V #Python 3.6.15+
	```

- Python libraries
	```bash
	#!/usr/bin/env sh

	#sudo pacman -S python-pip


	#python -m pip install pip==18.1
	#/usr/bin/pip -v
	

	/usr/bin/pip3 install pyttsx3
	/usr/bin/pip3 install speechrecognition
	/usr/bin/pip3 install yaml-1.3
	#/usr/bin/pip3 install 
	#/usr/bin/pip3 install python-espeak
	
	#/usr/bin/pip3 list
	```

### Requirements

1. Use a Linux operating system.

- Python package manager

1. Install [Anaconda on Linux](https://docs.anaconda.com/anaconda/install/linux/).
1. Install [Anaconda documents](https://docs.anaconda.com/anaconda/install/index.html).
1. Install [Git](https://git-scm.com/).

- Python libraries

```bash
conda install -c conda-forge speechrecognition
conda install -c conda-forge pip
pip install pyttsx3

#conda install -c conda-forge yaml
#conda install -c conda-forge pyyaml
#pip install yaml2
pip install yaml-1.3
#conda install -c anaconda yaml

pip install python-espeak
```

<!--
#Import system libraries
import os
import platform
import subprocess
import time

#Import external libraries
import pyttsx3
import speech_recognition as sr
import yaml
-->

### Installation

- Manually way

1. Clone this repository.
    > $ `git clone https://github.com/henrikbeck95/voice_assistant_linux.git $HOME/Documents/`

1. Run VAL (use Anaconda Python virtual environment)
    > $ `$(which python3) $HOME/Documents/voice_assistant_linux/src/main.py`.

### Uninstallation

???

## Usage

???
