import http.client as httplib
from ovest.database import crud
import time
import datetime
from ovest.gbs import gpsLocation
from ovest.emergencyHandler import internet as inter


class NotifyFallEmergency:
    def __init__(self, gsm, database, db_attr_fall, db_attr_timestamp):
        self.db = database
        self.fall = db_attr_fall
        self.timestamp = db_attr_timestamp
        self.gsm = gsm

    def notify_emergency_fallen(self):
        internet_connected = inter.check_internet_connection()
        # timezone berlin
        ts = datetime.datetime.fromtimestamp(
            time.time()).strftime('%Y-%m-%d %H:%M:%S')
        if internet_connected:
            self.db.update_child(self.fall, "Fall Detected")
            self.db.update_child(self.timestamp, ts)
        else:
            # NO internet
            print("@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@##@#@#@#@#")
            self.gsm.update_db_per_http(self.db.collection, self.db.user_document,
                                   self.fall, "Fall%20Detected")
            self.gsm.update_db_per_http(self.db.collection, self.db.user_document,
                                   self.timestamp, ts)

    def notify_emergency_not_fallen(self):
        internet_connected = inter.check_internet_connection()
        # timezone berlin
        ts = datetime.datetime.fromtimestamp(
            time.time()).strftime('%Y-%m-%d %H:%M:%S')
        if internet_connected:
            self.db.update_child(self.fall, 0)
            self.db.update_child(self.timestamp, ts)
        else:
            self.gsm.update_db_per_http(self.db.collection, self.db.user_document,
                                   self.fall, "NO%20Fall%20Detected")
            self.gsm.update_db_per_http(self.db.collection, self.db.user_document,
                                   self.timestamp, ts)
