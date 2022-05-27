import os
from setuptools import setup, find_packages

pathDirectoryCurrent = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(pathDirectoryCurrent, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

VERSION = '0.0.3'
DESCRIPTION = 'Virtual assistant from voice commands to control operating system graphical user interface.'

setup(
    name='voice-assistant-linux',
    version=VERSION,
    description=DESCRIPTION,
    author='Henrik Beck',
    author_email='henrikbeck95@gmail.com',
    license='GPL3',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/henrikbeck95/voice_assistant_linux/',
    packages=find_packages(),
    keywords=['val', 'voice assistant', 'i3wm', 'Unix Shell'],
    include_package_data=True,
    python_requires='>=3.10',
    classifiers=[
        #"Development Status :: 1 - Planning",
        #"Development Status :: 2 - Pre-Alpha",
        "Development Status :: 3 - Alpha",
        #"Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        #"Development Status :: 6 - Mature",
        #"Development Status :: 7 - Inactive",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=[
        'SpeechRecognition',
        'yaml-1.3'
    ],
)