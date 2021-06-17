"""Main module."""

from ovest.emergencyHandler import FallEmergencyHandler, NotifyFallEmergency, OutZoneEmergencyHandler, NotifyOutZoneEmergency
from ovest.database import crud
from ovest.acceleration import Acceleration
import smbus
import _thread
import time
import datetime

def main():
    bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
    dev_addr_acc = 0x68   # MPU6050 device address
    accel = Acceleration.Acceleration(bus, dev_addr_acc)
    #timezone berlin
    ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    db = crud.FirebaseDatabase("myovest", "test", {"is_fall": "NO_Fall_Detected",
    "timestamp" : ts, "Lat" : 0, "Long" : 0})# add attributes to database
    notify_fall = NotifyFallEmergency.NotifyFallEmergency(db, "is_fall", "timestamp")
    notify_out_zone = NotifyOutZoneEmergency.NotifyOutZoneEmergency(db, "timestamp", "Lat", "Long")
    fall_emer = FallEmergencyHandler.FallEmergencyHandler(accel, notify_fall)
    out_zone_emer = OutZoneEmergencyHandler.OutZoneEmergencyHandler(notify_out_zone)
    _thread.start_new_thread(fall_emer.run_fall_emergency_handler(), () )
    _thread.start_new_thread(out_zone_emer.run_out_zone_handler(), () )
   


main()