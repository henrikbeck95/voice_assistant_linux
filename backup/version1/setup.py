from setuptools import setup

#Recompile the README.md to PyPi PKGINFO
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
        name='VAL',
        version='0.0.1',
        description='Say hello to VAL!',
        author='Henrik Beck',
        author_email='henrikbeck95@gmail.com',
        license='MIT',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='https://github.com/henrikbeck95/voice_assistent',

        #py_modules=[""],
        #py_modules=["comando_voz_usuario"],
        #py_modules=["./src/__init__.py"],
        py_modules=[""],
        package_dir={'': 'src'},

        classifiers=[
            "Programming Language :: Python :: 3", 
            #"Programming Language :: Python :: 3.6", 
            "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)", 
            #"Operating System :: OS Independent", 
            "Operating System :: POSIX :: Linux", 
        ],

        #Python version
        python_requires='<=3.6',

        #Dependencies libraries (PyTest)
        install_requires = [
            "speechRecognition ~= 3.8.1",
            "pyttsx3 ~= 2.90",
            "wikipedia ~= 1.4.0",
            "PyAudio ~= 0.2.11", #For Python version > 3.6 this library must be installed manually
            "pywhatkit ~= 5.0",
        ],
        
        #Development dependencies libraries (PyTest)
        extra_require = {
            "dev": [
                "pytest>=3.7",
            ]
        }
)
