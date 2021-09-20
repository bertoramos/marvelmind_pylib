
#include <iostream>
#include <unistd.h>
#include <cstdlib>
#include <signal.h>

#include <map>
#include <vector>
#include <map>

#include "../marvelmind_device.hpp"

using namespace std;

MarvelMindDevice* dev;

void signal_callback_handler(int signum)
{
    dev->close();
    cout << "close" << endl;

    exit(signum);
}

int main()
{
    dev = new MarvelMindDevice("/dev/ttyACM0", true);
    dev->start();

    signal(SIGINT, signal_callback_handler);

    while(true)
    {
        map<int, vector<double>> pos_mobile = dev->getMobileBeaconsPosition();

        for(const auto& x : pos_mobile)
        {
            cout << x.first << " : " << endl;
            for (size_t i = 0; i < x.second.size(); i++) printf("%0.4f ", x.second[i]);
            
            cout << endl;
            
        }

        map<int, vector<double>> stat_position = dev->getStationaryBeaconsPosition();

        for(const auto& x : stat_position)
        {
            cout << x.first << " : " << endl;
            for (size_t i = 0; i < x.second.size(); i++) printf("%0.4f ", x.second[i]);
            
            cout << endl;
            
        }
        
    }

    return 0;
    
}
