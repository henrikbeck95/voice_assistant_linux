# About **VAL** project

## The history of this project

During the pandemic period I was trying to practice some physical exercises at home. I like to listen some music to get some extra motivation while doing my workout. Based on my experience, using a smartphone while running is not a good idea, accidents may occur. So, I start using an [Alexa]() device.

I really enjoy it quality besides that there was something I was really missing: reading the lyrics from the current song. I know it is not the propose from what `Alexa` has been made and the fact that there is no screen for implementing any graphical user interface is a limited spectre.

Thinking for a while about how I could solve this problem I had the idea to use my own laptop device for doing this task. Not only the sound control, but the entire desktop environment specially the window manager. By the way I had to development my own solution, my own virtual assistant, the **VAL** project.

Furthermore when I was planning about how to execute this ambitious plan I have started to thinking also about how people with special needs could be benefit from a project like this. Even there are a lot of **accessibility** tools I believe they will never be enough to satisfy every single case. If this project at once could help someone in this situation all the hard work is going to be rewarded. This combo of extra motivations is the fuel to pursuit this goal.

In Brazilian colleges it requires a final homework to complete the graduation. I have been talking with my great fried [Victor Ranalli]() about helping me during this project and he said: _"Why do not us develop the **VAL** to be our graduation project?"_ All I could say would be was: _"Why not?"_.

Thank you my friend for your contribution to this project specially about the software engineer documentation. I am sure without you this project would not be possible to reach the stage where it is in a very short time.

## The development process

We searched about how to develop a virtual assistant and many of materials and tutorials was returned as result. We have started filtering the content to attempt the window manager control and zero result were found. We had to build something totally unknown. We should have used our creativity to create something new from the begin.

During a long search we have found some interesting tools which could help us and speed up the development process. To make the story short we have been chosen the following tools:

- Start up setup

|Description            |Official name
|---                    |---
|Programming language   |Python
|Transcription library  |Speech Recognition
|Audio speech           |Pyttsx3
|Settings format        |YAML

The idea was very simple. It consisted about speaking a command. The command would be checked into the settings file to validate or not. And finally the user could get his return by executing what was told to be done. In case of not success it would return a spoken message informing the error.

Once we started developing the source code we have been faced a problem. A problem that we months and months to solve it. The libraries written in Python required a lower or equal 3.6 programming language version. Such as Python is native installed on Linux by default and at this point the current version was the 3.7, we could not easily go ahead.

Our first try was about running the **VAL** project inside a container. This process sounded like a nightmare because we had to guarantee three things:

- The requirement using the containerized method
    1. To be sure the user's machine virtualization mode is enable on BIOS.
    1. To be sure [Docker](), [Podman]() or [LXC]() would be installed on user's operating system.
    1. To be sure the container start up would be run using the appropriated flags to share the sound system between host and container.

It was not difficult to understand why we had to follow an alternative. This amazing solution could be [PyENV]() or [ASDF]() but they did not solve the problem as we had have imagine. We have gotten so closed with using `ASDF` but...

- Here are what happened to us:
    1. When Python was updated to 3.9 version the 3.6 version support was completely removed. We could not even compile the 3.6 version.
    
    1. To avoid this problem we should have compile the 3.8 version, then the 3.7 version and finally the 3.6 version.

    1. When we were using the 3.6 Python the PyAudio only worked if the operating system audio server was [ALSA]() or [PulseAudio]() with some `ALSA` extensions installed. In case of [Pipewire]() it failed even with `ALSA` extensions.

At time we could not do anything more to solve this problem using Python programming language. We stated another research about how to create an virtual assistant using [Java]() or [JavaScript](). While redesigning the entire application for `Java` we noticed that the same operating system audio server could fail in case `Pipewire` was set to be the default one.

- The reason for this belief was:
    1. `Java` is a full setup environment with his own tools.
    1. `Java` applications are portable for all operating systems because it run in a virtual machine called [Java Virtual Machine - JVM]().
    1. But the virtual machine once would require to talk with the host operating system audio system. At this point all the portability in theory could break.
    1. Unless there would be a library whose supports `Pipewire` it would work. Even thought we would set some source code treatment to support `PulseAudio` or `ALSA`. There would be some risks to take but the deadline was coming.

For some unknown reason I found a project called [Festival](). This could do what the `Pyttsx3` does and using a more human like audio speaker than `eSpeak5`. Once this tool is not written using Python we must have been sure the user has this software installed as a dependency whose Python could not threat but easily solved by the default operating system package manager.

Now there was another problem to be faced:

- How to connect Python + `Festival`?
    > Using Shell Script programming language to intermediate this communication.

After a few tests we have solved this problem. At this point "**VAL** leaned about how to speak". The focus was set to improve the functions treatment from the Shell Script file. This file has been became very robust and starting solving a collection of small solutions. We noticed we have the created our own library written in Shell Script.

We decided to migrate this library to a separated project repository called [**Shell Script Library**](https://github.com/henrikbeck95/shell_script_library) and use it as an external dependency. The reason for this was about [PyPi]() package structure does not pack any source code whose is not written in Python. Furthermore **Shell Script Library** has been became so gorgeous that it can help a lot of others projects development process.

Back to the **VAL** project we have refactored the Python source code to remove all the possible Python dependencies as we could in favor of **Shell Script Library**. We could now support current 3.10 Python version. We have changed from the ??? paradigm to _(OOP)_.

**VAL** is in alpha stage and it already does what it was made to be done: **VAL** executes voice commands and in case of invalid possibilities it returns the error message by speaking it contents.