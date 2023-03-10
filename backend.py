import json_parser
import config
import subprocess

from threading import Thread

import queue

import discordbackend

import camera

import datetime

backends = ["discord"]

inqueue = queue.Queue()
outqueue = queue.Queue()

def init_backend():
    backend = config.MessageBackend
    if not (backend in backends):
        print("Error: Unknown backend! Defaulting to default Discord backend!")
        print("given:" + config.MessageBackend)
        backend = "discord"
        config.MessageBackend = "discord";
    
    if(backend == "discord"):
        print("Backend callback: Initializing discord...")
        discordbackend.init_discord()
    else:
        print("Backend not implemented!")
    # Template, can put more backends here

    thread = Thread(target=message_driver)
    thread.start()
    send(["LoggingChannel", "Text", "OpenCam started at " + str(datetime.datetime.now())])

def send(t):
    outqueue.put(t)

def message_driver():
    while(True):
        message = inqueue.get(block=True)
        if(message.content == "df"):
            res = subprocess.run(['df', '-h'], stdout=subprocess.PIPE)
            send(["InputChannel", "text", "```"+str(res.stdout)+"```"])
        if(message.content == 'getmode'):
            send(["InputChannel", "Text", config.mode])
        if message.content.startswith("setmode"):
            s = message.content[7:].strip()
            if(s in ["auto", "enable", "disable"]):
                config.mode = s
                send(["InputChannel", "Text", "Mode set to " + config.mode])
            else:
                send(["InputChannel", "Text", "Invalid! Valid options: auto enable disable"])
        if message.content == 'getpic':
            print("Getting picture")
            send(["InputChannel", "image", camera.getpic()])
        if message.content == 'ping':
            send(["InputChannel", "text", "pong"])
                
            
