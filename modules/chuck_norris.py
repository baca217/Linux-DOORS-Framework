#!/usr/bin/env python3

import requests

def comman_handler(sentence, info):
    msg = sentence + " is not a known command"
    func = None
    comms, ident = commands()
    if sentence in comms[0]:
        msg = getTime()
    return msg, func 

def commands():
    comms = [
        [
            "tell me a chuck norris joke"
        ]
    ]

    ident = [
        "cosine"
    ]
    return comms, ident

def getJoke():
    res = requests.get("https://api.chucknorris.io/jokes/random")
    dic = res.json()
    joke = "The joke is: " + dic["value"]
    return joke 

def main():
    print(getJoke())

if __name__ == "__main__":
    main()