"""Main module."""

from ovest.acceleration import run as accer
from ovest.alert import run as alert
from ovest.alert.gbs import run as gbs
from ovest.alert.gsm import run as gsm
from threading import Thread
import smbus


def main():
    bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
    dev_addr_acc = 0x68   # MPU6050 device address
    accer.run(bus, dev_addr_acc)
