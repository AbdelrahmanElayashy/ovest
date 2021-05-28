import busio
import board
import adafruit_gps
from ovest.alert.gbs import GpsModule
from time import monotonic as timer
import time


def get_coordinate_location():
    i2c = board.I2C()
    gps = adafruit_gps.GPS_GtopI2C(i2c, debug=False)
    gps101 = GpsModule.Gps101(gps)

    deadline = timer() + 600  # run this for 10 min.
    while timer() < deadline:
        try:
            lan, lat = gps101.get_coordination()
            return lan, lat
        except Exception as e:
            time.sleep(2)
            continue
