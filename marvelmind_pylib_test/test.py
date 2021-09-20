
import marvelmind_pylib

dev = marvelmind_pylib.MarvelMindDevice("/dev/ttyACM1", True)
dev.start()

while True:
    try:
        mob_pos = dev.getMobileBeaconsPosition()
        stat_pos = dev.getStationaryBeaconsPosition()

        if len(mob_pos) > 0:
            print(mob_pos)
        if len(stat_pos) > 0:
            pass #print(stat_pos)
    except KeyboardInterrupt:
        break

dev.close()
