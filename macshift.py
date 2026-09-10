#!/usr/bin/env python3 

import sys
import signal
import time

def def_handler(sig, frame):

    print(f"Getting out...")
    sys.exit(1);

signal.signal(signal.SIGINT, def_handler)

def change_mac():
    
    time.sleep(2)
    print("works")

def main():

    change_mac()

if __name__=='__main__':

    main()
