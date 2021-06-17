import http.client as httplib
from ovest.database import crud
import time
import datetime
from ovest.gbs import gpsLocation


class NotifyOutZoneEmergency():
    def __init__(self, gsm, database, db_attr_timestamp, db_attr_lat, db_attr_long):
        self.db = database
        self.timestamp = db_attr_timestamp
        self.lat = db_attr_lat
        self.long = db_attr_long
        self.gsm = gsm

    def notify_location_out_zone(self):
        
        ts = datetime.datetime.fromtimestamp(time.time()).strftime(
            '%Y-%m-%d %H:%M:%S')  # timezone berlin
        # get gps location
        vlat, vlong = gpsLocation.get_coordinate_location()
        self.gsm.update_db_per_http(self.db.collection, self.db.user_document,
                               self.lat, vlat)
        self.gsm.update_db_per_http(self.db.collection, self.db.user_document,
                               self.long, vlong)
        self.gsm.update_db_per_http(self.db.collection, self.db.user_document,
                               self.timestamp, ts)
