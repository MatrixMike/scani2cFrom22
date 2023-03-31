# esp8266
# 29 March 2023
import machine
import time
pin = machine.Pin(2, machine.Pin.OUT)
# 0 is safe but not visible
for i in range(100):
    pin.on()
    time.sleep(0.5)
    pin.off()
    time.sleep(0.5)
    print(i)
    