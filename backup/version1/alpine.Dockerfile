FROM pip-alpine
MAINTAINER Henrik Beck <henrikbeck95@gmail.com>

ARG USER=default
ENV HOME /home/$USER

RUN apk update && apk add --update sudo

RUN adduser -D $USER && \
	echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER && \
	chmod 0440 /etc/sudoers.d/$USER

USER $USER

#Install Python-Pip libraries
RUN pip3 install --upgrade pip && \
	pip3 install pytest && \
	pip3 install pyttsx3 && \
	pip3 install wikipedia

#Copy the Voice Assistent for Linux files to container
COPY . /home/$USER/voice_assistent/

#Attribute the variables values
WORKDIR $HOME/voice_assistent/

#Others
#RUN pip install pywhatkit
#RUN pip install speechRecognition
	#&& \ #SpeechRecognition
	#pip install pyaudio #PyAudio

#Execute Voice assistent
#RUN pip install -e .
#RUN /home/$USER/.local/bin/pytest
#CMD python3 /home/$USER/voice_assistent/src/__init__.py

#RUN apk add alsa-lib-devel pulseaudio-libs-devel portaudio-devel
#sox libtool autoconf bison swig doxygen
