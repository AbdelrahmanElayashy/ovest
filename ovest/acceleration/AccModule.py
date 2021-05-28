'''
        Read Gyro and Accelerometer by Interfacing Raspberry Pi with MPU6050 using Python
'''
import smbus  

class Mpu6050:
    PWR_MGMT_1 = 0x6B
    SMPLRT_DIV = 0x19
    CONFIG = 0x1A
    GYRO_CONFIG = 0x1B
    INT_ENABLE = 0x38
    ACCEL_XOUT_H = 0x3B
    ACCEL_YOUT_H = 0x3D
    ACCEL_ZOUT_H = 0x3F
    GYRO_XOUT_H = 0x43
    GYRO_YOUT_H = 0x45
    GYRO_ZOUT_H = 0x47
    dev_addr = None
    bus = None

    def __init__(self, bus, dev_addr):
        self.dev_addr = dev_addr
        self.bus = bus
        self.mpu_init()

    def mpu_init(self):
        # write to sample rate register
        self.bus.write_byte_data(self.dev_addr, self.SMPLRT_DIV, 1)
        # Write to power management register
        self.bus.write_byte_data(self.dev_addr, self.PWR_MGMT_1, 1)
        # Write to Configuration register
        self.bus.write_byte_data(self.dev_addr, self.CONFIG, 0)
        # Write to Gyro configuration register
        self.bus.write_byte_data(self.dev_addr, self.GYRO_CONFIG, 24)
        # Write to interrupt enable register
        self.bus.write_byte_data(self.dev_addr, self.INT_ENABLE, 1)

    def read_raw_data(self, register_addr):
        # Accelero and Gyro value are 16-bit
        high = self.bus.read_byte_data(self.dev_addr, register_addr)
        low = self.bus.read_byte_data(self.dev_addr, register_addr+1)
        # concatenate higher and lower value
        value = ((high << 8) | low)
        # to get signed value from mpu6050
        if(value > 32768):
            value = value - 65536
        return value

    def get_signals(self):
        # Read Accelerometer raw value
        acc_x = self.read_raw_data(self.ACCEL_XOUT_H)
        acc_y = self.read_raw_data(self.ACCEL_YOUT_H)
        acc_z = self.read_raw_data(self.ACCEL_ZOUT_H)

        # Read Gyroscope raw value
        gyro_x = self.read_raw_data(self.GYRO_XOUT_H)
        gyro_y = self.read_raw_data(self.GYRO_YOUT_H)
        gyro_z = self.read_raw_data(self.GYRO_ZOUT_H)

        Ax = (acc_x - 686)/16384.0
        Ay = ((acc_y + 345.88)/16384.0) - 0.16
        Az = ((acc_z + 1127.777)/16384.0) + 0.1

        Gx = (gyro_x + 5.95)/131.0
        Gy = (gyro_y - 12.35)/131.0
        Gz = (gyro_z + 6.8)/131.0

        print("Gx=%.2f" % Gx, u'\u00b0' + "/s", "\tGy=%.2f" % Gy, u'\u00b0' + "/s", "\tGz=%.2f" %
               Gz, u'\u00b0' + "/s", "\tAx=%.2f g" % Ax, "\tAy=%.2f g" % Ay, "\tAz=%.2f g" % Az)

        return Ax, Ay, Az, Gx, Gy, Gz
