# System requirements

## Requirements tools

- Essential softwares to work.
    1. [x] Bash.
    1. [x] cURL.
    1. [x] GNU CoreUtils.
    1. [ ] [Festival]().
    1. [x] Linux kernel.
    1. [ ] Pip3.
    1. [ ] PyAudio.
    1. [x] Python >= 3.10 version.
    1. [ ] PyYaml library.
    1. [ ] [Shell Script Library](https://github.com/henrikbeck95/shell_script_library).
    1. [ ] SpeechRecognition library.
    1. [ ] Yaml-1.3 library.

## Setup dependencies

### Festival dependency

- ArchLinux
	> $ `sudo pacman -S festival festival-english festival-us python-pyaudio`
    <!--
    > $ `paru -S python-pyttsx3`
    -/->

<!--
- Debian
	> $ `sudo apt-get install festival`
-->

- Fedora <!--PyAudio-->
    > $ `sudo dnf install festival`

<!--
- Ubuntu
	> $ `sudo apt-get install festival`
-->

### **Shell Script Library** dependency

1. Download release latest version
    > $ `curl -fsSL github.com/henrikbeck95/shell_script_library/releases/latest/download/shell-script-library -O`

1. Move the **Shell Script Library** where your path environment can be loaded properly.
    - Moving the **Shell Script Library** into your system path
        > $ `mv ./shell-script-library /usr/local/bin/shell-script-library`

    - Moving the **Shell Script Library** into your local path
        > $ `mv ./shell-script-library $HOME/.local/bin/shell-script-library`

1. Give the executable permission
    > $ `chmod +x /usr/local/bin/shell-script-library`