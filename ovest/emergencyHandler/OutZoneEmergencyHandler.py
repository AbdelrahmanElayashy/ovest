from ovest.gbs import gpsLocation
from ovest.emergencyHandler import internet as inter
import schedule
import time


class OutZoneEmergencyHandler:
    def __init__(self, notify_emergency):
        self.notify = notify_emergency

    def run_out_zone_handler(self):
        schedule.every(5).minutes.do(self.notify.notify_location_out_zone)
        while True:
            print("checking OUT ZONE")
            if not inter.check_internet_connection():
                schedule.run_all()
                time.sleep(5)
            time.sleep(2)
