#!/usr/bin/env sh

#############################
#Description
#############################
#
#References
#- [Remover ruído do microfone no Linux](https://www.youtube.com/watch?v=kG0FjnNEibk)
#
#Required softwares
#1. Sox (recording)
#1. MPV (playing)
#1. Pactl (remove noise sound effect)
#############################

#############################
#Variables
#############################

AUX1=$1
AUX2=$2
#AUX3=$3

SOUND_PATH="/tmp"
SOUND_NAME="$AUX2.wav"

MESSAGE_HELP="\t\tTerminal voice recorder\n\t\t-----------------------\n
[Parameter options]
-h\t--help\t-?\t\tDisplay this help message
-e\t--edit\t\t\tEdit this script file
-t\t--trash\t\t\tMoving the recorded audio to the trash
-f\t--filter-noise\t\tRemove microphone noise audio
-p\t--play\t\t\tPlay recorded audio
-r\t--recorder\t\tRecorder audio

[Variables contents]
SOUND_NAME=$AUX2

[Example]
$0 <--parameter> $SOUND_NAME
"

MESSAGE_ERROR="Invalid option for $0!\n$MESSAGE_HELP"

#############################
#Functions
#############################

filter_noise(){
	#My micrphone name: Analog tereo Duplex

	pactl load-module module-echo-cancel aec_method=webrtc sink_properties=device.description="Noise_Reduction" aec_args="analog_gain_control=0\ digital_gain_control=0"

	#pactl load-module module-echo-cancel aec_method=speex sink_properties=device.description="Noise_Reduction" aec_args="analog_gain_control=0\ digital_gain_control=0"
}

sound_play(){
	#mpv $SOUND_PATH/$SOUND_NAME
	aplay $SOUND_PATH/$SOUND_NAME
}

sound_recorder(){
	#Record audio from 0 to 10 seconds
	sox -b 32 -e unsigned-integer -r 96k -c 2 -d --clobber --buffer $((96000*2*10)) $SOUND_PATH/$SOUND_NAME trim 0 10
}

sound_trash(){
	#rm -f $SOUND_PATH/$SOUND_NAME
	mv $SOUND_PATH/$SOUND_NAME $HOME/.local/share/Trash/
}

#############################
#Calling the functions
#############################

case $AUX1 in
	"" | "-h" | "--help" | "-?") echo -e "$MESSAGE_HELP" ;;
	"-e" | "--edit") $EDITOR $0 ;;
	"-t" | "--trash") sound_trash ;;
	"-f" | "--filter-noise") filter_noise ;;
	"-p" | "--play") sound_play ;;
	"-r" | "--recorder") sound_recorder ;;
	*) echo -e "$MESSAGE_ERROR" ;;
esac
