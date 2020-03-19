# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:18:46 2020

@author: Toshiba
"""

import Phygital as PyBot
import time

import PhygitalVehicleClass as x
Count=0


PyBot.init('COM7')
Vehicle=x.Vehicle
time.sleep(1)

while True:
    try:
        if PyBot.dRead(1) ==0:
            Count=Count+1
            print("Count = "+ str( Count))
            time.sleep(1.5)
            
        if PyBot.dRead(2)==0:     
            while Count>0:
                Vehicle.sharp_left(Vehicle,170,1)
                time.sleep(1)
                Count=Count-1
    except:
        if KeyboardInterrupt:
            PyBot.close()
            break
print("Closing")