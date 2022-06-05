# Setup for **Shell Script Library** developer

This tutorial is dedicated for this project contributors.

## Installing

### Python libraries

1. Install Python libraries
    > $ `pip3 install SpeechRecognition`

    > $ `pip3 install pyyaml`

    > $ `pip3 install yaml-1.3`

    > $ `pip3 install setuptools`

    > $ `pip3 install wheel`

    > $ `pip3 install twine`

### **VAL**

- Clone **VAL** repository from GitHub.
    > $ `git clone --branch development https://github.com/henrikbeck95/voice_assistant_linux.git`

## Usage

1. Run it.
    > $ `python3 ./voice_assistant_linux/src/__init__.py`

## Packing to PiPy repository

1. Build the package for PyPi
    > $ `python3 setup.py sdist bdist_wheel`

1. Upload the package to PyPi repository
    > $ `twine upload dist/*`

<!--
cp ./src/speaking.sh ./build/lib/src/speaking.sh

cp ./src/settings.yml ./build/lib/src/settings.yml

cp ./src/libs/shell-script-library ./build/lib/src/libs/shell-script-library
-->