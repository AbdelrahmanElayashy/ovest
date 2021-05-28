from ovest.acceleration import AccModule
from ovest.acceleration import falldetectionalgo

is_fall = False


def run(bus, dev_addr):
    mpu = AccModule.Mpu6050(bus, dev_addr)
    global is_fall
    while True:
        sig = mpu.get_signals()
        #is_fall = falldetection(sig)


def get_is_fall():
    global is_fall
    return is_fall


def test():
    print("acceleration")
