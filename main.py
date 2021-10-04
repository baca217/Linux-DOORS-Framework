#!/usr/bin/env python3 
import sys
sys.path.append('tools')
sys.path.append('modules')

import open_mic as om
import sklearn_sims as sk
import voice_synth as vs
import module_loader as ml
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
                
if __name__ == "__main__":
        main()