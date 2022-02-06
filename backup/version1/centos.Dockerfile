#Based on CentOS 7
FROM binkybong/speech-recognition
MAINTAINER Henrik Beck <henrikbeck95@gmail.com>

#RUN yum install epel-release -y && yum clean all && yum update -y

#RUN yum install portaudio-devel python34-pip mlocate bash-completion git wget sox libtool autoconf bison swig python34-devel python34-numpy python34-scipy python-devel doxygen alsa-lib-devel pulseaudio-libs-devel make -y

#Apply Vi customization and install LF terminal file manager
RUN \
	echo -e "set ts=4 sw=4" >> /etc/virc && \
	wget https://github.com/gokcehan/lf/releases/download/r24/lf-linux-amd64.tar.gz && \
	tar -zxf ./lf-linux-amd64.tar.gz && \
	mv -v ./lf /bin/ && \
	rm -f ./lf-linux-amd64.tar.gz

#Install Python-Pip libraries
#RUN pip3 install --upgrade pip
RUN pip3 install pytest && \
	pip3 install pyttsx3 && \
	pip3 install wikipedia

#RUN pip3 install Pillow
#RUN pip3 install pywhatkit

#Others
#RUN pip3 install SpeechRecognition
#RUN pip3 install PyAudio

#Update all Python-Pip packages
#RUN pip3 install --upgrade $(pip3 freeze | awk '{split($0, a, "=="); print a[1]}')

#Attribute the variables values
#WORKDIR /voice_assistent/

#Copy the Voice Assistent for Linux files to container
#COPY . /voice_assistent/

#Execute Voice assistent
#RUN pip install -e .
#RUN /home/$USER/.local/bin/pytest

#CMD python3 /home/$USER/voice_assistent/src/__init__.py
#CMD python3 -m speech_recognition
#CMD aplay ...
