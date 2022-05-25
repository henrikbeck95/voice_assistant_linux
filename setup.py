from setuptools import setup, find_packages

setup(
    name='voice-assistant-for-linux',
    version='0.0.1',
    description='Virtual assistant from voice commands to control operating system graphical user interface.',
    author='Henrik Beck',
    author_email='henrikbeck95@gmail.com',
    license='GPL3',
    long_description_content_type='text/markdown',
    url='https://github.com/henrikbeck95/voice_assistant_linux/',
    packages=find_packages(),
    
    entry_points={
        'console_scripts': [
#            'lyrics = lyrics.lyrics_in_terminal:start'
            'val = val.src:start'
        ]
    },
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL3 License",
        "Operating System :: POSIX :: Linux",
    ],
    
    install_requires=[
        'speech_recognition',
        'yaml-1.3'
    ],
    
    python_requires='>=3.6',

    include_package_data=True
)