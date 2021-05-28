import math
import time


class FallDetection:

    def __init__(self):
        self.fall = False
        self.trigger1 = False
        self.trigger2 = False
        self.trigger3 = False
        self.trigger1count = 0
        self.trigger2count = 0
        self.trigger3count = 0

    def fall_detection(self, sig):
        am = math.sqrt(math.pow(sig[0], 2) +
                       math.pow(sig[1], 2) + math.pow(sig[2], 2))

        if self.trigger3 == True:
            self.trigger3count += 1
            if self.trigger3count >= 10:

                angleChange = math.sqrt(
                    math.pow(sig[3], 2) + math.pow(sig[4], 2) + math.pow(sig[5], 2))
                print("The Angle Change in Trigger 3 is {}".format(angleChange))

                if (angleChange >= 0 and angleChange <= 10):
                    self.fall = True
                    self.trigger3 = False
                    self.trigger3count = 0
                    print("The Angle Change in case of Fall")
                    print("Fall detected")
                    #exit()
                else:
                    self.trigger3 = False
                    self.trigger3count = 0
                    print("Trigger3 Deactivated when Fall is not detected")
        if self.fall == True:
            print("Anet at fall={}".format(am))
            print("Gnet at fall={}".format(angleChange))
            print("Fall Detected")

            # Send Alert to caregiver: make sure that don't exceed 1 min
            self.fall = False
            return not self.fall

        if self.trigger2count >= 6:
            self.trigger2 = False
            self.trigger2count = 0
            print("Trigger 2 Deactivated: ALlow 0.5s for Orientation Change")

        if self.trigger1count >= 6:
            self.trigger1 = False
            self.trigger1count = 0
            print("Trigger 1 Deactivated: ALlow 0.5s for AM to break upper Threshold")

        if self.trigger2 == True:
            self.trigger2count += 1
            angleChange = math.sqrt(
                math.pow(sig[3], 2) + math.pow(sig[4], 2) + math.pow(sig[5], 2))
            print("The angle Change in Trigger 2 is {}".format(angleChange))

            if (angleChange >= 30 and angleChange <= 400):
                self.trigger3 = True
                self.trigger2 = False
                self.trigger2count = 0
                print("The angle Change in Trigger 3 is {}".format(angleChange))
                print("Trigger 3 Activated")

        if self.trigger1 == True:
            self.trigger1count += 1
            if am >= 1.2:
                self.trigger2 = True
                print("Trigger 2 Activated: AM breaks upper threshold")
                self.trigger1 = False
                self.trigger1count = 0

        if (am <= 2 and self.trigger2 == False):
            self.trigger1 = True
            print("Trigger 1 Activated: AM breaks lower threshold 0.4g")

        #time.sleep(0.05)
        return self.fall
