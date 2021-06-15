import http.client as httplib
from ovest.database import crud
from ovest.emergencyHandler import NotifyEmergency as emr
import time
from ovest.gsm import interface as gsm
import datetime
from ovest.gbs import gpsLocation

class NotifyFallEmergency(emr.NotifyEmergency):
    def __init__(self, database, db_attr_fall, db_attr_timestamp, db_attr_lat, db_attr_long):
        self.db = database
        self.fall = db_attr_fall
        self.timestamp = db_attr_timestamp
        self.lat = db_attr_lat
        self.long = db_attr_long

    def notify_emergency_fallen(self):
        internet_connected = super().check_internet_connection()
        #timezone berlin
        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        if not internet_connected:
            self.db.update_child(self.fall, "Fall_Detected")
            self.db.update_child(self.timestamp, ts)
        else:
            # NO internet
            gsm.update_db_per_http(self.db.collection, self.db.user_document,
            self.fall, "Fall_Detected")
            gsm.update_db_per_http(self.db.collection, self.db.user_document,
            self.timestamp, ts)
            # get gps location
            vlat, vlong = gpsLocation.get_coordinate_location()
            gsm.update_db_per_http(self.db.collection, self.db.user_document,
            self.lat, vlat)
            gsm.update_db_per_http(self.db.collection, self.db.user_document,
            self.long, vlong)

    def notify_emergency_not_fallen(self):
        internet_connected = super().check_internet_connection()
        #timezone berlin
        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        if not internet_connected:
            self.db.update_child(self.fall, "NO_Fall_Detected")
            self.db.update_child(self.timestamp, ts)
        else:
            gsm.update_db_per_http(self.db.collection, self.db.user_document,
            self.fall, "NO_Fall_Detected")
            gsm.update_db_per_http(self.db.collection, self.db.user_document,
            self.timestamp, ts)
            # get gps location
            vlat, vlong = gpsLocation.get_coordinate_location()
            gsm.update_db_per_http(self.db.collection, self.db.user_document,
            self.lat, vlat)
            gsm.update_db_per_http(self.db.collection, self.db.user_document,
            self.long, vlong)
            