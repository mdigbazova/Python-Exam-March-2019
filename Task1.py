#Python#Fund#Test

import math
width = float(input())
depth = float(input())
height = float(input())

volTruck = width*depth*height
numBar = int(input())
count_of_barrels = 0
for i in range(numBar):
    radBarr = float(input())
    heBarr = float(input())
    volBarrel = math.pi * radBarr * radBarr * heBarr
    remainTruckVol = volTruck - volBarrel
    if remainTruckVol < 0:
        print (f"Truck is full. {count_of_barrels} on board!")
        break
    else:
        volTruck = remainTruckVol
        count_of_barrels += 1

volume_of_truck = remainTruckVol
if count_of_barrels == numBar and remainTruckVol >= 0:
    print(f"All barrels on board. Capacity left - {abs(volume_of_truck):.2f}.")
