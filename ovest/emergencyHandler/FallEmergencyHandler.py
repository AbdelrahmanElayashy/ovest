import time


class FallEmergencyHandler:
    def __init__(self, acceleration, notify_emergency):
        self.acceleration = acceleration
        self.notify = notify_emergency

    def run_fall_emergency_handler(self):
        while True:
            status = self.acceleration.is_fallen()
            time.sleep(0.05)
            if status:
                self.notify.notify_emergency_fallen()
                time.sleep(4)
                self.notify.notify_emergency_not_fallen()
                for i in range(1000):
                    print("###############FALL DETECTED#######################")
