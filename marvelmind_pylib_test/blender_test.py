

import threading
from dataclasses import dataclass

#import sys
#sys.path.append("F:\\Universidad\\TFM\\MarvelmindLib\\marvelmind_pylib_test\\")
import marvelmind_pylib as mpl

@dataclass
class Beacon:
    address: int
    timestamp: float

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
        self.__dev.start()

        self.__beacons = {}

    def execute(self):
        mobile_pos = self.__dev.getMobileBeaconsPosition()
        stationary_pos = self.__dev.getStationaryBeaconsPosition()

        for address, xyz in mobile_pos.items():
            current_beacon = Beacon(address,
                                    xyz[3],
                                    xyz[0], xyz[1], xyz[2],
                                    False)

            self.__beacons[address] = current_beacon

        for address, xyz in stationary_pos.items():
            current_beacon = Beacon(address,
                                    0,
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


from threading import Lock

class Singleton(type):
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class MarvelmindHandler(metaclass=Singleton):

    def __init__(self):
        self.__thread = None

    def start(self, device, verbose):
        if self.__thread is None:
            self.dev = device
            self.__thread = MarvelmindThread(device=device, verbose=verbose)
            self.__thread.start()

    def stop(self):
        if self.__thread is not None and not self.__thread.stopped():
            self.__thread.stop()
            self.__thread.join()

            self.__thread = None
            print("Stopped")
        else:
            raise Exception("Thread is not started")

    def getBeacon(self, address):
        if self.__thread is not None:
            return self.__thread.getBeacon(address=address)
        else:
            raise Exception("Thread is not started")

    def getAll(self):
        if self.__thread is not None:
            return self.__thread.getAll()
        else:
            raise Exception("Thread is not started")

    def getStationaryBeacons(self):
        if self.__thread is not None:
            return self.__thread.getStationaryBeacons()
        else:
            raise Exception("Thread is not started")

    def isRunning(self):
        return self.__thread is not None


def main():

    dev = "COM6"

    import serial
    try:
        serial_port = serial.Serial(dev)
        if serial_port.is_open:
            serial_port.close()
            del serial_port
    except:
        print(f"Serial port {dev} not available")
        return


    try:
        MarvelmindHandler().start(dev, True)
    except Exception as ex:
        print(ex)
        return

    import time
    time.sleep(5)

    MarvelmindHandler().stop()


if __name__=="__main__":
    main()
