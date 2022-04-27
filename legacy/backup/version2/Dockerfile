FROM registry.fedoraproject.org/fedora-minimal
MAINTAINER Henrik Beck <henrikbeck95@gmail.com>

#Install Python 3.6, Pip 3 and Anaconda
RUN microdnf install -y bzip2 --nodocs --setopt install_weak_deps=0 && \
	microdnf install -y python36 --nodocs --setopt install_weak_deps=0 && \
	curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh && \
	bash /tmp/miniconda.sh -bfp /usr/local/ && \
	rm -fr /tmp/miniconda.sh && \
	conda install -y python=3.6 && \
	conda update conda && \
	conda clean --all --yes && \
	rpm -e --nodeps curl bzip2 && \
	microdnf clean all

#Install Python packages
RUN \
	conda install -c conda-forge wikipedia && \
	conda install -c conda-forge speechrecognition && \
	conda install -c anaconda pyaudio && \
	conda install -c anaconda portaudio && \
	pip install pyttsx3==2.71 && \
	pip install wolframalpha
	#conda install -c anaconda wolframalpha #&& \
	#conda install -c wolframresearch wolframclient && \

#Install terminal editor
RUN microdnf install -y vim --nodocs --setopt install_weak_deps=0

WORKDIR /val/

#Copy Virtual Assistent for Linux (VAL) files
COPY . /val/
