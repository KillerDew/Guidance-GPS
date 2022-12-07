import math
import time
from datatypes import GeoLocation

earthrad = 6364.912*1000



def GetVector (x, y):
    b = y.ALtitude + earthrad
    c = x.ALtitude + earthrad

    b2 = b**2
    c2 = c**2
    bc2 = 2*b*c

    alpha = y.Longitude - x.Longitude
    alpha = alpha *(math.pi/180)
    
    outy = (b2 +c2 - bc2*math.cos(alpha))**0.5

    alpha = y.Latitude - x.Latitude
    alpha = alpha *(math.pi/180)
    
    outx = (b2+c2-bc2*math.cos(alpha))**0.5

    outz = b-c

    return GeoLocation(outx, outy, outz)

def Lerp(a, b, x):
    new = GeoLocation.__add__(a, b)
    return new.__times__(x)





#in1 = input("Launch coordinate [lat, long, alt]: ")
#launch = GeoLocation(float(in1.split(", ")[0]), float(in1.split(", ")[1]), int(in1.split(", ")[2]))
#time.sleep(0.5)
#in2 = input("Target coordinate [lat, long, alt]: ")
#targ = GeoLocation(float(in2.split(", ")[0]), float(in2.split(", ")[1]), int(in2.split(", ")[2]))
#time.sleep(0.5)
#vector = GetVector(launch, targ)
#midvector = Lerp(GeoLocation(0, 0, launch.ALtitude), vector, 0.5)
#output = launch.AddMetres(midvector)
#print("Calculating")
#time.sleep(1)
#print (vector)
#print (output)
#print ((vector.Latitude**2+vector.Longitude**2+vector.ALtitude**2)**0.5)
