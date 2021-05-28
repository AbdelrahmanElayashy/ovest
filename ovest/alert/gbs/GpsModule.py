import time
import board
import busio
import adafruit_gps

class Gps101:
    last_print = None
    current = None
    gps = None

    def __init__(self, gps): 
        self.gps = gps
        self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        self.gps.send_command(b"PMTK220, 1000")

    def get_coordination(self):
        self.last_print = time.monotonic()
        
        self.gps.update()

        self.current = time.monotonic()

        if self.current - self.last_print >= 1.0:
            self.last_print = self.current
        
        if (not self.gps.has_fix):
            raise Exception("Waiting for fix")

        else:
            return self.gps.latitude, self.gps.longitude
