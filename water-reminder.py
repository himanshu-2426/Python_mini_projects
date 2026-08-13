import time
from plyer import notification

def water_reminder():
        while True:
            notification.notify(
                title="HEY HIMANSHU!",
                message="Time to sip some water!",
                timeout=10
            )
            time.sleep(3)
            

water_reminder()
#ctrl+c for quit 
# notification.notify(title="hello",message="this is a plyer notification")