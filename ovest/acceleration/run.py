from ovest.acceleration import AccModule
from ovest.acceleration import falldetectionalgo
import time

is_fall = False


def run(bus, dev_addr):
    mpu = AccModule.Mpu6050(bus, dev_addr)
    fall_obj = falldetectionalgo.FallDetection()
    global is_fall
    while True:
        sig = mpu.get_signals()
        is_fall = fall_obj.fall_detection(sig)
        time.sleep(0.05)
        if is_fall:
            for i in range(1000):
                print("###############FALL DETECTED#######################")


def get_is_fall():
    global is_fall
    return is_fall


def test():
    print("acceleration")
