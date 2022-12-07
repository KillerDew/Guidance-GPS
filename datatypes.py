import math

earthrad = 6.364912E6

class GeoLocation:
    Latitude = 0.0000
    Longitude = 0.0000
    ALtitude = 0.0000
    def __init__(self, lat, longi, alt):
        self.Latitude = lat
        self.Longitude = longi
        self.ALtitude = alt

    def __str__(self):
        string = "{latitude} {longitude} {alti}".format(latitude=self.Latitude, longitude = self.Longitude, alti = self.ALtitude)
        return string

    def __add__(a, b):
        return GeoLocation((a.Latitude + b.Latitude), (a.Longitude+b.Longitude), (a.ALtitude+b.Latitude))
    def __times__(self, x):
        return GeoLocation((self.Latitude*x), (self.Longitude*x), (self.ALtitude*x))

    def __minus__(self, y):
        new = GeoLocation(self.Latitude-y.Latitude, self.Longitude-y.Longitude, self.ALtitude-y.Altitude)
        return new

    def AddMetres(self, x):
        new = GeoLocation(0, 0, 0)
        new.Latitude = self.Latitude+(180/math.pi)*(x.Longitude/earthrad)
        new.Longitude = self.Longitude+(180/math.pi)*(x.Latitude/earthrad)/math.cos(self.Latitude)
        new.ALtitude = self.ALtitude
        return new
