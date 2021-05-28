import http.client as httplib
from ovest.database import crud
from ovest.emergencyHandler import NotifyEmergency as emr
import time


class NotifyFallEmergency(emr.NotifyEmergency):
    def __init__(self, database, db_attr):
        self.db = database
        self.db_attr = db_attr

    def notify_emergency_fallen(self):
        internet_connected = super().check_internet_connection()
        if internet_connected:
            self.db.update_child(self.db_attr, True)
        else:
            # TODO what happen if not?
            print("no connection")

    def notify_emergency_not_fallen(self):
        internet_connected = super().check_internet_connection()
        if internet_connected:
            self.db.update_child(self.db_attr, False)
        else:
            # TODO what happen if not?
            print("no connection")
        return True



