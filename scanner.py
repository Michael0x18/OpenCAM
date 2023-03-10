import json_parser
import config
import subprocess
from threading import Thread
import bluetooth
import time

# will use bluetoothctl scan on in order to find devices

import json_parser
import backend

verified_devices = dict()
found_devices = list()


proc = None

def go():
    global verified_devices
    verified_devices = json_parser.load_config("config/whitelist.json")
    t = Thread(target=mainloop)
    t.start()
    
def mainloop():
    print('KEYS ARE HERE!!!!!!!!!')
    print(verified_devices.keys())
    while True:
        print("Running bluetooth loop")
        
        nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True,
                                            flush_cache=True, lookup_class=False)

        a = list()
        for addr, name in nearby_devices:
            a.append(str(addr))
        for i in a:
            print(i)
            print(type(i))
            print(i in verified_devices)
            found = False;
            for j in verified_devices.keys():
                if( str(i) == str(j)):
                    found = True
            if( found ):
                print("!!! "+i)
                if( not (i in found_devices)):
                    backend.send(["LoggingChannel", "Text", i+" - "+verified_devices[i] + " has connected"]);
                    found_devices.append(i)
        for i in found_devices:
            if( not (i in a)):
                backend.send(["LoggingChannel", "Text", i + " - " + verified_devices[i]+ " has disconnected"]);
                found_devices.remove(i)
        time.sleep(20)
