from ovest.acceleration import Mpu6050
from ovest.acceleration import FallDetection


class Acceleration:

    def __init__(self, bus, dev_addr):
        self.mpu = Mpu6050.Mpu6050(bus, dev_addr)
        self.fallen_algo = FallDetection.FallDetection()

    def is_fallen(self):
        sig = self.mpu.get_signals()
        status = self.fallen_algo.fall_detection(sig)
        return status
