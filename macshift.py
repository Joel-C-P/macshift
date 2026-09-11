#!/usr/bin/env python3 

import sys
import signal
import time
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="Change MAC address")
    parser.add_argument("-m", "--mac", dest= "mac_address", required=True, help= "Ex: -m xx:xx:xx:xx:xx:xx")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Ex: -i eth0|ens34")

    options = parser.parse_args()

    return options.mac_address, options.interface

def def_handler(sig, frame):

    print(f"Getting out...")
    sys.exit(1);

signal.signal(signal.SIGINT, def_handler)


def change_mac():
    
    print()
def main():

    change_mac()
    
    mac_address, interface = get_arguments()

    print(mac_address)
    print(interface)
if __name__=='__main__':

    main()
