"""Main module."""

from ovest.emergencyHandler import FallEmergencyHandler
from ovest.emergencyHandler import NotifyFallEmergency
from ovest.database import crud
from ovest.acceleration import Acceleration
import smbus


def main():
    # bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
    # dev_addr_acc = 0x68   # MPU6050 device address
    # accel = Acceleration.Acceleration(bus, dev_addr_acc)
    db = crud.FirebaseDatabase("myovest", "test", {"is_fall": False})
    notify = NotifyFallEmergency.NotifyFallEmergency(db, "is_fall")
    fall_emer = FallEmergencyHandler.FallEmergencyHandler(accel, notify)
    fall_emer.run_fall_emergency_handler()
