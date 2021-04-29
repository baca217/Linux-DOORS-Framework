#!/usr/bin/env python3
import sys
sys.path.append('tools')
sys.path.append('modules')
import sklearn_sims as sk
import module_loader as ml
import pathlib
import time

def main():
    classes = ml.class_builder()
    info = {"path" : str(pathlib.Path(__file__).parent.absolute())}
    voice = None
    commands = [
            "using youtube play the song slow dancing in the darkness"
             ]

    for i in commands:
        print(i)
        msg, func, mod = sk.compare_command(i, classes, info)
        run_results(msg, func, mod, classes, voice)

def run_results(msg, func, mod, classes, voice):
    print(msg)
    if func: #we got a func back
        if mod in classes.keys(): #classes funcs should manipulate themselves
            func(classes[mod])
        else:
            func()
        input("wait")

if __name__ == "__main__":
    main()
