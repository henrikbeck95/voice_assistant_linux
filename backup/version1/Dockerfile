FROM ubuntu:21.04
MAINTAINER Henrik Beck <henrikbeck95@gmail.com>

#Update system
RUN apt update && \
	apt install -y tzdata software-properties-common && \
	add-apt-repository -y -u ppa:certbot/certbot && \
	apt install -y certbot

#Install essential softwares
RUN apt install -y bash-completion wget python3-pip #python3-all-dev doxygen

#Install Python-Pip libraries
RUN pip3 install python-dev-tools && \
	pip3 install pytest && \
	pip3 install pyttsx3 && \
	pip3 install wikipedia && \
	pip3 install SpeechRecognition && \
	pip3 install pywhatkit && \
	pip3 install numpy && \
	apt install -y python3-pyaudio

#Apply Vi customization
#echo "set ts=4 sw=4" >> /etc/virc

#Install Vim and LF terminal file manager
RUN \
	apt install -y vim && \
	wget https://github.com/gokcehan/lf/releases/download/r24/lf-linux-amd64.tar.gz && \
	tar -zxf ./lf-linux-amd64.tar.gz && \
	mv -v ./lf /bin/ && \
	rm -f ./lf-linux-amd64.tar.gz

#############################
#Version 0.2
#############################

#Install audio drivers
RUN apt install -y sox libsox-fmt-all alsa-firmware-loaders alsa-oss alsa-tools alsa-utils #alsa-base alsa-lib

#Copy the Voice Assistent for Linux files to container
COPY . /voice_assistent/

#Attribute the variables values
WORKDIR /voice_assistent/

ENV EDITOR=vim

#############################
#Version 0.3
#############################

#Virtual AI
#git clone https://github.com/Moiz-Ali-Moomin/Virtual_AI
RUN wget https://raw.githubusercontent.com/Moiz-Ali-Moomin/Virtual_AI/master/task1.py

#Voice control menu
#git clone https://github.com/Moiz-Ali-Moomin/voice-control-menu-python/
#wget -O https://raw.githubusercontent.com/Moiz-Ali-Moomin/voice-control-menu-python/main/task9.py

#Install audio drivers
#RUN apt install -y jackd1
#RUN apt install -y jackd1 libasound2 libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0

#CentOS 7 softwares
#RUN yum install sox libtool autoconf bison swig alsa-lib-devel pulseaudio-libs-devel make -y

#############################
#Version 1.0 - Running...
#############################

#Update Python-pip and all Python-Pip packages
#RUN pip3 install --upgrade pip && pip3 install --upgrade $(pip3 freeze | awk '{split($0, a, "=="); print a[1]}')

#Execute audio file (for testing audio device)
#CMD aplay a.wav #ALSA alsa-utils
#CMD play a.mp3 #Sox

#Execute Voice assistent
#CMD python3 -m speech_recognition
#CMD python3 /voice_assistent/src/__init__.py
#CMD python3 /voice_assistent/src/__init_short__.py

#Execute Voice assistent (developemnt mode)
#RUN pip install -e .
#RUN /home/$USER/.local/bin/pytest

#Docker run command
#docker run -it --rm --privileged=true --device=/dev/snd:/dev/snd myContainerName jackd -R -d alsa -d hw:1
