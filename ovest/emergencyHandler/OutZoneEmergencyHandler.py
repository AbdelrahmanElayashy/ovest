from ovest.gbs import gpsLocation
from ovest.emergencyHandler import internet as inter


class OutZoneEmergencyHandler:
    def __init__(self, notify_emergency):
        self.notify = notify_emergency

    def run_out_zone_handler(self):
        while True:
            if not inter.check_internet_connection():
                self.notify.notify_location_out_zone()
            sleep(500)
