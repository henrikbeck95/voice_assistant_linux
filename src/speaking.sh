#!/usr/bin/env sh

#############################
#Credits
#############################
#Author: Henrik Beck
#E-mail: henrikbeck95@gmail.com
#License: GPL3
#Version: 0.0.1
#############################

##############################
#Import Shell Script Library
##############################

if [[ -f /usr/local/bin/shell-script-library ]]; then
    source /usr/local/bin/shell-script-library
elif [[ -f ./src/libs/shell-script-library ]]; then
    source ./src/libs/shell-script-library
else
    echo -e "Shell Script Library could not be loaded"
fi

##############################
#Functions
##############################

voice_assistant_requirements(){
    #Native packages
    sudo pacman -S festival festival-english festival-us

    sudo pacman -S python-pyaudio
    #paru -S python-pyttsx3

    #Python packages
    pip3 install SpeechRecognition
    pip3 install yaml-1.3
}

voice_assistant_speech_text_festival(){
    local VALUE_CONTANT=$1

    case $(utils_check_if_software_is_installed "festival") in
        "false") display_message_error_simple "Festival is not installed" ;;
        #"true") festival <<< '(SayText "Say anything")' ;;
        #"true") festival <<< "(SayText \"$VALUE_CONTANT\")" ;;
        "true") echo "(SayText \"$VALUE_CONTANT\")" | festival ;;
    esac
}

voice_assistant_speech_text_val(){
    #voice_assistant_speech_text_val "Say something"
    
    local VALUE_CONTANT=$@

    notify-send "$VALUE_CONTANT"
    voice_assistant_speech_text_festival "$VALUE_CONTANT"
}