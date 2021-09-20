
#include <iostream>

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#ifdef WIN32
#include <windows.h>
#else
#include <fcntl.h>
#include <unistd.h>
#include <signal.h>
#include <semaphore.h>
#include <time.h>
#endif // WIN32

#include <vector>
#include <map>

extern "C" {
    #include "marvelmind.h"
}

using namespace std;

class MarvelMindDevice {
    public:
        MarvelMindDevice(string serialPort, bool verbose)
        {
            hedge__ = createMarvelmindHedge ();
            if (hedge__ == NULL)
            {
                puts ("Error: Unable to create MarvelmindHedge");
                exit(1);
            }
            char * new_serial_port = (char *) malloc(sizeof(char)*(serialPort.length() + 1));

            strcpy(new_serial_port, serialPort.c_str());

            hedge__->ttyFileName = new_serial_port;
            hedge__->verbose = verbose;

            // cout << "Serial port : " << serialPort << endl;
            // cout << "Serial port OUT : " << hedge__->ttyFileName << endl;
        };
        
        void start();
        void close();

        ~MarvelMindDevice();

        map<int, vector<double>> getMobileBeaconsPosition();
        map<int, vector<double>> getStationaryBeaconsPosition();

        // vector<double> getPosition();
        // vector<vector<double>> getStationaryBeacons();
        
    private:
        struct MarvelmindHedge * hedge__;
};

void MarvelMindDevice::start()
{
    cout << "Serial port start" << hedge__->ttyFileName;
    startMarvelmindHedge(hedge__);
}

void MarvelMindDevice::close()
{
    stopMarvelmindHedge (hedge__);
    destroyMarvelmindHedge (hedge__);
    hedge__ = NULL;
}

MarvelMindDevice::~MarvelMindDevice()
{
    if (hedge__ != NULL) close();
}


map<int, vector<double>> MarvelMindDevice::getMobileBeaconsPosition()
{
    map<int, vector<double>> result;

    uint8_t i, j;
    double xm, ym, zm;

    cout << "";

    if (hedge__->haveNewValues_)
    {
        
        struct PositionValue* poses;
        
        int resultSize = 0;
        poses = getMobilePositionFromModem(hedge__, true, &resultSize);
        
        
        if(poses == NULL) {
            return result;
        }
        
        for (size_t i = 0; i < resultSize; i++)
        {   
            PositionValue position = poses[i];
            uint8_t address = position.address;
            double xm, ym, zm;

            xm = ((double) position.x)/1000.0;
            ym = ((double) position.y)/1000.0;
            zm = ((double) position.z)/1000.0;

            vector<double> pos;
            pos.push_back(xm);
            pos.push_back(ym);
            pos.push_back(zm);

            result[address] = pos;
        }
    }

    return result;
}

map<int, vector<double>> MarvelMindDevice::getStationaryBeaconsPosition()
{
    map<int, vector<double>> result;
    // printStationaryBeaconsPositionsFromMarvelmindHedge(hedge__, true);

    cout << "";

    struct StationaryBeaconsPositions positions;
    getStationaryBeaconsPositionsFromMarvelmindHedge(hedge__, &positions);
    if(positions.updated) {
        for (size_t i = 0; i < positions.numBeacons; i++)
        {
            StationaryBeaconPosition stat_pos = positions.beacons[i];
            int addr = stat_pos.address;
            double xm = ((double) stat_pos.x)/1000.0;
            double ym = ((double) stat_pos.y)/1000.0;
            double zm = ((double) stat_pos.z)/1000.0;

            // cout << "XYZ " << xm << " " << ym << " " << zm << endl;
            
            vector<double> pos;
            pos.push_back(xm);
            pos.push_back(ym);
            pos.push_back(zm);

            result[addr] = pos;
        }
    }

    return result;
}
