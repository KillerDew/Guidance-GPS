import haversineLerp
from time import sleep
from datatypes import GeoLocation
from inverse import vincentyinverse
from direct import vincentydirect
from enum import Enum

class FLIGHTTYPE(Enum):
  Direct = 1
  Top_Down = 2
  Pop_Up = 3
  Custom = 4

#print(VincentySolution.Bearing_Dist((GeoLocation(51.967257920383155, -0.22752416320145133, 98)), (GeoLocation(51.96683486806281, -0.22743296809494498, 95)))) #not working



#x = GeoLocation(0, 0, 0)
#y = GeoLocation (0, 0, 0)
#in1 = input("point 1: [lat, long, alt]")
#x.Latitude = float(in1.split(",")[0])
#x.Longitude = float(in1.split(",")[1])
#x.ALtitude = float(in1.split(",")[2])

#in2 = input("target: [lat, long, alt]")
#x.Latitude = float(in2.split(",")[0])
#x.Longitude = float(in2.split(",")[1])
#x.ALtitude = float(in2.split(",")[2])
#percent = float(input("midpoint percent:"))

#inverseresult = vincentysoultion2.vincentyinverse(x.Latitude, x.Longitude, #y.Latitude, y.Longitude)
#print (inverseresult)
#dist = inverseresult[2]
#initial = inverseresult[0]
#final = inverseresult[1]

#midpoint = vincentysoultion2.vincentydirect(x.Latitude, x.Longitude, initial, #dist*percent)

#print(midpoint)
#print (dist)
# FIX


x = GeoLocation(51.96790250975882, -0.2273349836468697, 0)
y = GeoLocation(51.9658401216410, -0.22791434079408648, 0)
result = (vincentyinverse(x, y))

result2 = vincentydirect(x, result[0], result[2]*0.5)
#print(result)

print()
print(result2)
  #--Works--




##INTERFACE

def inputs():
  pass
  #Fligh_type = FLIGHTTYPE(input("Flight Type [Direct, Top_Down, Pop_Up, Custom]: "))
  #print (Fligh_type)









inputs()


