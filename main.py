#!/usr/bin/env python3 
import sys
sys.path.append('tools')
sys.path.append('modules')

import open_mic as om
import sklearn_sims as sk
#import modules.serial_comm as serial_comm
import voice_synth as vs
import module_loader as ml
from tests.main_tests.main_test import run_tests
import os #for recording, temporary usage
import time #for testing
from pygame import mixer
from parse import *
import socket
import time
import pathlib

def main():
    voice = vs.VoiceSynth()
    decoder = om.Decoder()
    classes = ml.class_builder()
    info = {"path" : str(pathlib.Path(__file__).parent.absolute())}
    os.system("clear") #clearing out text from vosk intialization

    while True:
        sent = decoder.run()
        msg, func, mod = sk.compare_command(sent, classes, info)
        run_results(msg, func, mod, classes, voice)

def run_results(msg, func, mod, classes, voice):
    print(msg)
    if func: #we got a func back
        if mod in classes.keys(): #classes funcs should manipulate themselves
            func(classes[mod])
        else:
            func()

def local(): #function for recording and testing locally
    rec_com = [ #commands for recording audio
        "echo \"recording for 10 seconds\"",
        "arecord -t wav -D \"hw:2,0\" -d 10 -f S16_LE -r 48000 {}/temp/temp.wav".format(info["path"]),
        "ffmpeg -i {}/temp/temp.wav -isr 48000 -ar 8000 {}/temp/downSamp.wav".format(info["path"],info["path"]),
        "rm {}/temp/temp.wav".format(info["path"]),
        "clear",
        "echo \"done recording\"",
        ]

    try: #removing original recording file if it exists
        os.system("rm downSamp.wav")
    except:
        print(end = "")
    for i in rec_com:
        os.system(i)
                
if __name__ == "__main__":
        main()
