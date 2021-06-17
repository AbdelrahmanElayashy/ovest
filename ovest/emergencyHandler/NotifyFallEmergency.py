import http.client as httplib
from ovest.database import crud
import time
from ovest.gsm import interface as gsm
import datetime
from ovest.gbs import gpsLocation
from ovest.emergencyHandler import internet as inter


class NotifyFallEmergency:
    def __init__(self, database, db_attr_fall, db_attr_timestamp):
        self.db = database
        self.fall = db_attr_fall
        self.timestamp = db_attr_timestamp


    def notify_emergency_fallen(self):
        internet_connected = inter.check_internet_connection()
        # timezone berlin
        ts = datetime.datetime.fromtimestamp(
            time.time()).strftime('%Y-%m-%d %H:%M:%S')
        if internet_connected:
            self.db.update_child(self.fall, "Fall_Detected")
            self.db.update_child(self.timestamp, ts)
        else:
            # NO internet
            gsm.update_db_per_http(self.db.collection, self.db.user_document,
                                   self.fall, "Fall_Detected")
            gsm.update_db_per_http(self.db.collection, self.db.user_document,
                                   self.timestamp, ts)

    def notify_emergency_not_fallen(self):
        internet_connected = super().check_internet_connection()
        # timezone berlin
        ts = datetime.datetime.fromtimestamp(
            time.time()).strftime('%Y-%m-%d %H:%M:%S')
        if internet_connected:
            self.db.update_child(self.fall, "NO_Fall_Detected")
            self.db.update_child(self.timestamp, ts)
        else:
            gsm.update_db_per_http(self.db.collection, self.db.user_document,
                                   self.fall, "NO_Fall_Detected")
            gsm.update_db_per_http(self.db.collection, self.db.user_document,
                                   self.timestamp, ts)

