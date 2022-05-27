from setuptools import setup, find_packages

######################################
#Create package for PyPi and upload it
######################################
#pip3 install setuptools
#pip3 install wheel
#python3 setup.py sdist bdist_wheel
#Upload the ./dist folder to PyPi
#pip3 install twine #For uploading
#twine upload dist/*
######################################
#pip3 install voice-assistant-linux
######################################

VERSION = '0.0.1'
DESCRIPTION = 'Virtual assistant from voice commands to control operating system graphical user interface.'

setup(
    name='voice-assistant-linux',
    version=VERSION,
    description=DESCRIPTION,
    author='Henrik Beck',
    author_email='henrikbeck95@gmail.com',
    license='GPL3',
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
        "License :: OSI Approved :: GPL3 License",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=[
        #'SpeechRecognition',
        'speech_recognition',
        'yaml-1.3'
    ],
)