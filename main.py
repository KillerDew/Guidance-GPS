import haversineLerp
from time import sleep
from datatypes import GeoLocation
from inverse import vincentyinverse
from direct import vincentydirect
from enum import Enum
import math
from math import tan

radconversion = math.pi/180

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


#x = GeoLocation(51.96790250975882, -0.2273349836468697, 0)
#y = GeoLocation(51.9658401216410, -0.22791434079408648, 0)
#result = (vincentyinverse(x, y))

#result2 = vincentydirect(x, result[0], result[2]*0.5)
#print(result)

#print()
#print(result2)
  #--Works--




##INTERFACE

def inputs():
  
  flightype = input("Flight type [1: Direct, 2: Top down, 3: Pop Up]: ")

  if (flightype == "1"):
    midheight = float(input("Mid-height (m): "))
    maxclimb = float(input("Max climb angle (deg): "))
    launchstr = input("Launch point [lat, long, alt]: ")
    Launch = GeoLocation(0, 0, 0)
    Launch.Latitude = float(launchstr.split(",")[0])
    Launch.Longitude = float(launchstr.split(",")[1])
    Launch.ALtitude = float(launchstr.split(",")[2])

    targetstr = input("Target Point [lat, long, alt]: ")
    Target = GeoLocation(0, 0, 0)
    Target.Latitude = float(targetstr.split(",")[0])
    Target.Longitude = float(targetstr.split(",")[1])
    Target.ALtitude = float(targetstr.split(",")[2])

    inverseresult = vincentyinverse(Launch, Target)
    b_i = inverseresult[0]
    b_f = inverseresult[1]
    D_T = inverseresult[2]
    
    d_d = midheight/tan(maxclimb*radconversion)
    directresult = vincentydirect(Launch, b_i, d_d)
    MID_POINT = GeoLocation(directresult[0], directresult[1], Launch.ALtitude)
    print(MID_POINT)
  elif (flightype == "2"):
    midheight = float(input("Coast Height (m): "))
    maxclimb = float(input("Max climb angle (deg): "))
    maxdive = float(input("Max dive angle (deg): "))
    Launchstr = input("Launch point [lat, long, alt]: ")
    Launch = GeoLocation(0, 0, 0)
    Launch.Latitude = float(Launchstr.split(",")[0])
    Launch.Longitude = float(Launchstr.split(",")[1])
    Launch.ALtitude = float(Launchstr.split(",")[2])

    targetstr = input("Target point [lat, long, alt]: ")
    Target = GeoLocation(0, 0, 0)
    Target.Latitude = float(targetstr.split(",")[0])
    Target.Longitude = float(targetstr.split(",")[1])
    Target.ALtitude = float(targetstr.split(",")[2])

    inverseresult = vincentyinverse(Launch, Target)
    B_i = inverseresult[0]
    B_f = inverseresult[1]
    D_T = inverseresult[2]

    D_c = midheight/tan(maxclimb*radconversion)
    D_d = midheight*tan(maxdive*radconversion)

    directresult = vincentydirect(Launch, B_i, D_c)
    Coastpoint = GeoLocation(0, 0, 0)
    Coastpoint.Latitude = directresult[0]
    Coastpoint.Longitude = directresult[1]
    Coastpoint.ALtitude = Launch.ALtitude

    directresult = vincentydirect(Launch, B_i, D_T-D_d)
    DivePoint = GeoLocation(0, 0, 0)
    DivePoint.Latitude = directresult[0]
    DivePoint.Longitude = directresult[1]
    DivePoint.ALtitude = Target.ALtitude

    print()
    print(Coastpoint)
    print()
    print(DivePoint)
  elif(flightype =="3"):
    Popupheight = float(input("Pop up height (m): "))
    Maxclimb = float(input("max climb angle (deg): "))
    maxdive = float(input("Max dive angle (deg): "))
    launchstr = input("Launch Point [lat, long, alt]: ")
    Launch = GeoLocation(0, 0, 0)
    Launch.Latitude = float(launchstr.split(",")[0])
    Launch.Longitude = float(launchstr.split(",")[1])
    Launch.ALtitude = float(launchstr.split(",")[2])

    targstr = input("Target Point [lat, long, alt")
    Target = GeoLocation(0, 0, 0)
    Target.Latitude = float(targstr.split(",")[0])
    Target.Longitude = float(targstr.split(",")[1])
    Target.ALtitude = float(targstr.split(",")[2])

    ΔAltitude = Target.ALtitude - Launch.ALtitude

    inverse_result = vincentyinverse(Launch, Target)
    b_i = inverse_result[0]
    b_f = inverse_result[1]
    d_T = inverse_result[2]

    d_c = Popupheight/tan(Maxclimb*radconversion)
    d_d = Popupheight*tan(maxdive*radconversion)

    d_0 = d_T*(1-((d_d+d_c)/d_T))

    direct_result = vincentydirect(Launch, b_i, d_0)
    climb_point = GeoLocation(0, 0, 0)
    climb_point.Latitude = direct_result[0]
    climb_point.Longitude = direct_result[1]
    climb_point.Altitude = ΔAltitude*(d_0/d_T)

    direct_result = vincentydirect(climb_point, b_i, d_c)

    Dive_point = GeoLocation(0, 0, 0)
    Dive_point.Latitude = direct_result[0]
    Dive_point.Longitude = direct_result[1]
    Dive_point.Altitude = ΔAltitude*((d_0+d_c)/d_T)
    print()
    print(climb_point)
    print()
    print(Dive_point)
    #--Pop Up End--
    
    

    

inputs()


