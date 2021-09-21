

import threading
from dataclasses import dataclass

import marvelmind_pylib as mpl

@dataclass
class Beacon:
    address: int

    x: float
    y: float
    z: float

    is_stationary: bool

class StoppableThread(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stopper = threading.Event()
    
    def stop(self):
        self._stopper.set()
    
    def stopped(self):
        return self._stopper.isSet()

class MarvelmindThread(StoppableThread):

    def __init__(self, *args, **kwargs):
        self.__tty_dev = kwargs['device']
        self.__verbose = kwargs['verbose']
        del kwargs['device']
        del kwargs['verbose']

        super(MarvelmindThread, self).__init__(*args, **kwargs)

        self.__dev = mpl.MarvelMindDevice(self.__tty_dev, self.__verbose)
        rescode = self.__dev.start()
        if not rescode:
            raise Exception("Error")
        
        self.__beacons = {}
    
    def execute(self):
        mobile_pos = self.__dev.getMobileBeaconsPosition()
        stationary_pos = self.__dev.getStationaryBeaconsPosition()

        for address, xyz in mobile_pos.items():
            current_beacon = Beacon(address,
                                    xyz[0], xyz[1], xyz[2],
                                    False)
            
            self.__beacons[address] = current_beacon

        for address, xyz in stationary_pos.items():
            current_beacon = Beacon(address,
                                    xyz[0], xyz[1], xyz[2],
                                    True)
            
            self.__beacons[address] = current_beacon
    
    def getBeacon(self, address):
        return self.__beacons[address] if address in self.__beacons else None
    
    def getAll(self):
        return self.__beacons

    def getStationaryBeacons(self):
        return [beacon for addr, beacon in self.__beacons.items() if beacon.is_stationary]
    
    def __str__(self):
        txt = ""
        for address, pos in self.__beacons.items():
            txt += str(pos) + "\n"
        return txt
    
    def close_device(self):
        self.__dev.close()
        del self.__dev

    def run(self):
        while True:
            if self.stopped():
                self.close_device()
                return
            self.execute()


def parse():
    import sys
    import argparse
    import re

    parser = argparse.ArgumentParser(description="Marvelmind console application")
    parser.add_argument('--usb', required=False, type=str, default="/dev/ttyACM0", help="Marvelmind device (default : /dev/ttyACM0) ")
    args = parser.parse_args()

    win2_patt = re.compile("COM\d+")
    unix_patt = re.compile("/dev/tty\w+")

    if win2_patt.match(args.usb) or unix_patt.match(args.usb):
        return args.usb, True
    
    return args.usb, False

def main():

    dev, stat = parse()
    if not stat:
        print(dev, " not recognized")
        return

    try:
        thread = MarvelmindThread(device=dev, verbose=True)
        thread.start()
    except Exception as ex:
        #thread.close_device()
        print(ex)
        return
    
    while True:
        try:
            cmd = input(">> ").strip().split(" ")
            cmd = [t for t in cmd if len(t)>0]
            if cmd[0] == "get" and len(cmd) == 2:
                
                if cmd[1] == "all":
                    print(thread)

                if cmd[1] == "stats":
                    for b in thread.getStationaryBeacons():
                        print(b)
                
                if cmd[1].isdigit():
                    addr = int(cmd[1])
                    beacon = thread.getBeacon(addr)
                    if beacon is not None:
                        print(beacon)
            
            if cmd[0] == "exit":
                break
        except KeyboardInterrupt:
            print("")
        except Exception as ex:
            print("Exception : ", ex)
            break
    
    thread.stop()
    thread.join()


if __name__=="__main__":
    main()