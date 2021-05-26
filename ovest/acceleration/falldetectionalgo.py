import AccModule
import math
import time


fall = False
trigger1 = False
trigger2 = False
trigger3 = False
trigger1count = 0
trigger2count = 0
trigger3count = 0

while True:
    sig = AccModule.get_signals()

    am  = math.sqrt(math.pow(sig[0], 2) + math.pow(sig[1], 2) + math.pow(sig[2], 2))

    if trigger3 == True:
        trigger3count += 1
        if trigger3count >= 10:
            
            angleChange  = math.sqrt(math.pow(sig[3], 2) + math.pow(sig[4], 2) + math.pow(sig[5], 2))
            print("The Angle Change in Trigger 3 is {}".format(angleChange))
            
            if (angleChange >=0 and angleChange <= 10):
                Fall = True
                trigger3 = False
                trigger3count = 0
                print("The Angle Change in case of Fall")
                print("Fall detected")
                exit()
            else:
                trigger3 = False
                trigger3count = 0
                print("Trigger3 Deactivated when Fall is not detected")
    if fall == True:
        print("Anet at fall={}".format(am))
        print("Gnet at fall={}".format(angleChange))
        print("Fall Detected")
        
        #Send Alert to caregiver: make sure that don't exceed 1 min
        fall = False
        
    if trigger2count >= 6:
        trigger2 = False
        trigger2count = 0
        print("Trigger 2 Deactivated: ALlow 0.5s for Orientation Change")

    if trigger1count >= 6:
        trigger1 = False
        trigger1count = 0
        print("Trigger 1 Deactivated: ALlow 0.5s for AM to break upper Threshold")

    if trigger2 == True:
        trigger2count += 1
        angleChange  = math.sqrt(math.pow(sig[3], 2) + math.pow(sig[4], 2) + math.pow(sig[5], 2))
        print("The angle Change in Trigger 2 is {}".format(angleChange))
        
        if (angleChange >= 30 and angleChange <= 400):
            trigger3 = True
            trigger2 = False
            trigger2count = 0
            print("The angle Change in Trigger 3 is {}".format(angleChange))
            print("Trigger 3 Activated")
        
    if trigger1 == True:
        trigger1count += 1
        if am >= 1.2:
            trigger2 = True
            print("Trigger 2 Activated: AM breaks upper threshold")
            trigger1 = False
            trigger1count = 0


    if (am <= 2 and trigger2 == False):
        trigger1 = True
        print("Trigger 1 Activated: AM breaks lower threshold 0.4g")

    time.sleep(0.05)   
